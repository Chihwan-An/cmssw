import FWCore.ParameterSet.Config as cms

from ..sequences.HLTIterativeTrackingIteration0_cfi import *
from ..sequences.HLTIterativeTrackingDoubletRecovery_cfi import *
from ..modules.hltMergedTracks_cfi import *

HLTIterativeTrackingIter02 = cms.Sequence( HLTIterativeTrackingIteration0 + HLTIterativeTrackingDoubletRecovery + hltMergedTracks )
