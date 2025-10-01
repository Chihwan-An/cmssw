import FWCore.ParameterSet.Config as cms

from ..modules.hltIterL3OISeedsFromL2Muons_cfi import *
from ..modules.hltIterL3OITrackCandidates_cfi import *
from ..modules.hltIterL3OIMuCtfWithMaterialTracks_cfi import *
from ..modules.hltIterL3OIMuonTrackCutClassifier_cfi import *
from ..modules.hltIterL3OIMuonTrackSelectionHighPurity_cfi import *
from ..modules.hltL3MuonsIterL3OI_cfi import *

HLTIterL3OImuonTkCandidateSequence = cms.Sequence( hltIterL3OISeedsFromL2Muons + hltIterL3OITrackCandidates + hltIterL3OIMuCtfWithMaterialTracks + hltIterL3OIMuonTrackCutClassifier + hltIterL3OIMuonTrackSelectionHighPurity + hltL3MuonsIterL3OI )
