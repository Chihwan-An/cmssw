import FWCore.ParameterSet.Config as cms

hltDoubletRecoveryPFlowCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    src = cms.InputTag( "hltDoubletRecoveryPFlowCkfTrackCandidates" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    AlgorithmName = cms.string( "hltDoubletRecovery" ),
    GeometricInnerState = cms.bool( True ),
    reMatchSplitHits = cms.bool( False ),
    usePropagatorForPCA = cms.bool( False ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltDoubletRecoveryMaskedMeasurementTrackerEvent" ),
    useSimpleMF = cms.bool( True ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    NavigationSchool = cms.string( "" ),
    MeasurementTracker = cms.string( "" )
)
