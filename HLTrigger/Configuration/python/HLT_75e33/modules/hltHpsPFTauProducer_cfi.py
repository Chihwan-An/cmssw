import FWCore.ParameterSet.Config as cms
from HLTrigger.Configuration.HLT_75e33.modules.hltHpsPFTauProducerSansRefs_cfi import *

hltHpsPFTauProducer = cms.EDProducer("RecoTauPiZeroUnembedder",
    src = cms.InputTag("hltHpsPFTauProducerSansRefs")
)
