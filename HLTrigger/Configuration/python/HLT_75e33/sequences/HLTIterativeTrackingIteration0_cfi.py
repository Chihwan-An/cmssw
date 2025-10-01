import FWCore.ParameterSet.Config as cms

from ..modules.hltIter0PFLowPixelSeedsFromPixelTracks_cfi import *
from ..modules.hltIter0PFlowCkfTrackCandidatesMkFitSiPixelHits_cfi import *
from ..modules.hltSiStripRecHits_cfi import *
from ..modules.hltIter0PFlowCkfTrackCandidatesMkFitSiStripHits_cfi import *
from ..modules.hltIter0PFlowCkfTrackCandidatesMkFitEventOfHits_cfi import *
from ..modules.hltIter0PFlowCkfTrackCandidatesMkFitSeeds_cfi import *
from ..modules.hltIter0PFlowCkfTrackCandidatesMkFit_cfi import *
from ..modules.hltIter0PFlowCkfTrackCandidates_cfi import *
from ..modules.hltIter0PFlowCtfWithMaterialTracks_cfi import *
from ..modules.hltIter0PFlowTrackCutClassifier_cfi import *
from ..modules.hltIter0PFlowTrackSelectionHighPurity_cfi import *

HLTIterativeTrackingIteration0 = cms.Sequence( hltIter0PFLowPixelSeedsFromPixelTracks + hltIter0PFlowCkfTrackCandidatesMkFitSiPixelHits + hltSiStripRecHits + hltIter0PFlowCkfTrackCandidatesMkFitSiStripHits + hltIter0PFlowCkfTrackCandidatesMkFitEventOfHits + hltIter0PFlowCkfTrackCandidatesMkFitSeeds + hltIter0PFlowCkfTrackCandidatesMkFit + hltIter0PFlowCkfTrackCandidates + hltIter0PFlowCtfWithMaterialTracks + hltIter0PFlowTrackCutClassifier + hltIter0PFlowTrackSelectionHighPurity )
