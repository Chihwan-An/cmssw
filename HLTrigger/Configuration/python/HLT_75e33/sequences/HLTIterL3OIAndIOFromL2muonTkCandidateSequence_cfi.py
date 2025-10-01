import FWCore.ParameterSet.Config as cms

from ..sequences.HLTIterL3OImuonTkCandidateSequence_cfi import *
from ..sequences.HLTIterL3IOmuonTkCandidateSequence_cfi import *
from ..modules.hltIterL3OIL3MuonsLinksCombination_cfi import *
from ..modules.hltIterL3OIL3Muons_cfi import *
from ..modules.hltIterL3OIL3MuonCandidates_cfi import *
from ..modules.hltL2SelectorForL3IO_cfi import *
from ..modules.hltIterL3MuonsFromL2LinksCombination_cfi import *

HLTIterL3OIAndIOFromL2muonTkCandidateSequence = cms.Sequence( HLTIterL3OImuonTkCandidateSequence + hltIterL3OIL3MuonsLinksCombination + hltIterL3OIL3Muons + hltIterL3OIL3MuonCandidates + hltL2SelectorForL3IO + HLTIterL3IOmuonTkCandidateSequence + hltIterL3MuonsFromL2LinksCombination )
