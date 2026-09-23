#!/bin/bash
#
# Shared setup for the Phase-II HLT validation condor jobs. Sourced, never run.
#

# The release is built for a SCRAM arch that may not match the worker node, so
# re-exec inside the matching container before touching anything else. Call as
#   hltval_reexec "$0" "$@"
hltval_reexec() {
    [ -n "$HLTVAL_IN_CONTAINER" ] && return 0
    local script=$1; shift
    local arch want_el host_el wrapper
    arch=$(ls "$CMSSW_BASE_DIR/.SCRAM" 2>/dev/null | grep -m1 '_amd64_\|_aarch64_')
    want_el=${arch%%_*}                                   # e.g. el9
    host_el=el$(sed -n 's/^VERSION_ID="\?\([0-9]*\).*/\1/p' /etc/os-release)
    [ -z "$want_el" ] || [ "$want_el" = "$host_el" ] && return 0
    wrapper=/cvmfs/cms.cern.ch/common/cmssw-$want_el
    if [ ! -x "$wrapper" ]; then
        echo "need $want_el but $wrapper is not available on $(hostname)" >&2
        exit 3
    fi
    echo "host is $host_el, release needs $want_el -> re-exec under $wrapper"
    export HLTVAL_IN_CONTAINER=1
    exec "$wrapper" -- "$script" "$@"
}

hltval_setup_cmssw() {
    source /cvmfs/cms.cern.ch/cmsset_default.sh || exit 5
    cd "$CMSSW_BASE_DIR/src" || exit 5
    eval "$(scramv1 runtime -sh)" || exit 5

    # Some worker nodes ship an incomplete /etc/cvmfs/CMS_SITECONF - the tree
    # that /cvmfs/cms.cern.ch/SITECONF/local symlinks to - and there the
    # relative ../T1_US_FNAL path in <data-access> does not resolve, so
    # PoolSource dies with "Unable to construct any file locator". Point at a
    # complete copy on the shared filesystem instead. cmsset_default.sh always
    # sets SITECONFIG_PATH, so this has to overwrite it rather than only fill
    # in a default.
    local siteconf=${HLTVAL_SITECONF:-/data6/Users/achihwan/tauwiki/epr_snu/siteconf/local}
    if [ -r "$siteconf/JobConfig/site-local-config.xml" ] &&
       [ -r "$siteconf/../T1_US_FNAL/storage.json" ]; then
        export SITECONFIG_PATH="$siteconf"
        echo "SITECONFIG_PATH -> $SITECONFIG_PATH"
    else
        echo "no usable SITECONF at $siteconf, keeping $SITECONFIG_PATH" >&2
    fi
}

# cmsRun writes into a scratch area and the result is moved into place only
# once it is complete, so a killed job never leaves a half written file
hltval_enter_scratch() {
    SCRATCH=${_CONDOR_SCRATCH_DIR:-${TMPDIR:-/tmp}}/hltval_$$
    mkdir -p "$SCRATCH" || exit 6
    trap 'rm -rf "$SCRATCH"' EXIT
    cd "$SCRATCH" || exit 6
}

# VarParsing rewrites outputFile - with maxEvents set it becomes
# <name>_numEvent<N>.root - so take whatever single ROOT file came out instead
# of assuming the name we asked for. Sets HLTVAL_PRODUCED.
hltval_single_root() {
    local found
    mapfile -t found < <(find "$SCRATCH" -maxdepth 1 -type f -name '*.root')
    if [ ${#found[@]} -ne 1 ]; then
        echo "expected exactly one ROOT file in $SCRATCH, got ${#found[@]}:" >&2
        printf '  %s\n' "${found[@]}" >&2
        exit 7
    fi
    HLTVAL_PRODUCED=${found[0]}
}

hltval_deliver() {
    local out=$1
    mkdir -p "$(dirname "$out")"
    mv "$HLTVAL_PRODUCED" "$out" || exit 8
    echo "=== done: $out ($(stat -c %s "$out") bytes) ==="
}
