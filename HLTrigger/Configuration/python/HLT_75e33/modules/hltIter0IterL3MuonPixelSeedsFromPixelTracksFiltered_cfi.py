import FWCore.ParameterSet.Config as cms

hltIter0IterL3MuonPixelSeedsFromPixelTracksFiltered = cms.EDProducer( "MuonHLTSeedMVAClassifier",
    src = cms.InputTag( "hltIter0IterL3MuonPixelSeedsFromPixelTracks" ),
    L1Muon = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L2Muon = cms.InputTag( "hltL2MuonCandidates" ),
    rejectAll = cms.bool( False ),
    isFromL1 = cms.bool( False ),
    mvaFileB = cms.FileInPath( "RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter0_PatatrackSeeds_barrel_v3.xml" ),
    mvaFileE = cms.FileInPath( "RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter0_PatatrackSeeds_endcap_v3.xml" ),
    mvaScaleMeanB = cms.vdouble( 4.332629261558539E-4, 4.689795312031938E-6, 7.644844964566431E-6, 6.580623848546099E-4, 0.00523266117445817, 5.6968993532947E-4, 0.20322471101222087, -0.005575351463397025, 0.18247595248098955, 1.5342398341020196E-4 ),
    mvaScaleStdB = cms.vdouble( 7.444819891335438E-4, 0.0014335177986615237, 0.003503839482232683, 0.07764362324530726, 0.8223406268068466, 0.6392468338330071, 0.2405783807668161, 0.2904161358810494, 0.21887441827342669, 0.27045195352036544 ),
    mvaScaleMeanE = cms.vdouble( 3.120747098810717E-4, 4.5298701434656295E-6, 1.2002076996572005E-5, 0.007900535887258366, -0.022166389143849694, 7.12338927507459E-4, 0.22819667672872926, -0.0039375694144792705, 0.19304371973554835, -1.2936058928324214E-5 ),
    mvaScaleStdE = cms.vdouble( 6.302274350028021E-4, 0.0013138279991871378, 0.004880335178644773, 0.32509543981045624, 0.9449952711981982, 0.279802349646327, 0.3193063648341999, 0.3334815828876066, 0.22528017441813106, 0.2822750719936266 ),
    doSort = cms.bool( False ),
    nSeedsMaxB = cms.int32( 99999 ),
    nSeedsMaxE = cms.int32( 99999 ),
    etaEdge = cms.double( 1.2 ),
    mvaCutB = cms.double( 0.04 ),
    mvaCutE = cms.double( 0.04 ),
    minL1Qual = cms.int32( 7 ),
    baseScore = cms.double( 0.5 )
)
