import FWCore.ParameterSet.Config as cms

hltL1JetsHLTPFTauLooseSingleTauWPDeepTauMatch = cms.EDProducer( "L1THLTTauMatching",
    L1TauTrigger = cms.InputTag( "hltL1SingleNNTau150" ),
    JetSrc = cms.InputTag( "hltHpsSelectedPFTauLooseTauWPDeepTau" ),
    EtMin = cms.double( 0.0 ),
    ReduceTauContent = cms.bool( True ),
    KeepOriginalVertex = cms.bool( False )
)
