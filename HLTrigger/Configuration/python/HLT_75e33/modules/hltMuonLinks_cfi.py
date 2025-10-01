import FWCore.ParameterSet.Config as cms

hltMuonLinks = cms.EDProducer( "MuonLinksProducerForHLT",
    LinkCollection = cms.InputTag( "hltL3MuonsIterL3Links" ),
    InclusiveTrackerTrackCollection = cms.InputTag( "hltPFMuonMerging" ),
    ptMin = cms.double( 2.5 ),
    pMin = cms.double( 2.5 ),
    shareHitFraction = cms.double( 0.8 )
)
