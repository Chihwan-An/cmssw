#!/usr/bin/env python3
"""
Driver for the Phase-II HLT validation.

Modes
  local   : run every input in this shell, one cmsRun after the other
  condor  : submit one HTCondor job per input ROOT file (DQMIO/source step only)
  harvest : merge the per-file DQMIO outputs and run the harvesting client

Inputs are either DBS dataset names (/Primary/ProcessedDataset/DataTier) or
local paths - a directory, a glob or a plain ROOT file.
"""

import argparse
import glob
import os
import shutil
import subprocess
import sys
import tempfile

SOURCE_CFG = "Validation/HLTrigger/test/runPhaseIIValSource_cfg.py"
CLIENT_CFG = "Validation/HLTrigger/test/runValClient_cfg.py"
SOURCE_JOB = "Validation/HLTrigger/test/condor/runValSource.sh"
CLIENT_JOB = "Validation/HLTrigger/test/condor/runValClient.sh"

DQM_NAME = "DQM_V0001_R000000001__HLT__Validation__{}.root"


def cmssw_base():
    base = os.environ.get("CMSSW_BASE")
    if base:
        return base
    # .../$CMSSW_BASE/src/Validation/HLTrigger/test/doPhaseIIValidation.py
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(here, "..", "..", "..", ".."))


def lookup_datasets(sample_tag):

    primary_datasets = ["RelValZpToMM_m6000_14TeV","RelValZpToEE_m6000_14TeV","RelValZpTT_1500_14","RelValTTbarToDilepton_14TeV","RelValQCD_Pt15To7000_Flat_14","RelValTTbar_14TeV"]
    return [f"/{p}/{sample_tag}/GEN-SIM-RECO" for p in primary_datasets]


def is_dbs_name(entry):
    """DBS names are /Primary/ProcessedDataset/DataTier - three non empty fields."""
    if entry.startswith("dbs:"):
        return True
    if entry.endswith(".root") or "*" in entry or "?" in entry:
        return False
    parts = entry.split("/")
    return entry.startswith("/") and len(parts) == 4 and all(parts[1:])


def expand_local(entry):
    """A directory, a glob or a single file -> sorted list of ROOT files."""
    if os.path.isdir(entry):
        files = glob.glob(os.path.join(entry, "*.root"))
    else:
        files = glob.glob(entry)
    return sorted(os.path.abspath(f) for f in files if f.endswith(".root"))


def group_inputs(entries):
    """-> [(label, kind, [payload, ...]), ...] with kind in {'dbs', 'local'}."""
    groups = []
    for entry in entries:
        if is_dbs_name(entry):
            name = entry[len("dbs:"):] if entry.startswith("dbs:") else entry
            label = "__".join(name.split("/")[1:3])
            groups.append((label, "dbs", ["dbs:" + name]))
            continue

        files = expand_local(entry)
        if not files:
            raise SystemExit(f"no ROOT file matches '{entry}'")
        # every local input is labelled by the directory holding the files,
        # never by slicing the path the way a DBS name would be sliced
        label = os.path.basename(os.path.dirname(files[0])) or "localfiles"
        for existing in groups:
            if existing[0] == label and existing[1] == "local":
                existing[2].extend(files)
                break
        else:
            groups.append((label, "local", files))
    return groups


def dqm_dir(outdir, label):
    return os.path.join(outdir, label, "DQMIO")


def dqm_file(outdir, label, payload):
    if payload.startswith("dbs:"):
        stem = label
    else:
        stem = os.path.splitext(os.path.basename(payload))[0]
    return os.path.join(dqm_dir(outdir, label), stem + "_DQM.root")


def run(cmd, cwd=None):
    print("+ " + " ".join(cmd), flush=True)
    rc = subprocess.Popen(cmd, cwd=cwd).wait()
    if rc != 0:
        raise SystemExit(f"command failed with exit code {rc}: {' '.join(cmd)}")


# ---------------------------------------------------------------- local mode

