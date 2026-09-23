#!/bin/bash
#
# One Phase-II HLT validation source job = one input ROOT file.
#
#   runValSource.sh <CMSSW_BASE> <input.root> <output_DQM.root> [sampleLabel] [maxEvents]
#
set -o pipefail
source "$(dirname "$(readlink -f "$0")")/jobcommon.sh"

CMSSW_BASE_DIR=$1
INFILE=$2
OUTFILE=$3
SAMPLE_LABEL=${4:-test}
MAX_EVENTS=${5:--1}

if [ -z "$CMSSW_BASE_DIR" ] || [ -z "$INFILE" ] || [ -z "$OUTFILE" ]; then
    echo "usage: $0 <CMSSW_BASE> <input.root> <output_DQM.root> [sampleLabel] [maxEvents]" >&2
    exit 2
fi

hltval_reexec "$0" "$@"

echo "=== $(date) on $(hostname) ==="
echo "input  : $INFILE"
echo "output : $OUTFILE"
echo "release: $CMSSW_BASE_DIR"

if [ ! -f "$INFILE" ]; then
    echo "input file does not exist: $INFILE" >&2
    exit 4
fi

hltval_setup_cmssw
hltval_enter_scratch

cmsRun "$CMSSW_BASE_DIR/src/Validation/HLTrigger/test/runPhaseIIValSource_cfg.py" \
    "inputFiles=file:$INFILE" \
    "outputFile=out_DQM.root" \
    "sampleLabel=$SAMPLE_LABEL" \
    "maxEvents=$MAX_EVENTS"
RC=$?
if [ $RC -ne 0 ]; then
    echo "cmsRun failed (exit $RC)" >&2
    exit $RC
fi

hltval_single_root
hltval_deliver "$OUTFILE"
