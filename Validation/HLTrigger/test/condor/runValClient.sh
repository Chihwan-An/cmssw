#!/bin/bash
#
# Harvesting job: merge every per-file DQMIO output of one sample and run the
# HLTGenValClient over it.
#
#   runValClient.sh <CMSSW_BASE> <dqmio_dir> <output.root> <outTag>
#
set -o pipefail
source "$(dirname "$(readlink -f "$0")")/jobcommon.sh"

CMSSW_BASE_DIR=$1
DQMIO_DIR=$2
OUTFILE=$3
OUT_TAG=${4:-All}

if [ -z "$CMSSW_BASE_DIR" ] || [ -z "$DQMIO_DIR" ] || [ -z "$OUTFILE" ]; then
    echo "usage: $0 <CMSSW_BASE> <dqmio_dir> <output.root> [outTag]" >&2
    exit 2
fi

hltval_reexec "$0" "$@"

echo "=== $(date) on $(hostname) ==="
echo "inputs : $DQMIO_DIR"
echo "output : $OUTFILE"
echo "outTag : $OUT_TAG"

hltval_setup_cmssw
hltval_enter_scratch

# a plain list file keeps the command line short however many inputs there are
find "$DQMIO_DIR" -maxdepth 1 -type f -name '*_DQM.root' -printf 'file:%p\n' |
    sort > "$SCRATCH/dqmio.txt"
N=$(wc -l < "$SCRATCH/dqmio.txt")
echo "harvesting $N DQMIO file(s)"
if [ "$N" -eq 0 ]; then
    echo "nothing to harvest in $DQMIO_DIR" >&2
    exit 4
fi

cmsRun "$CMSSW_BASE_DIR/src/Validation/HLTrigger/test/runValClient_cfg.py" \
    "inputFiles_load=$SCRATCH/dqmio.txt" \
    "outTag=$OUT_TAG"
RC=$?
if [ $RC -ne 0 ]; then
    echo "cmsRun failed (exit $RC)" >&2
    exit $RC
fi

# the list file is not a ROOT file, so the single-ROOT check still holds
hltval_single_root
hltval_deliver "$OUTFILE"
