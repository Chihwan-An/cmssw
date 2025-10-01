import FWCore.ParameterSet.Config as cms

#from ..modules.hltPixelTracksSoA_cfi import *
#from ..modules.hltPixelTracks_cfi import *
from ..modules.hltPhase2PixelTracksSoA_cfi import *
from ..modules.hltPhase2PixelTracks_cfi import *

#HLTRecoPixelTracksSequence = cms.Sequence( hltPixelTracksSoA + hltPixelTracks )
HLTRecoPixelTracksSequence = cms.Sequence( hltPhase2PixelTracksSoA + hltPhase2PixelTracks )