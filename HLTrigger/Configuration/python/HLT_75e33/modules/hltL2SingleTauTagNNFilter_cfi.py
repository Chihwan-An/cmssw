import FWCore.ParameterSet.Config as cms

hltL2SingleTauTagNNFilter = cms.EDFilter( "L2TauTagFilter",
    saveTags = cms.bool( True ),
    nExpected = cms.int32( 1 ),
    #L1TauSrc = cms.InputTag( "hltL1sSingleTau" ),
    L1TauSrc = cms.InputTag( "hltL1SingleNNTau150" ),
    L2Outcomes = cms.InputTag( 'hltL2TauTagNNProducer' ),
    DiscrWP = cms.double( 0.8517 ),
    l1TauPtThreshold = cms.double( 250.0 )
)