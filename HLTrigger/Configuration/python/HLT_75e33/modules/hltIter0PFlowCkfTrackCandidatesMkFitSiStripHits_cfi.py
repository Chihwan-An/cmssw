import FWCore.ParameterSet.Config as cms

hltIter0PFlowCkfTrackCandidatesMkFitSiStripHits = cms.EDProducer( "MkFitSiStripHitConverter",
    rphiHits = cms.InputTag( 'hltSiStripRecHits','rphiRecHit' ),
    stereoHits = cms.InputTag( 'hltSiStripRecHits','stereoRecHit' ),
    clusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    ttrhBuilder = cms.ESInputTag( "","hltESPTTRHBWithTrackAngle" ),
    minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) )
)
