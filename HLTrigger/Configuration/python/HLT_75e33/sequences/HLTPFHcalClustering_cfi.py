import FWCore.ParameterSet.Config as cms

from ..modules.hltParticleFlowRecHitHBHESoA_cfi import *
from ..modules.hltParticleFlowRecHitHBHE_cfi import *
from ..modules.hltParticleFlowClusterHBHESoA_cfi import *
from ..modules.hltParticleFlowClusterHBHE_cfi import *
from ..modules.hltParticleFlowClusterHCAL_cfi import *

HLTPFHcalClustering = cms.Sequence( hltParticleFlowRecHitHBHESoA + hltParticleFlowRecHitHBHE + hltParticleFlowClusterHBHESoA + hltParticleFlowClusterHBHE + hltParticleFlowClusterHCAL )
