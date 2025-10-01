import FWCore.ParameterSet.Config as cms

hltNNPuppiTauPuppiMet_55_190L1TkFilter = cms.EDFilter("PathStatusFilter",
    logicalExpression = cms.string('pNNPuppiTauPuppiMet_55_190')
)
