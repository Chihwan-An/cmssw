import FWCore.ParameterSet.Config as cms

from ..modules.hltDoubletRecoveryClustersRefRemoval_cfi import *
from ..modules.hltDoubletRecoveryMaskedMeasurementTrackerEvent_cfi import *
from ..modules.hltDoubletRecoveryPixelLayersAndRegions_cfi import *
from ..modules.hltDoubletRecoveryPFlowPixelClusterCheck_cfi import *
from ..modules.hltDoubletRecoveryPFlowPixelHitDoublets_cfi import *
from ..modules.hltDoubletRecoveryPFlowPixelSeeds_cfi import *
from ..modules.hltDoubletRecoveryPFlowCkfTrackCandidates_cfi import *
from ..modules.hltDoubletRecoveryPFlowCtfWithMaterialTracks_cfi import *
from ..modules.hltDoubletRecoveryPFlowTrackCutClassifier_cfi import *
from ..modules.hltDoubletRecoveryPFlowTrackSelectionHighPurity_cfi import *

HLTIterativeTrackingDoubletRecovery = cms.Sequence( hltDoubletRecoveryClustersRefRemoval + hltDoubletRecoveryMaskedMeasurementTrackerEvent + hltDoubletRecoveryPixelLayersAndRegions + hltDoubletRecoveryPFlowPixelClusterCheck + hltDoubletRecoveryPFlowPixelHitDoublets + hltDoubletRecoveryPFlowPixelSeeds + hltDoubletRecoveryPFlowCkfTrackCandidates + hltDoubletRecoveryPFlowCtfWithMaterialTracks + hltDoubletRecoveryPFlowTrackCutClassifier + hltDoubletRecoveryPFlowTrackSelectionHighPurity )
