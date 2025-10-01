import FWCore.ParameterSet.Config as cms

from ..sequences.HLTIterL3MuonRecopixelvertexingSequence_cfi import *
from ..sequences.HLTIterativeTrackingIteration0ForIterL3Muon_cfi import *
from ..modules.hltL3MuonsIterL3IO_cfi import *

HLTIterL3IOmuonTkCandidateSequence = cms.Sequence( HLTIterL3MuonRecopixelvertexingSequence + HLTIterativeTrackingIteration0ForIterL3Muon + hltL3MuonsIterL3IO )
