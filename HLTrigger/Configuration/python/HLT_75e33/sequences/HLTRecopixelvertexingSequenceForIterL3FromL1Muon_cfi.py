import FWCore.ParameterSet.Config as cms

from ..sequences.HLTRecopixelvertexingSequence_cfi import *
from ..modules.hltIterL3FromL1MuonPixelTracksTrackingRegions_cfi import *
from ..modules.hltPixelTracksInRegionL1_cfi import *

HLTRecopixelvertexingSequenceForIterL3FromL1Muon = cms.Sequence( HLTRecopixelvertexingSequence + hltIterL3FromL1MuonPixelTracksTrackingRegions + hltPixelTracksInRegionL1 )
