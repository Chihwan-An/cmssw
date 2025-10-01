# HLT Sequence Components Documentation

## HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1 Sequence

### HLTBeginSequence
**File:** `/data6/Users/achihwan/CMSSW_15_1_0_pre4/src/HLTrigger/Configuration/python/HLT_75e33/sequences/HLTBeginSequence_cfi.py`

**Definition:**
```python
HLTBeginSequence = cms.Sequence(hltTriggerType+HLTL1Sequence+HLTBeamSpotSequence)
```

**Components:**
- `hltTriggerType` - Trigger type module
- `HLTL1Sequence` - L1 trigger sequence  
- `HLTBeamSpotSequence` - Beam spot sequence

---

### hltPuppiTauTkMuon4218L1TkFilter
**Type:** PathStatusFilter
**Function:** Filter for pPuppiTauTkMuon42_18 logic

---

### HLTRawToDigiSequence
**File:** `/data6/Users/achihwan/CMSSW_15_1_0_pre4/src/HLTrigger/Configuration/python/HLT_75e33/sequences/HLTRawToDigiSequence_cfi.py`

**Definition:**
```python
HLTRawToDigiSequence = cms.Sequence(hltHgcalDigis+HLTEcalDigisSequence+hltHcalDigis+hltMuonCSCDigis+hltMuonDTDigis+hltMuonGEMDigis)
```

**Components:**
- `hltHgcalDigis` - HGCAL digitization
- `HLTEcalDigisSequence` - ECAL digis sequence
- `hltHcalDigis` - HCAL digitization
- `hltMuonCSCDigis` - CSC muon digitization
- `hltMuonDTDigis` - DT muon digitization
- `hltMuonGEMDigis` - GEM muon digitization

---

### HLTHgcalLocalRecoSequence
**File:** `/data6/Users/achihwan/CMSSW_15_1_0_pre4/src/HLTrigger/Configuration/python/HLT_75e33/sequences/HLTHgcalLocalRecoSequence_cfi.py`

**Definition:**
```python
HLTHgcalLocalRecoSequence = cms.Sequence(
    hltHGCalUncalibRecHit+
    hltHGCalRecHit+
    hltHgcalLayerClustersEE+
    hltHgcalLayerClustersHSci+
    hltHgcalLayerClustersHSi+
    hltHgcalMergeLayerClusters)
```

**Components:**
- HGCAL uncalibrated rechits
- HGCAL calibrated rechits  
- Layer clusters for EE, HSci, HSi
- Merged layer clusters
- Alternative heterogeneous version available with SoA producers

---

### HLTLocalrecoSequence
**File:** `/data6/Users/achihwan/CMSSW_15_1_0_pre4/src/HLTrigger/Configuration/python/HLT_75e33/sequences/HLTLocalrecoSequence_cfi.py`

**Definition:**
```python
HLTLocalrecoSequence = cms.Sequence(bunchSpacingProducer+HLTCalolocalrecoSequence)
```

**Components:**
- `bunchSpacingProducer` - Bunch spacing information
- `HLTCalolocalrecoSequence` - Calorimeter local reconstruction

---

### HLTTrackingSequence
**File:** `/data6/Users/achihwan/CMSSW_15_1_0_pre4/src/HLTrigger/Configuration/python/HLT_75e33/sequences/HLTTrackingSequence_cfi.py`

**Definition:**
```python
HLTTrackingSequence = cms.Sequence(HLTItLocalRecoSequence+
                                   HLTOtLocalRecoSequence+
                                   hltTrackerClusterCheck+
                                   HLTPhase2PixelTracksSequence+
                                   hltPhase2PixelVertices+
                                   HLTInitialStepSequence+
                                   HLTHighPtTripletStepSequence+
                                   hltGeneralTracks)
```

**Components:**
- IT (Inner Tracker) and OT (Outer Tracker) local reconstruction
- Tracker cluster check
- Phase 2 pixel tracks and vertices
- Initial step and high-pT triplet step sequences
- General tracks reconstruction

---

### HLTMuonsSequence
**File:** `/data6/Users/achihwan/CMSSW_15_1_0_pre4/src/HLTrigger/Configuration/python/HLT_75e33/sequences/HLTMuonsSequence_cfi.py`

**Definition:**
```python
HLTMuonsSequence = cms.Sequence(
    HLTL2MuonsFromL1TkSequence
    + HLTPhase2L3FromL1TkSequence
    + HLTIter0Phase2L3FromL1TkSequence
    + HLTIter2Phase2L3FromL1TkSequence
    + hltPhase2L3MuonFilter
    + HLTPhase2L3OISequence
    + HLTPhase2L3MuonsSequence
)
```

**Components:**
- L2 muons from L1Tk sequence
- Phase 2 L3 sequences with different iterations
- Outside-in (OI) sequence
- L3 muon filter and final muons sequence

