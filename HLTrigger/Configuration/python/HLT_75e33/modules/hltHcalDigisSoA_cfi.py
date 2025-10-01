import FWCore.ParameterSet.Config as cms

hltHcalDigisSoA = cms.EDProducer( "HcalDigisSoAProducer@alpaka",
    hbheDigisLabel = cms.InputTag( "hltHcalDigis" ),
    qie11DigiLabel = cms.InputTag( "hltHcalDigis" ),
    digisLabelF01HE = cms.string( "f01HEDigis" ),
    digisLabelF5HB = cms.string( "f5HBDigis" ),
    digisLabelF3HB = cms.string( "f3HBDigis" ),
    maxChannelsF01HE = cms.uint32( 10000 ),
    maxChannelsF5HB = cms.uint32( 10000 ),
    maxChannelsF3HB = cms.uint32( 10000 ),
    alpaka = cms.untracked.PSet(  backend = cms.untracked.string( "" ) )
)
