import FWCore.ParameterSet.Config as cms

hltDoubletRecoveryMaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    src = cms.InputTag( "hltMeasurementTrackerEvent" ),
    clustersToSkip = cms.InputTag( "hltDoubletRecoveryClustersRefRemoval" ),
    phase2clustersToSkip = cms.InputTag( "" )
)
