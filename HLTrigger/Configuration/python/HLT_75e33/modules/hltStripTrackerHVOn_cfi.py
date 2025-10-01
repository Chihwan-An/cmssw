import FWCore.ParameterSet.Config as cms

hltStripTrackerHVOn = cms.EDFilter( "DetectorStateFilter",
    DebugOn = cms.untracked.bool( False ),
    DetectorType = cms.untracked.string( "sistrip" ),
    acceptedCombinations = cms.untracked.vstring(  ),
    DcsStatusLabel = cms.untracked.InputTag( "" ),
    DCSRecordLabel = cms.untracked.InputTag( "hltOnlineMetaDataDigis" )
)