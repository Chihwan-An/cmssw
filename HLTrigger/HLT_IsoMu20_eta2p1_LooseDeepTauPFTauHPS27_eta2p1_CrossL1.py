
import FWCore.ParameterSet.Config as cms

from HLTrigger.Configuration.HLT_75e33.modules.hltPuppiTauTkMuon4218L1TkFilter_cfi import *
from HLTrigger.Configuration.HLT_75e33.sequences.HLTRawToDigiSequence_cfi import *
from HLTrigger.Configuration.HLT_75e33.sequences.HLTHgcalLocalRecoSequence_cfi import *
from HLTrigger.Configuration.HLT_75e33.sequences.HLTLocalrecoSequence_cfi import *
from HLTrigger.Configuration.HLT_75e33.sequences.HLTTrackingSequence_cfi import *
from HLTrigger.Configuration.HLT_75e33.sequences.HLTMuonsSequence_cfi import *
from HLTrigger.Configuration.HLT_75e33.sequences.HLTParticleFlowSequence_cfi import *
from HLTrigger.Configuration.HLT_75e33.modules.hltParticleFlowRecHitECALUnseeded_cfi import *
from HLTrigger.Configuration.HLT_75e33.modules.hltParticleFlowClusterECALUncorrectedUnseeded_cfi import *
from HLTrigger.Configuration.HLT_75e33.modules.hltParticleFlowClusterECALUnseeded_cfi import *
from HLTrigger.Configuration.HLT_75e33.modules.hltFixedGridRhoFastjetAllCaloForEGamma_cfi import *
from HLTrigger.Configuration.HLT_75e33.modules.hltPhase2L3MuonCandidates_cfi import *
from HLTrigger.Configuration.HLT_75e33.modules.hltPhase2L3MuonsEcalIsodR0p3dRVeto0p000_cfi import *
from HLTrigger.Configuration.HLT_75e33.modules.hltPhase2L3MuonsHcalIsodR0p3dRVeto0p000_cfi import *
from HLTrigger.Configuration.HLT_75e33.modules.hltPhase2L3MuonsHgcalLCIsodR0p2dRVetoEM0p00dRVetoHad0p02minEEM0p00minEHad0p00_cfi import *
from HLTrigger.Configuration.HLT_75e33.modules.hltL3fL1TkSingleMu18Filtered20_cfi import *
from HLTrigger.Configuration.HLT_75e33.modules.hltL3crIsoL1TkSingleMu22EcalIso0p41_cfi import *
from HLTrigger.Configuration.HLT_75e33.modules.hltL3crIsoL1TkSingleMu22HcalIso0p40_cfi import *
from HLTrigger.Configuration.HLT_75e33.modules.hltL3crIsoL1TkSingleMu22HgcalIso4p70_cfi import *
from HLTrigger.Configuration.HLT_75e33.sequences.HLTPhase2L3MuonGeneralTracksSequence_cfi import *
from HLTrigger.Configuration.HLT_75e33.modules.hltPhase2L3MuonsTrkIsoRegionalNewdR0p3dRVeto0p005dz0p25dr0p20ChisqInfPtMin0p0Cut0p07_cfi import *
from HLTrigger.Configuration.HLT_75e33.modules.hltL3crIsoL1TkSingleMu22TrkIsoRegionalNewFiltered0p07EcalHcalHgcalTrk_cfi import *
from HLTrigger.Configuration.HLT_75e33.sequences.HLTAK4PFJetsReconstruction_cfi import *
from HLTrigger.Configuration.HLT_75e33.modules.hltAK4PFJetsForTaus_cfi import *
from HLTrigger.Configuration.HLT_75e33.sequences.HLTPFTauHPS_cfi import *
from HLTrigger.Configuration.HLT_75e33.sequences.HLTHPSDeepTauPFTauSequence_cfi import *
from HLTrigger.Configuration.HLT_75e33.modules.hltHpsSelectedPFTauLooseTauWPDeepTau_cfi import *
from HLTrigger.Configuration.HLT_75e33.modules.hltHpsPFTau27LooseTauWPDeepTau_cfi import *
from HLTrigger.Configuration.HLT_75e33.sequences.HLTEndSequence_cfi import *

HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1_Sequence = cms.Sequence(
    HLTRawToDigiSequence +
    HLTLocalrecoSequence +
    HLTTrackingSequence +
    HLTMuonsSequence +
    hltPhase2L3MuonCandidates +
    hltL3fL1TkSingleMu18Filtered20 +
    HLTPhase2L3MuonGeneralTracksSequence +
    hltPhase2L3MuonsEcalIsodR0p3dRVeto0p000 +
    hltPhase2L3MuonsHcalIsodR0p3dRVeto0p000 +
    hltPhase2L3MuonsHgcalLCIsodR0p2dRVetoEM0p00dRVetoHad0p02minEEM0p00minEHad0p00 +
    hltPhase2L3MuonsTrkIsoRegionalNewdR0p3dRVeto0p005dz0p25dr0p20ChisqInfPtMin0p0Cut0p07 +
    hltL3crIsoL1TkSingleMu22EcalIso0p41 +
    hltL3crIsoL1TkSingleMu22HcalIso0p40 +
    hltL3crIsoL1TkSingleMu22HgcalIso4p70 +
    hltL3crIsoL1TkSingleMu22TrkIsoRegionalNewFiltered0p07EcalHcalHgcalTrk +
    HLTParticleFlowSequence +
    HLTAK4PFJetsReconstruction +
    hltAK4PFJetsForTaus +
    HLTPFTauHPS +
    HLTHPSDeepTauPFTauSequence +
    hltHpsSelectedPFTauLooseTauWPDeepTau +
    hltHpsPFTau27LooseTauWPDeepTau +
    hltPuppiTauTkMuon4218L1TkFilter +
    HLTEndSequence
)

HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1 = cms.Path(HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1_Sequence)
