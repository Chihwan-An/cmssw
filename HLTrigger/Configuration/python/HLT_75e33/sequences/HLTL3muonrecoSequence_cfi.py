import FWCore.ParameterSet.Config as cms

from ..sequences.HLTL3muonrecoNocandSequence_cfi import *
from ..modules.hltIterL3MuonCandidates_cfi import *

HLTL3muonrecoSequence = cms.Sequence( HLTL3muonrecoNocandSequence + hltIterL3MuonCandidates )