---

### HLTParticleFlowSequence
**File:** `/data6/Users/achihwan/CMSSW_15_1_0_pre4/src/HLTrigger/Configuration/python/HLT_75e33/sequences/HLTParticleFlowSequence_cfi.py`

**Definition:**
```python
HLTParticleFlowSequence = cms.Sequence(HLTParticleFlowClusterSequence+HLTIterTICLSequence+HLTVertexRecoSequence+HLTParticleFlowSuperClusteringSequence+HLTCaloTowersRecSequence+HLTParticleFlowRecoSequence)
```

**Components:**
- Particle flow clustering
- Iterative TICL sequence
- Vertex reconstruction
- Super clustering and calo towers
- Final PF reconstruction

---

### hltParticleFlowRecHitECALUnseeded
**Type:** PFRecHitProducer
**Function:** ECAL rechits for particle flow

---

### hltParticleFlowClusterECALUncorrectedUnseeded
**Type:** PFClusterProducer
**Function:** ECAL clustering for particle flow

---

### hltParticleFlowClusterECALUnseeded
**Type:** CorrectedECALPFClusterProducer
**Function:** Energy-corrected ECAL PF clusters

---

### hltFixedGridRhoFastjetAllCaloForEGamma
**Type:** FixedGridRhoProducer
**Function:** Energy density calculation for EGamma objects

---

### hltPhase2L3MuonCandidates
**Type:** L3MuonCandidateProducer
**Function:** Creates L3 muon candidates from muons

---

### hltPhase2L3MuonsEcalIsodR0p3dRVeto0p000
**Type:** ECAL PF cluster isolation producer
**Function:** ECAL isolation with dR=0.3, dRVeto=0.000

---

### hltPhase2L3MuonsHcalIsodR0p3dRVeto0p000
**Type:** HCAL PF cluster isolation producer
**Function:** HCAL isolation with dR=0.3, dRVeto=0.000

---

### hltPhase2L3MuonsHgcalLCIsodR0p2dRVetoEM0p00dRVetoHad0p02minEEM0p00minEHad0p00
**Type:** HGCAL layer cluster isolation producer
**Function:** HGCAL isolation with dR=0.2, EM veto=0.00, Had veto=0.02, min energy thresholds

---

### hltL3fL1TkSingleMu18Filtered20
**Type:** HLTMuonTrkL1TkMuFilter
**Function:** Filter for muons with pT > 20 GeV

---

### hltL3crIsoL1TkSingleMu22EcalIso0p41
**Type:** ECAL isolation filter
**Function:** ECAL isolation < 0.41

---

### hltL3crIsoL1TkSingleMu22HcalIso0p40
**Type:** HCAL isolation filter
**Function:** HCAL isolation < 0.40

---

### hltL3crIsoL1TkSingleMu22HgcalIso4p70
**Type:** HGCAL isolation filter
**Function:** HGCAL isolation < 4.70

---

### HLTPhase2L3MuonGeneralTracksSequence
**File:** `/data6/Users/achihwan/CMSSW_15_1_0_pre4/src/HLTrigger/Configuration/python/HLT_75e33/sequences/HLTPhase2L3MuonGeneralTracksSequence_cfi.py`

**Definition:**
```python
HLTPhase2L3MuonGeneralTracksSequence = cms.Sequence(
    hltTrackerClusterCheck
    +hltPhase2L3MuonPixelTracksAndHighPtTripletTrackingRegions
    +hltPhase2L3MuonPixelTracksSeedLayers
    +hltPhase2L3MuonPixelTracksHitDoublets
    +hltPhase2L3MuonPixelTracksHitQuadruplets
    +hltPhase2L3MuonPixelTracks
    +hltPhase2L3MuonPixelVertices
    +hltPhase2L3MuonInitialStepSeeds
    +hltPhase2L3MuonInitialStepTrackCandidates
    +hltPhase2L3MuonInitialStepTracks
    +hltPhase2L3MuonInitialStepTrackCutClassifier
    +hltPhase2L3MuonInitialStepTracksSelectionHighPurity
    +hltPhase2L3MuonHighPtTripletStepClusters
    +hltPhase2L3MuonHighPtTripletStepSeedLayers
    +hltPhase2L3MuonHighPtTripletStepHitDoublets
    +hltPhase2L3MuonHighPtTripletStepHitTriplets
    +hltPhase2L3MuonHighPtTripletStepSeeds
    +hltPhase2L3MuonHighPtTripletStepTrackCandidates
    +hltPhase2L3MuonHighPtTripletStepTracks
    +hltPhase2L3MuonHighPtTripletStepTrackCutClassifier
    +hltPhase2L3MuonHighPtTripletStepTracksSelectionHighPurity
    +hltPhase2L3MuonGeneralTracks
    )
```

