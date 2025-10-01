import FWCore.ParameterSet.Config as cms

hltSiStripRecHits = cms.EDProducer( "SiStripRecHitConverter",
    ClusterProducer = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    rphiRecHits = cms.string( "rphiRecHit" ),
    stereoRecHits = cms.string( "stereoRecHit" ),
    matchedRecHits = cms.string( "matchedRecHit" ),
    useSiStripQuality = cms.bool( False ),
    MaskBadAPVFibers = cms.bool( False ),
    doMatching = cms.bool( False ),
    StripCPE = cms.ESInputTag( "hltESPStripCPEfromTrackAngle","hltESPStripCPEfromTrackAngle" ),
    Matcher = cms.ESInputTag( "SiStripRecHitMatcherESProducer","StandardMatcher" ),
    siStripQualityLabel = cms.ESInputTag( "","" )
)
