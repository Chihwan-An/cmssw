import FWCore.ParameterSet.Config as cms

hltIter3IterL3FromL1MuonPixelHitDoublets = cms.EDProducer( "HitPairEDProducer",
    seedingLayers = cms.InputTag( "hltIter3IterL3FromL1MuonPixelLayersAndRegions" ),
    trackingRegions = cms.InputTag( "hltIter3IterL3FromL1MuonTrackingRegions" ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    clusterCheck = cms.InputTag( "hltIter3IterL3FromL1MuonPixelClusterCheck" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( False ),
    maxElement = cms.uint32( 0 ),
    maxElementTotal = cms.uint32( 50000000 ),
    putEmptyIfMaxElementReached = cms.bool( False ),
    layerPairs = cms.vuint32( 0 )
)
