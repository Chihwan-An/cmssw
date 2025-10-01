import FWCore.ParameterSet.Config as cms

hltL1sTauVeryBigOR = cms.EDFilter( "HLTL1TSeed",
    saveTags = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_LooseIsoEG22er2p1_IsoTau26er2p1_dR_Min0p3 OR L1_LooseIsoEG24er2p1_IsoTau27er2p1_dR_Min0p3 OR L1_LooseIsoEG22er2p1_Tau70er2p1_dR_Min0p3 OR L1_SingleTau120er2p1 OR L1_SingleTau130er2p1 OR L1_DoubleTau70er2p1 OR L1_DoubleIsoTau28er2p1 OR L1_DoubleIsoTau30er2p1 OR L1_DoubleIsoTau32er2p1 OR L1_DoubleIsoTau34er2p1 OR L1_DoubleIsoTau35er2p1 OR L1_DoubleIsoTau36er2p1 OR L1_Mu18er2p1_Tau24er2p1 OR L1_Mu18er2p1_Tau26er2p1 OR L1_Mu22er2p1_IsoTau30er2p1 OR L1_Mu22er2p1_IsoTau32er2p1 OR L1_Mu22er2p1_IsoTau34er2p1 OR L1_Mu22er2p1_IsoTau40er2p1 OR L1_Mu22er2p1_Tau70er2p1 OR L1_IsoTau52er2p1_QuadJet36er2p5 OR L1_DoubleTau_Iso34_Iso23_er2p1_Jet55_RmOvlp_dR0p5 OR L1_DoubleTau_Iso34_Iso26_er2p1_Jet55_RmOvlp_dR0p5 OR L1_DoubleTau_Iso34_Iso23_er2p1_Jet70_RmOvlp_dR0p5 OR L1_DoubleTau_Iso34_Iso26_er2p1_Jet70_RmOvlp_dR0p5" ),
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