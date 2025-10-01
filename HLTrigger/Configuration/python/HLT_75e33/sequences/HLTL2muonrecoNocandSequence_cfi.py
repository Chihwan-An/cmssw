import FWCore.ParameterSet.Config as cms

from ..sequences.HLTMuonLocalRecoSequence_cfi import *
from ..modules.hltL2OfflineMuonSeeds_cfi import *
from ..modules.hltL2MuonSeeds_cfi import *
from ..modules.hltL2Muons_cfi import *

HLTL2muonrecoNocandSequence = cms.Sequence(
    HLTMuonLocalRecoSequence +
    hltL2OfflineMuonSeeds +
    hltL2MuonSeeds +
    hltL2Muons )