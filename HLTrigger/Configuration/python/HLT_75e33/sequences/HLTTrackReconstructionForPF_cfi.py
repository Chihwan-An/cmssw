import FWCore.ParameterSet.Config as cms

from ..sequences.HLTDoLocalPixelSequence_cfi import *
from ..sequences.HLTRecopixelvertexingSequence_cfi import *
from ..sequences.HLTDoLocalStripSequence_cfi import *
from ..sequences.HLTIterativeTrackingIter02_cfi import *
from ..modules.hltPFMuonMerging_cfi import *
from ..modules.hltMuonLinks_cfi import *
from ..modules.hltMuons_cfi import *

HLTTrackReconstructionForPF = cms.Sequence( HLTDoLocalPixelSequence + HLTRecopixelvertexingSequence + HLTDoLocalStripSequence + HLTIterativeTrackingIter02 + hltPFMuonMerging + hltMuonLinks + hltMuons )
