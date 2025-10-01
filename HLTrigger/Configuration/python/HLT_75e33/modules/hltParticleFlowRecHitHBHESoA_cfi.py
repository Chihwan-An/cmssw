import FWCore.ParameterSet.Config as cms

hltParticleFlowRecHitHBHESoA = cms.EDProducer( "PFRecHitSoAProducerHCAL@alpaka",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( "hltHbheRecoSoA" ),
        params = cms.ESInputTag( "hltESPPFRecHitHCALParams","" )
      )
    ),
    topology = cms.ESInputTag( "hltESPPFRecHitHCALTopology","" ),
    synchronise = cms.untracked.bool( False ),
    alpaka = cms.untracked.PSet(  backend = cms.untracked.string( "" ) )
)
