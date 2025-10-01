import FWCore.ParameterSet.Config as cms

hltIterL3MuonPixelTracksTrackingRegions = cms.EDProducer( "MuonTrackingRegionByPtEDProducer",
    DeltaR = cms.double( 0.025 ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    OnDemand = cms.int32( -1 ),
    vertexCollection = cms.InputTag( "notUsed" ),
    MeasurementTrackerName = cms.InputTag( "" ),
    UseVertex = cms.bool( False ),
    Rescale_Dz = cms.double( 4.0 ),
    Pt_fixed = cms.bool( True ),
    Z_fixed = cms.bool( True ),
    Pt_min = cms.double( 0.0 ),
    DeltaZ = cms.double( 24.2 ),
    ptRanges = cms.vdouble( 0.0, 15.0, 20.0, 1.0E64 ),
    deltaEtas = cms.vdouble( 0.2, 0.2, 0.2 ),
    deltaPhis = cms.vdouble( 0.75, 0.45, 0.225 ),
    maxRegions = cms.int32( 5 ),
    precise = cms.bool( True ),
    input = cms.InputTag( "hltL2SelectorForL3IO" )
)
