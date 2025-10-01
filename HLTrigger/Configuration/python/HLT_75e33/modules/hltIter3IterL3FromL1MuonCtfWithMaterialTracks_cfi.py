import FWCore.ParameterSet.Config as cms

hltIter3IterL3FromL1MuonCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    src = cms.InputTag( "hltIter3IterL3FromL1MuonCkfTrackCandidates" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    AlgorithmName = cms.string( "hltIter3IterL3FromL1Muon" ),
    GeometricInnerState = cms.bool( True ),
    reMatchSplitHits = cms.bool( False ),
    usePropagatorForPCA = cms.bool( False ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter3IterL3FromL1MuonMaskedMeasurementTrackerEvent" ),
    useSimpleMF = cms.bool( True ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    NavigationSchool = cms.string( "" ),
    MeasurementTracker = cms.string( "" )
)
