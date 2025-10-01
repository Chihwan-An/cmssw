import FWCore.ParameterSet.Config as cms

hltDoubletRecoveryClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trajectories = cms.InputTag( "hltIter0PFlowTrackSelectionHighPurity" ),
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    pixelClusters = cms.InputTag( "hltSiPixelClusters" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    oldClusterRemovalInfo = cms.InputTag( "" ),
    TrackQuality = cms.string( "highPurity" ),
    maxChi2 = cms.double( 16.0 ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    overrideTrkQuals = cms.InputTag( "" )
)
