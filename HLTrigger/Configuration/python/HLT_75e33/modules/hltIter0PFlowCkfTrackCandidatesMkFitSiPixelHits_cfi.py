import FWCore.ParameterSet.Config as cms

hltIter0PFlowCkfTrackCandidatesMkFitSiPixelHits = cms.EDProducer( "MkFitSiPixelHitConverter",
    hits = cms.InputTag( "hltSiPixelRecHits" ),
    clusters = cms.InputTag( "hltSiPixelClusters" ),
    ttrhBuilder = cms.ESInputTag( "","hltESPTTRHBWithTrackAngle" )
)
