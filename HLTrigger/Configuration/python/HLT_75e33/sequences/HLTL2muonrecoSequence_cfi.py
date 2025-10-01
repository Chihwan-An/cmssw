import FWCore.ParameterSet.Config as cms

from ..sequences.HLTL2muonrecoNocandSequence_cfi import *
from ..modules.hltL2MuonCandidates_cfi import *

HLTL2muonrecoSequence = cms.Sequence( HLTL2muonrecoNocandSequence + hltL2MuonCandidates )
