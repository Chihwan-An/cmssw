import FWCore.ParameterSet.Config as cms

hltIter0PFlowCkfTrackCandidatesMkFitSeeds = cms.EDProducer( "MkFitSeedConverter",
    seeds = cms.InputTag( "hltIter0PFLowPixelSeedsFromPixelTracks" ),
    ttrhBuilder = cms.ESInputTag( "","hltESPTTRHBWithTrackAngle" ),
    maxNSeeds = cms.uint32( 500000 )
)
