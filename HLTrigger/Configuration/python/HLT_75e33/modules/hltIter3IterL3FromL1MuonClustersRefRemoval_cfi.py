import FWCore.ParameterSet.Config as cms

hltIter3IterL3FromL1MuonClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trajectories = cms.InputTag( "hltIter0IterL3FromL1MuonTrackSelectionHighPurity" ),
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    pixelClusters = cms.InputTag( "hltSiPixelClusters" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    oldClusterRemovalInfo = cms.InputTag( "" ),
    TrackQuality = cms.string( "highPurity" ),
    maxChi2 = cms.double( 16.0 ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    overrideTrkQuals = cms.InputTag( "" )
)
