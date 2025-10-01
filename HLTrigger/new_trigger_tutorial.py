
# This is a tutorial script for creating a new HLT path.
# It is intended to be run with cmsRun.
# The script defines a new trigger path called HLT_MyNewMuon_v1
# that selects events with a muon with pT > 20 GeV.

import FWCore.ParameterSet.Config as cms

# Create a new CMS process
process = cms.Process('HLT')

# Import the HLT configuration from the GRun menu
# This provides all the necessary sequences and modules for HLT reconstruction
process.load('HLTrigger.Configuration.HLT_GRun_cff')

# Define a new filter instance using HLTMuonL3SimplePreFilter
# This filter will select muons with pT > 20 GeV.
# The parameters are copied from a similar existing filter, as suggested in the tutorial.
process.hltL3fL1sSingleMu22L1f0L2f10L3Filtered20 = cms.EDFilter("HLTMuonL3SimplePreFilter",
    MinPt = cms.double(20.0),
    MinN = cms.int32(1),
    MaxEta = cms.double(2.5),
    MinEta = cms.double(-1.0),
    MaxDr = cms.double(2.0),
    MinDr = cms.double(-1.0),
    MaxDz = cms.double(9999.0),
    MinDz = cms.double(-1.0),
    ChargeOpt = cms.int32(0),
    CandTag = cms.InputTag("hltL3MuonCandidates"),
    PreviousCandTag = cms.InputTag("hltL2fL1sSingleMu22L1f0L2Filtered10Q"),
    saveTags = cms.bool(True)
)

# Define the new HLT path
# The path starts with the HLTBeginSequence, which is standard for all HLT paths.
# It is followed by the L1 seed, which in this case is hltL1sSingleMu22.
# Then, the standard muon reconstruction sequence is included.
# Finally, our new filter is added at the end of the path.
process.HLT_MyNewMuon_v1 = cms.Path(
    process.HLTBeginSequence +
    process.hltL1sSingleMu22 +
    process.hltPreIsoMu24 +
    process.hltL1fL1sMu22L1Filtered0 +
    process.HLTL2muonrecoSequence +
    cms.ignore(process.hltL2fL1sSingleMu22L1f0L2Filtered10Q) +
    process.HLTL3muonrecoSequence +
    cms.ignore(process.hltL1fForIterL3L1fL1sMu22L1Filtered0) +
    process.hltL3fL1sSingleMu22L1f0L2f10L3Filtered20 + # Our new filter
    process.HLTEndSequence
)

# Add the new path to the schedule
# The schedule determines which paths are executed.
process.schedule = cms.Schedule(process.HLT_MyNewMuon_v1)

# Minimal source and maxEvents for a runnable configuration
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        # --- BEGIN USER INPUT ---
        # You must add a ROOT file as input. For example:
        '/store/relval/CMSSW_15_1_0_pre4/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/150X_mcRun3_2021_realistic_v1-v1/00000/00a7f79b-8375-4743-9520-5985a4b5e595.root'
        # --- END USER INPUT ---
    )
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
