import FWCore.ParameterSet.Config as cms


#from ..sequences.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence_cfi import *
from ..sequences.HLTDoFullUnpackingEgammaEcalSequence_cfi import *
from ..sequences.HLTDoLocalHcalSequence_cfi import *
#from ..modules.hltTowerMakerForAll_cfi import *
from ..modules.hltPhase2TowerMakerForAll_cfi import *


HLTDoCaloSequence = cms.Sequence(
    #HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence +
    HLTDoFullUnpackingEgammaEcalSequence +
    HLTDoLocalHcalSequence +
    #hltTowerMakerForAll )
    hltPhase2TowerMakerForAll )