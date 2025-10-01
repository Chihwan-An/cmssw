import FWCore.ParameterSet.Config as cms

from ..modules.hltEcalPreshowerDigis_cfi import *
from ..modules.hltEcalPreshowerRecHit_cfi import *

HLTPreshowerSequence = cms.Sequence( hltEcalPreshowerDigis + hltEcalPreshowerRecHit )
