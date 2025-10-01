import FWCore.ParameterSet.Config as cms

from ..modules.hltIter0IterL3MuonPixelSeedsFromPixelTracks_cfi import *
from ..modules.hltIter0IterL3MuonPixelSeedsFromPixelTracksFiltered_cfi import *
from ..modules.hltIter0IterL3MuonCkfTrackCandidates_cfi import *
from ..modules.hltIter0IterL3MuonCtfWithMaterialTracks_cfi import *
from ..modules.hltIter0IterL3MuonTrackCutClassifier_cfi import *
from ..modules.hltIter0IterL3MuonTrackSelectionHighPurity_cfi import *

HLTIterativeTrackingIteration0ForIterL3Muon = cms.Sequence( hltIter0IterL3MuonPixelSeedsFromPixelTracks + hltIter0IterL3MuonPixelSeedsFromPixelTracksFiltered + hltIter0IterL3MuonCkfTrackCandidates + hltIter0IterL3MuonCtfWithMaterialTracks + hltIter0IterL3MuonTrackCutClassifier + hltIter0IterL3MuonTrackSelectionHighPurity )
