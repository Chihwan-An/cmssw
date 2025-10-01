import FWCore.ParameterSet.Config as cms

hltOnlineBeamSpotDevice = cms.EDProducer( "BeamSpotDeviceProducer@alpaka",
    src = cms.InputTag( "hltOnlineBeamSpot" ),
    alpaka = cms.untracked.PSet(  backend = cms.untracked.string( "" ) )
)
