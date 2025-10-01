import FWCore.ParameterSet.Config as cms

from ..sequences.HLTIterL3muonTkCandidateSequence_cfi import *
from ..modules.hltIter03IterL3FromL1MuonMerged_cfi import *
from ..modules.hltIterL3MuonMerged_cfi import *
from ..modules.hltIterL3MuonAndMuonFromL1Merged_cfi import *
from ..modules.hltIterL3GlbMuon_cfi import *
from ..modules.hltIterL3MuonsNoID_cfi import *
from ..modules.hltIterL3Muons_cfi import *
from ..modules.hltL3MuonsIterL3Links_cfi import *
from ..modules.hltIterL3MuonTracks_cfi import *

HLTL3muonrecoNocandSequence = cms.Sequence( HLTIterL3muonTkCandidateSequence + hltIter03IterL3FromL1MuonMerged + hltIterL3MuonMerged + hltIterL3MuonAndMuonFromL1Merged + hltIterL3GlbMuon + hltIterL3MuonsNoID + hltIterL3Muons + hltL3MuonsIterL3Links + hltIterL3MuonTracks )
