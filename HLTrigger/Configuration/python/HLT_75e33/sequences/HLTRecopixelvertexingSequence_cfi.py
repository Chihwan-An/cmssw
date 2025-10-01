import FWCore.ParameterSet.Config as cms

from ..sequences.HLTRecoPixelTracksSequence_cfi import *
#from ..modules.hltPixelVerticesSoA_cfi import *
#from ..modules.hltPixelVertices_cfi import *
#from ..modules.hltTrimmedPixelVertices_cfi import *

from ..modules.hltPhase2PixelVertices_cfi import *
from ..modules.hltPhase2TrimmedPixelVertices_cfi import *


#HLTRecopixelvertexingSequence = cms.Sequence( HLTRecoPixelTracksSequence + hltPixelVerticesSoA + hltPixelVertices + hltTrimmedPixelVertices )
HLTRecopixelvertexingSequence = cms.Sequence( HLTRecoPixelTracksSequence  + hltPhase2PixelVertices + hltPhase2TrimmedPixelVertices )