import FWCore.ParameterSet.Config as cms

from ..sequences.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence_cfi import *
from ..sequences.HLTDoLocalHcalSequence_cfi import *
from ..modules.hltTowerMakerForAll_cfi import *

HLTDoCaloSequencePF = cms.Sequence( HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence + HLTDoLocalHcalSequence + hltTowerMakerForAll )
