import FWCore.ParameterSet.Config as cms

hltL1VBFDiJetIsoTau = cms.EDFilter( "HLTL1TSeed",
    saveTags = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleJet45_Mass_Min550_IsoTau45er2p1_RmOvlp_dR0p5 OR L1_DoubleJet45_Mass_Min600_IsoTau45er2p1_RmOvlp_dR0p5 OR L1_DoubleJet45_Mass_Min700_IsoTau45er2p1_RmOvlp_dR0p5 OR L1_DoubleJet45_Mass_Min800_IsoTau45er2p1_RmOvlp_dR0p5" ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1MuonShowerInputTag = cms.InputTag( 'hltGtStage2Digis','MuonShower' ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1EtSumZdcInputTag = cms.InputTag( 'hltGtStage2Digis','EtSumZDC' )
)