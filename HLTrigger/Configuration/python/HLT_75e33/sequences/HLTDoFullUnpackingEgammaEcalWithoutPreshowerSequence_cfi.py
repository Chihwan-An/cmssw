import FWCore.ParameterSet.Config as cms

from ..modules.hltEcalDigisLegacy_cfi import *
from ..modules.hltEcalDigisSoA_cfi import *
from ..modules.hltEcalDigis_cfi import *
from ..modules.hltEcalUncalibRecHitSoA_cfi import *
from ..modules.hltEcalUncalibRecHit_cfi import *
from ..modules.hltEcalDetIdToBeRecovered_cfi import *
from ..modules.hltEcalRecHit_cfi import *

HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence = cms.Sequence(
    hltEcalDigisLegacy + 
    hltEcalDigisSoA + 
    hltEcalDigis +
    hltEcalUncalibRecHitSoA + 
    hltEcalUncalibRecHit + 
    hltEcalDetIdToBeRecovered + 
    hltEcalRecHit )

