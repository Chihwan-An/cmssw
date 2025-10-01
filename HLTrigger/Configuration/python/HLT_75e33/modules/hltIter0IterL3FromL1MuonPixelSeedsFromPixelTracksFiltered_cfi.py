import FWCore.ParameterSet.Config as cms

hltIter0IterL3FromL1MuonPixelSeedsFromPixelTracksFiltered = cms.EDProducer( "MuonHLTSeedMVAClassifier",
    src = cms.InputTag( "hltIter0IterL3FromL1MuonPixelSeedsFromPixelTracks" ),
    L1Muon = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L2Muon = cms.InputTag( "hltL2MuonCandidates" ),
    rejectAll = cms.bool( False ),
    isFromL1 = cms.bool( True ),
    mvaFileB = cms.FileInPath( "RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter0FromL1_PatatrackSeeds_barrel_v3.xml" ),
    mvaFileE = cms.FileInPath( "RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter0FromL1_PatatrackSeeds_endcap_v3.xml" ),
    mvaScaleMeanB = cms.vdouble( 3.999966523561405E-4, 1.5340202670472034E-5, 2.6710290157638425E-5, 5.978116313043455E-4, 0.0049135275917734636, 3.4305653488182246E-5, 0.24525118734715307, -0.0024635178849904426 ),
    mvaScaleStdB = cms.vdouble( 7.666933596884494E-4, 0.015685297920984408, 0.026294325262867256, 0.07665283880432934, 0.834879854164998, 0.5397258722194461, 0.2807075832224741, 0.32820882609116625 ),
    mvaScaleMeanE = cms.vdouble( 3.017047347441654E-4, 9.077959353128816E-5, 2.7101609045025927E-4, 0.004557390407735609, -0.020781128525626812, 9.286198943080588E-4, 0.26674085200387376, -0.002971698676536822 ),
    mvaScaleStdE = cms.vdouble( 8.125341035878315E-4, 0.19268436761240013, 0.579019516987623, 0.3222327708969556, 1.0567488273501275, 0.2648980106841699, 0.30889713721141826, 0.3593729790466801 ),
    doSort = cms.bool( False ),
    nSeedsMaxB = cms.int32( 99999 ),
    nSeedsMaxE = cms.int32( 99999 ),
    etaEdge = cms.double( 1.2 ),
    mvaCutB = cms.double( 0.04 ),
    mvaCutE = cms.double( 0.04 ),
    minL1Qual = cms.int32( 7 ),
    baseScore = cms.double( 0.5 )
)
