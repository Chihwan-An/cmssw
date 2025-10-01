import FWCore.ParameterSet.Config as cms

hltIter0PFlowCkfTrackCandidatesMkFitEventOfHits = cms.EDProducer( "MkFitEventOfHitsProducer",
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    pixelHits = cms.InputTag( "hltIter0PFlowCkfTrackCandidatesMkFitSiPixelHits" ),
    stripHits = cms.InputTag( "hltIter0PFlowCkfTrackCandidatesMkFitSiStripHits" ),
    usePixelQualityDB = cms.bool( True ),
    useStripStripQualityDB = cms.bool( True )
)