def run_source(base, payload, out_dqm, sample_tag, max_events=-1):
    os.makedirs(os.path.dirname(out_dqm), exist_ok=True)
    scratch = tempfile.mkdtemp(prefix="hltval_", dir=os.path.dirname(out_dqm))
    try:
        run(["cmsRun", os.path.join(base, "src", SOURCE_CFG),
             "inputFiles=" + payload,
             "outputFile=out_DQM.root",
             f"sampleLabel={sample_tag}",
             f"maxEvents={max_events}"], cwd=scratch)
        # VarParsing rewrites outputFile (out_DQM_numEvent<N>.root when
        # maxEvents is set), so pick up whatever came out
        produced = glob.glob(os.path.join(scratch, "*.root"))
        if len(produced) != 1:
            raise SystemExit(f"expected one ROOT file in {scratch}, got {produced}")
        shutil.move(produced[0], out_dqm)
    finally:
        shutil.rmtree(scratch, ignore_errors=True)


def mode_local(args, base, groups):
    for label, kind, payloads in groups:
        for payload in payloads:
            arg = payload if kind == "dbs" else "file:" + payload
            run_source(base, arg, dqm_file(args.outdir, label, payload), args.sampletag,
                       args.maxevents)
        harvest(args, base, label)


# -------------------------------------------------------------- harvest mode

def harvest(args, base, label):
    produced = sorted(glob.glob(os.path.join(dqm_dir(args.outdir, label), "*_DQM.root")))
    if not produced:
        print(f"[{label}] nothing to harvest in {dqm_dir(args.outdir, label)}", file=sys.stderr)
        return

    out_tag = label
    dest = os.path.join(args.outdir, label, DQM_NAME.format(out_tag))
    scratch = tempfile.mkdtemp(prefix="harvest_", dir=os.path.join(args.outdir, label))
    try:
        # VarParsing reads a plain list file, so the number of inputs is not
        # limited by the length of the command line
        listfile = os.path.join(scratch, "dqmio.txt")
        with open(listfile, "w") as fh:
            fh.write("".join("file:" + f + "\n" for f in produced))
        run(["cmsRun", os.path.join(base, "src", CLIENT_CFG),
             "inputFiles_load=" + listfile,
             f"outTag={out_tag}"], cwd=scratch)
        shutil.move(os.path.join(scratch, DQM_NAME.format(out_tag)), dest)
        print(f"[{label}] harvested {len(produced)} file(s) -> {dest}")
    finally:
        shutil.rmtree(scratch, ignore_errors=True)


HARVEST_JDS = """\
universe              = vanilla
executable            = {executable}
arguments             = {base} {dqmio} {outfile} {label}
getenv                = False
should_transfer_files = NO
stream_output         = True
stream_error          = True
log                   = {logdir}/harvest_{label}_$(Cluster).log
output                = {logdir}/harvest_{label}_$(Cluster).out
error                 = {logdir}/harvest_{label}_$(Cluster).err
RequestCpus           = 1
RequestMemory         = {memory}
requirements          = {requirements}
queue
"""


def mode_harvest(args, base, groups):
    """Harvesting also runs cmsRun, so it goes to a worker node as well - the
    submit host may not even be able to run the release."""
    executable = os.path.join(base, "src", CLIENT_JOB)
    if not os.access(executable, os.X_OK):
        raise SystemExit(f"{executable} is missing or not executable")

    submitted = []
    for label, _kind, _payloads in groups:
        dqmio = dqm_dir(args.outdir, label)
        produced = sorted(glob.glob(os.path.join(dqmio, "*_DQM.root")))
        if not produced:
            print(f"[{label}] nothing to harvest in {dqmio}", file=sys.stderr)
            continue

        jobdir = os.path.join(args.outdir, label, "condor")
        logdir = os.path.join(jobdir, "log")
        os.makedirs(logdir, exist_ok=True)
        dest = os.path.join(args.outdir, label, DQM_NAME.format(label))

        jds = os.path.join(jobdir, f"{label}_harvest.jds")
        with open(jds, "w") as fh:
            fh.write(HARVEST_JDS.format(executable=executable, base=base,
                                        dqmio=dqmio, outfile=dest, label=label,
                                        logdir=logdir, memory=args.memory,
                                        requirements=args.requirements))
        print(f"[{label}] harvesting {len(produced)} file(s) -> {dest}")
        submitted.append(jds)

    submit_all(args, submitted)


# --------------------------------------------------------------- condor mode

