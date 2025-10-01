import FWCore.ParameterSet.Config as cms

hltIter3IterL3FromL1MuonPixelSeedsFiltered = cms.EDProducer( "MuonHLTSeedMVAClassifier",
    src = cms.InputTag( "hltIter3IterL3FromL1MuonPixelSeeds" ),
    L1Muon = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L2Muon = cms.InputTag( "hltL2MuonCandidates" ),
    rejectAll = cms.bool( False ),
    isFromL1 = cms.bool( True ),
    mvaFileB = cms.FileInPath( "RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter3FromL1_DoubletSeeds_barrel_v1.xml" ),
    mvaFileE = cms.FileInPath( "RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter3FromL1_DoubletSeeds_endcap_v1.xml" ),
    mvaScaleMeanB = cms.vdouble( 0.006826621711798213, 1.340471761359199E-5, 2.5827749083302998E-6, 3.8329754175309627E-4, -0.006327854398161656, 0.0017211841076523692, 0.2760538806332439, -0.010429922003892818 ),
    mvaScaleStdB = cms.vdouble( 0.006225819995879627, 7.4048803387083885E-6, 3.6347963283736586E-6, 0.062213478665703675, 0.828854421408699, 0.3714730344087147, 0.42155116686695293, 0.38566415759730355 ),
    mvaScaleMeanE = cms.vdouble( 0.0013243955281318262, 7.150658575633707E-6, 1.0493070182976E-5, -0.004802713888821372, -0.022186379498012398, 8.335525228198972E-4, 0.2915475574025415, -0.01200308471140653 ),
    mvaScaleStdE = cms.vdouble( 0.0013768261827517547, 7.80116971559064E-6, 8.819635719472336E-5, 0.27824938208607475, 1.798678366076454, 0.16556388679148643, 0.48300543536161705, 0.401204958844809 ),
    doSort = cms.bool( False ),
    nSeedsMaxB = cms.int32( 99999 ),
    nSeedsMaxE = cms.int32( 99999 ),
    etaEdge = cms.double( 1.2 ),
    mvaCutB = cms.double( 0.1 ),
    mvaCutE = cms.double( 0.1 ),
    minL1Qual = cms.int32( 7 ),
    baseScore = cms.double( 0.5 )
)
