import FWCore.ParameterSet.Config as cms

hltIter0PFlowCkfTrackCandidatesMkFit = cms.EDProducer( "MkFitProducer",
    pixelHits = cms.InputTag( "hltIter0PFlowCkfTrackCandidatesMkFitSiPixelHits" ),
    stripHits = cms.InputTag( "hltIter0PFlowCkfTrackCandidatesMkFitSiStripHits" ),
    eventOfHits = cms.InputTag( "hltIter0PFlowCkfTrackCandidatesMkFitEventOfHits" ),
    seeds = cms.InputTag( "hltIter0PFlowCkfTrackCandidatesMkFitSeeds" ),
    clustersToSkip = cms.InputTag( "" ),
    buildingRoutine = cms.string( "cloneEngine" ),
    config = cms.ESInputTag( "","hltESPIter0PFlowTrackCandidatesMkFitConfig" ),
    seedCleaning = cms.bool( True ),
    removeDuplicates = cms.bool( True ),
    backwardFitInCMSSW = cms.bool( False ),
    mkFitSilent = cms.untracked.bool( True ),
    limitConcurrency = cms.untracked.bool( False ),
    minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
)
