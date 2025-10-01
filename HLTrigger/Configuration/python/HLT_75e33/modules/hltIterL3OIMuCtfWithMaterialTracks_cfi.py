import FWCore.ParameterSet.Config as cms

hltIterL3OIMuCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    src = cms.InputTag( "hltIterL3OITrackCandidates" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    AlgorithmName = cms.string( "iter10" ),
    GeometricInnerState = cms.bool( True ),
    reMatchSplitHits = cms.bool( False ),
    usePropagatorForPCA = cms.bool( False ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltMeasurementTrackerEvent" ),
    useSimpleMF = cms.bool( False ),
    SimpleMagneticField = cms.string( "" ),
    Fitter = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    MeasurementTracker = cms.string( "hltESPMeasurementTracker" )
)
