import FWCore.ParameterSet.Config as cms

hltIterL3MuonTracks = cms.EDProducer( "HLTMuonTrackSelector",
    track = cms.InputTag( "hltIterL3MuonAndMuonFromL1Merged" ),
    muon = cms.InputTag( "hltIterL3Muons" ),
    originalMVAVals = cms.InputTag( "none" ),
    copyMVA = cms.bool( False ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False )
)
