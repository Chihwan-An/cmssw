import FWCore.ParameterSet.Config as cms

hltIter0PFlowCkfTrackCandidates = cms.EDProducer( "MkFitOutputConverter",
    mkFitEventOfHits = cms.InputTag( "hltIter0PFlowCkfTrackCandidatesMkFitEventOfHits" ),
    mkFitPixelHits = cms.InputTag( "hltIter0PFlowCkfTrackCandidatesMkFitSiPixelHits" ),
    mkFitStripHits = cms.InputTag( "hltIter0PFlowCkfTrackCandidatesMkFitSiStripHits" ),
    mkFitSeeds = cms.InputTag( "hltIter0PFlowCkfTrackCandidatesMkFitSeeds" ),
    tracks = cms.InputTag( "hltIter0PFlowCkfTrackCandidatesMkFit" ),
    seeds = cms.InputTag( "hltIter0PFLowPixelSeedsFromPixelTracks" ),
    ttrhBuilder = cms.ESInputTag( "","hltESPTTRHBWithTrackAngle" ),
    propagatorAlong = cms.ESInputTag( "","PropagatorWithMaterialParabolicMf" ),
    propagatorOpposite = cms.ESInputTag( "","PropagatorWithMaterialParabolicMfOpposite" ),
    qualityMaxInvPt = cms.double( 100.0 ),
    qualityMinTheta = cms.double( 0.01 ),
    qualityMaxR = cms.double( 120.0 ),
    qualityMaxZ = cms.double( 280.0 ),
    qualityMaxPosErr = cms.double( 100.0 ),
    qualitySignPt = cms.bool( True ),
    doErrorRescale = cms.bool( True ),
    tfDnnLabel = cms.string( "trackSelectionTf" ),
    candMVASel = cms.bool( False ),
    candWP = cms.double( 0.0 ),
    batchSize = cms.int32( 16 )
)
