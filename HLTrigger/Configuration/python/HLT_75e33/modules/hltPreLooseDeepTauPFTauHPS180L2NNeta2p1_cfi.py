import FWCore.ParameterSet.Config as cms

hltPreLooseDeepTauPFTauHPS180L2NNeta2p1 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)