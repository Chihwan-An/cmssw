import FWCore.ParameterSet.Config as cms

from ..sequences.HLTRecoJetSequenceAK4UncorrectedPF_cfi import *
from ..modules.hltAK4CaloJetsPFEt5_cfi import *

HLTRecoJetSequenceAK4PrePF = cms.Sequence( HLTRecoJetSequenceAK4UncorrectedPF + hltAK4CaloJetsPFEt5 )
