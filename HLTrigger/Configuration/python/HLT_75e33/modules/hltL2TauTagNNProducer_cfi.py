import FWCore.ParameterSet.Config as cms

hltL2TauTagNNProducer = cms.EDProducer( "L2TauNNProducerAlpaka",
    debugLevel = cms.int32( 0 ),
    L1Taus = cms.VPSet( 
      #cms.PSet(  L1TauTrigger = cms.InputTag( "hltL1P2GTTau" ),
      #  L1CollectionName = cms.string( "P2GTTau" )
      #),
      cms.PSet(  L1TauTrigger = cms.InputTag( "hltL1SeedForDoublePuppiTau" ),
        L1CollectionName = cms.string( "SeedForDoublePuppiTau" )
      ),
      cms.PSet(  L1TauTrigger = cms.InputTag( "hltPuppiTauTkIsoEle4522L1TkFilter" ),
        L1CollectionName = cms.string( "TkIsoEle4522" )
      ),
      cms.PSet(  L1TauTrigger = cms.InputTag( "hltPuppiTauTkMuon4218L1TkFilter" ),
        L1CollectionName = cms.string( "TkMuon4218" )
      )
    ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    hoInput = cms.InputTag( "hltHoreco" ),
    ebInput = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    eeInput = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    #pataVertices = cms.InputTag( "hltPixelVerticesSoA" ),
    pataVertices = cms.InputTag( "hltPhase2PixelVerticesSoA" ),
    #pataTracks = cms.InputTag( "hltPixelTracksSoA" ),
    pataTracks = cms.InputTag( "hltPhase2PixelTracksSoA" ),
    BeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    maxVtx = cms.uint32( 100 ),
    fractionSumPt2 = cms.double( 0.3 ),
    minSumPt2 = cms.double( 0.0 ),
    track_pt_min = cms.double( 1.0 ),
    track_pt_max = cms.double( 10.0 ),
    track_chi2_max = cms.double( 99999.0 ),
    #graphPath = cms.string( "RecoTauTag/TrainingFiles/data/L2TauNNTag/L2TauTag_Run3v1.pb" ),
    #normalizationDict = cms.string( "RecoTauTag/TrainingFiles/data/L2TauNNTag/NormalizationDict.json" )
)