**Components:**
- Complete muon-specific tracking sequence with pixel tracks, initial step, and high-pT triplet step reconstruction

---

### hltPhase2L3MuonsTrkIsoRegionalNewdR0p3dRVeto0p005dz0p25dr0p20ChisqInfPtMin0p0Cut0p07
**Type:** Track isolation producer
**Function:** Track isolation with dR=0.3, dRVeto=0.005, dz=0.25, dr=0.20, cut=0.07

---

### hltL3crIsoL1TkSingleMu22TrkIsoRegionalNewFiltered0p07EcalHcalHgcalTrk
**Type:** Combined isolation filter
**Function:** Combined ECAL+HCAL+HGCAL+Track isolation filter

---

### HLTAK4PFJetsReconstruction
**File:** `/data6/Users/achihwan/CMSSW_15_1_0_pre4/src/HLTrigger/Configuration/python/HLT_75e33/sequences/HLTAK4PFJetsReconstruction_cfi.py`

**Definition:**
```python
HLTAK4PFJetsReconstruction = cms.Sequence(hltAK4PFJets+hltAK4PFJetCorrectorL1+hltAK4PFJetCorrectorL2+hltAK4PFJetCorrectorL3+hltAK4PFJetCorrector+hltAK4PFJetsCorrected)
```

**Components:**
- AK4 PF jet reconstruction
- L1, L2, L3 jet energy corrections
- Final corrected jets

---

### hltAK4PFJetsForTaus
**Type:** FastjetJetProducer
**Function:** AK4 PF jets for tau reconstruction

---

### HLTPFTauHPS
**File:** `/data6/Users/achihwan/CMSSW_15_1_0_pre4/src/HLTrigger/Configuration/python/HLT_75e33/sequences/HLTPFTauHPS_cfi.py`

**Definition:**
```python
HLTPFTauHPS = cms.Sequence(hltTauPFJets08Region+hltHpsTauPFJetsRecoTauChargedHadronsWithNeutrals+hltPFTauPiZeros+hltHpsCombinatoricRecoTaus+hltHpsSelectionDiscriminator+hltHpsPFTauProducerSansRefs+hltHpsPFTauProducer+hltHpsPFTauDiscriminationByDecayModeFindingNewDMs+hltHpsPFTauTrackFindingDiscriminator+hltHpsSelectedPFTausTrackFinding+hltHpsPFTauTrack)
```

**Components:**
- Tau PF jets in region
- Charged hadron and neutral pion reconstruction
- Combinatoric tau reconstruction
- HPS discriminators and tau producers

---

### HLTHPSDeepTauPFTauSequence
**File:** `/data6/Users/achihwan/CMSSW_15_1_0_pre4/src/HLTrigger/Configuration/python/HLT_75e33/sequences/HLTHPSDeepTauPFTauSequence_cfi.py`

**Definition:**
```python
HLTHPSDeepTauPFTauSequence = cms.Sequence(hltHpsPFTauDiscriminationByDecayModeFindingNewDMs+hltHpsPFTauPrimaryVertexProducerForDeepTau+hltHpsPFTauSecondaryVertexProducerForDeepTau+hltHpsPFTauTransverseImpactParametersForDeepTau+hltFixedGridRhoFastjetAll+hltHpsPFTauBasicDiscriminatorsForDeepTau+hltHpsPFTauBasicDiscriminatorsdR03ForDeepTau+hltHpsPFTauDeepTauProducer)
```

**Components:**
- Decay mode finding
- Primary and secondary vertex producers
- Impact parameters
- Deep tau discriminators and producer

---

### hltHpsSelectedPFTauLooseTauWPDeepTau
**Type:** PFTauSelector
**Function:** PF tau selector with DeepTau VSjet discriminator

---

### hltHpsPFTau27LooseTauWPDeepTau
**Type:** HLT1PFTau filter
**Function:** Tau filter with pT > 27 GeV and DeepTau loose working point

---

### HLTEndSequence
**File:** `/data6/Users/achihwan/CMSSW_15_1_0_pre4/src/HLTrigger/Configuration/python/HLT_75e33/sequences/HLTEndSequence_cfi.py`

**Definition:**
```python
HLTEndSequence = cms.Sequence(hltBoolEnd)
```

**Components:**
- `hltBoolEnd` - Boolean end module

---

## Summary

All HLT sequence components implement Phase 2 upgrade features including:
- HGCAL integration for forward calorimetry
- Advanced muon isolation using multiple calorimeter systems (ECAL, HCAL, HGCAL)
- DeepTau-based tau identification for high-luminosity LHC environment
- Hierarchical reconstruction from raw data to physics objects

The sequence flows from raw data processing through local reconstruction, tracking, particle flow, object reconstruction, and final selection filters.