import FWCore.ParameterSet.Config as cms

hltSiPixelDigiErrors = cms.EDProducer( "SiPixelDigiErrorsFromSoAAlpaka",
    digiErrorSoASrc = cms.InputTag( "hltSiPixelClustersSoA" ),
    fmtErrorsSoASrc = cms.InputTag( "hltSiPixelClustersSoA" ),
    CablingMapLabel = cms.string( "" ),
    UsePhase1 = cms.bool( True ),
    ErrorList = cms.vint32( 29 ),
    UserErrorList = cms.vint32( 40 )
)
