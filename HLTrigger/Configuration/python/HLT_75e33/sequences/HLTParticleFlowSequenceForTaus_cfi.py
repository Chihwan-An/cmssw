import FWCore.ParameterSet.Config as cms

from ..sequences.HLTPreshowerSequence_cfi import *
from ..sequences.HLTPFHcalClustering_cfi import *
from ..modules.hltParticleFlowRecHitECALUnseeded_cfi import *
from ..modules.hltParticleFlowRecHitHF_cfi import *
from ..modules.hltParticleFlowRecHitPSUnseeded_cfi import *
from ..modules.hltParticleFlowClusterECALUncorrectedUnseeded_cfi import *
from ..modules.hltParticleFlowClusterPSUnseeded_cfi import *
from ..modules.hltParticleFlowClusterECALUnseeded_cfi import *
from ..modules.hltParticleFlowClusterHF_cfi import *
from ..modules.hltLightPFTracks_cfi import *
from ..modules.hltParticleFlowBlockForTaus_cfi import *
from ..modules.hltParticleFlowForTaus_cfi import *

HLTParticleFlowSequenceForTaus = cms.Sequence( HLTPreshowerSequence + hltParticleFlowRecHitECALUnseeded + hltParticleFlowRecHitHF + hltParticleFlowRecHitPSUnseeded + hltParticleFlowClusterECALUncorrectedUnseeded + hltParticleFlowClusterPSUnseeded + hltParticleFlowClusterECALUnseeded + HLTPFHcalClustering + hltParticleFlowClusterHF + hltLightPFTracks + hltParticleFlowBlockForTaus + hltParticleFlowForTaus )
