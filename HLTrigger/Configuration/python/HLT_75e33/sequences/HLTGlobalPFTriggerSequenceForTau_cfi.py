import FWCore.ParameterSet.Config as cms

from ..sequences.HLTL2muonrecoSequence_cfi import *
from ..sequences.HLTL3muonrecoSequence_cfi import *
from ..sequences.HLTRecoJetSequenceAK4PrePF_cfi import *
from ..modules.hltTauJet5_cfi import *
from ..sequences.HLTTrackReconstructionForPF_cfi import *
from ..sequences.HLTParticleFlowSequenceForTaus_cfi import *
from ..modules.hltAK4PFJetsForTaus_cfi import *


HLTGlobalPFTriggerSequenceForTau = cms.Sequence( 
    HLTL2muonrecoSequence +
    HLTL3muonrecoSequence +
    HLTRecoJetSequenceAK4PrePF + 
    hltTauJet5 + 
    HLTTrackReconstructionForPF + 
    HLTParticleFlowSequenceForTaus + 
    hltAK4PFJetsForTaus )