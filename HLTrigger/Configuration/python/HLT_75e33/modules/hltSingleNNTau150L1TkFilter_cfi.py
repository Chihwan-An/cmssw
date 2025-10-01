import FWCore.ParameterSet.Config as cms

hltSingleNNTau150L1TkFilter = cms.EDFilter("PathStatusFilter",
    logicalExpression = cms.string('l1tNNTauProducerPuppi')
)
