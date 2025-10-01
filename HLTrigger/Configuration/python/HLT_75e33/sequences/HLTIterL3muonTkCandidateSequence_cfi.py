import FWCore.ParameterSet.Config as cms

from ..sequences.HLTDoLocalPixelSequence_cfi import *
from ..sequences.HLTDoLocalStripSequence_cfi import *
from ..sequences.HLTIterL3OIAndIOFromL2muonTkCandidateSequence_cfi import *
from ..sequences.HLTIterL3IOmuonFromL1TkCandidateSequence_cfi import *
from ..modules.hltL1MuonsPt0_cfi import *

HLTIterL3muonTkCandidateSequence = cms.Sequence( HLTDoLocalPixelSequence + HLTDoLocalStripSequence + HLTIterL3OIAndIOFromL2muonTkCandidateSequence + hltL1MuonsPt0 + HLTIterL3IOmuonFromL1TkCandidateSequence )
