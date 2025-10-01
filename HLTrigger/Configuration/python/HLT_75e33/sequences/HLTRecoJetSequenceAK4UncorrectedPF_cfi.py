import FWCore.ParameterSet.Config as cms

from ..sequences.HLTDoCaloSequencePF_cfi import *
from ..modules.hltAK4CaloJetsPF_cfi import *

HLTRecoJetSequenceAK4UncorrectedPF = cms.Sequence( HLTDoCaloSequencePF + hltAK4CaloJetsPF )
