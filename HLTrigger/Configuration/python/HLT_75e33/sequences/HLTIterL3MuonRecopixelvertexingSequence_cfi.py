import FWCore.ParameterSet.Config as cms

from ..sequences.HLTRecopixelvertexingSequence_cfi import *
from ..modules.hltIterL3MuonPixelTracksTrackingRegions_cfi import *
from ..modules.hltPixelTracksInRegionL2_cfi import *

HLTIterL3MuonRecopixelvertexingSequence = cms.Sequence( HLTRecopixelvertexingSequence + hltIterL3MuonPixelTracksTrackingRegions + hltPixelTracksInRegionL2 )
