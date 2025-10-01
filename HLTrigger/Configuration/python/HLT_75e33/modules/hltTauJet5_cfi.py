import FWCore.ParameterSet.Config as cms

hltTauJet5 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltAK4CaloJetsPFEt5" ),
    triggerType = cms.int32( 84 ),
    MinE = cms.double( -1.0 ),
    MinPt = cms.double( 5.0 ),
    MinMass = cms.double( -1.0 ),
    MaxMass = cms.double( -1.0 ),
    MinEta = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
