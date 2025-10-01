import FWCore.ParameterSet.Config as cms

hltSiPixelRecHits = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    src = cms.InputTag("hltSiPixelClusters")
)
