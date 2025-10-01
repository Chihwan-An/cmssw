import FWCore.ParameterSet.Config as cms

hltIter3IterL3FromL1MuonMaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    src = cms.InputTag( "hltMeasurementTrackerEvent" ),
    clustersToSkip = cms.InputTag( "hltIter3IterL3FromL1MuonClustersRefRemoval" ),
    phase2clustersToSkip = cms.InputTag( "" )
)