JDS_TEMPLATE = """\
universe              = vanilla
executable            = {executable}
arguments             = {base} $(infile) $(outfile) {sample_tag} {max_events}
getenv                = False
should_transfer_files = NO
# write the logs as the job runs, otherwise a job that dies late looks silent
stream_output         = True
stream_error          = True
log                   = {logdir}/{label}_$(Cluster).log
output                = {logdir}/{label}_$(Cluster)_$(Process).out
error                 = {logdir}/{label}_$(Cluster)_$(Process).err
RequestCpus           = {cpus}
RequestMemory         = {memory}
# the release ships no x86-64-v2 build of the CORAL externals, so cmsRun dies
# with an illegal instruction on a v2 node - keep the jobs on v3 and above
requirements          = {requirements}
queue infile, outfile from {listfile}
"""


def mode_condor(args, base, groups):
    executable = os.path.join(base, "src", SOURCE_JOB)
    if not os.access(executable, os.X_OK):
        raise SystemExit(f"{executable} is missing or not executable")

    submitted = []
    for label, kind, payloads in groups:
        if kind == "dbs":
            print(f"[{label}] skipped: condor mode takes local files, not DBS names",
                  file=sys.stderr)
            continue

        jobdir = os.path.join(args.outdir, label, "condor")
        logdir = os.path.join(jobdir, "log")
        os.makedirs(logdir, exist_ok=True)
        os.makedirs(dqm_dir(args.outdir, label), exist_ok=True)

        listfile = os.path.join(jobdir, "jobs.list")
        with open(listfile, "w") as fh:
            for payload in payloads:
                fh.write(f"{payload}, {dqm_file(args.outdir, label, payload)}\n")

        jds = os.path.join(jobdir, f"{label}.jds")
        with open(jds, "w") as fh:
            fh.write(JDS_TEMPLATE.format(executable=executable, base=base,
                                         sample_tag=args.sampletag or "test",
                                         max_events=args.maxevents,
                                         logdir=logdir, label=label,
                                         cpus=args.cpus, memory=args.memory,
                                         requirements=args.requirements,
                                         listfile=listfile))
        print(f"[{label}] {len(payloads)} job(s) -> {jds}")
        submitted.append(jds)

    submit_all(args, submitted)
    if submitted:
        print("\nonce the jobs are done, harvest with:\n"
              f"  {sys.argv[0]} --mode harvest --inputfiles {' '.join(args.inputfiles)}"
              f" --sampletag {args.sampletag} --outdir {args.outdir}")


def submit_all(args, submitted):
    if not submitted:
        return
    if args.no_submit or shutil.which("condor_submit") is None:
        why = "--no-submit given" if args.no_submit else "condor_submit not on PATH"
        print(f"\nnot submitting ({why}), run this on the submit node:")
        for jds in submitted:
            print(f"  condor_submit {jds}")
    else:
        for jds in submitted:
            run(["condor_submit", jds])


# --------------------------------------------------------------------- main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Phase II Validation')
    parser.add_argument("--mode", choices=["local", "condor", "harvest"], default="local",
                        help='run here, submit one condor job per file, or harvest')
    parser.add_argument("--inputdbsnames", type=str, nargs="+", default=None, help='input datasets')
    parser.add_argument("--inputfiles", type=str, nargs="+", default=None,
                        help='local ROOT files, globs or directories')
    parser.add_argument("--sampletag", type=str, default=None, help='sample tag')
    parser.add_argument("--outdir", type=str, default=os.getcwd(),
                        help='base directory for the DQM output')
    parser.add_argument("--cpus", type=int, default=1, help='RequestCpus per condor job')
    parser.add_argument("--memory", type=int, default=4000, help='RequestMemory per condor job in MB')
    parser.add_argument("--maxevents", type=int, default=-1,
                        help='events per job, -1 for the whole file')
    parser.add_argument("--requirements", type=str,
                        default='(Microarch =?= "x86_64-v3") || (Microarch =?= "x86_64-v4")',
                        help='condor requirements expression')
    parser.add_argument("--no-submit", action="store_true",
                        help='write the condor files but do not submit them')

    args = parser.parse_args()
    args.outdir = os.path.abspath(args.outdir)

    entries = list(args.inputfiles or []) + list(args.inputdbsnames or [])
    if not entries:
        entries = lookup_datasets(args.sampletag)
    args.inputfiles = entries

    base = cmssw_base()
    groups = group_inputs(entries)

    {"local": mode_local, "condor": mode_condor, "harvest": mode_harvest}[args.mode](
        args, base, groups)
