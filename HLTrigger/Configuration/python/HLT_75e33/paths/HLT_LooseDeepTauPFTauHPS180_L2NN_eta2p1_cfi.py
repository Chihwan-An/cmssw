import FWCore.ParameterSet.Config as cms

from ..sequences.HLTBeginSequence_cfi import *
from ..modules.hltL1SingleNNTau150_cfi import *
from ..sequences.HLTRawToDigiSequence_cfi import *
from ..sequences.HLTHgcalLocalRecoSequence_cfi import *
from ..sequences.HLTLocalrecoSequence_cfi import *
from ..sequences.HLTTrackingSequence_cfi import *
from ..sequences.HLTMuonsSequence_cfi import *
from ..sequences.HLTParticleFlowSequence_cfi import *
from ..sequences.HLTAK4PFJetsReconstruction_cfi import *
from ..sequences.HLTPFTauHPS_cfi import *
from ..sequences.HLTHPSDeepTauPFTauSequence_cfi import *
from ..sequences.HLTEndSequence_cfi import *
from ..modules.hltPreLooseDeepTauPFTauHPS180L2NNeta2p1_cfi import *
from ..modules.hltAK4PFJetsForTaus_cfi import *
from ..modules.hltParticleFlowRecHitECALUnseeded_cfi import *
from ..modules.hltParticleFlowClusterECALUncorrectedUnseeded_cfi import *
from ..modules.hltParticleFlowClusterECALUnseeded_cfi import *
from ..modules.hltHpsSelectedPFTauLooseTauWPDeepTau_cfi import *
from ..modules.hltHpsPFTau180LooseTauWPDeepTau_cfi import *
from ..modules.hltL1JetsHLTPFTauLooseSingleTauWPDeepTauMatch_cfi import *


HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1 = cms.Path(
    HLTBeginSequence 
    + hltL1SingleNNTau150
    + hltPreLooseDeepTauPFTauHPS180L2NNeta2p1                               

    + HLTRawToDigiSequence 
    + HLTHgcalLocalRecoSequence 
    + HLTLocalrecoSequence 
    + HLTTrackingSequence 
    
    + HLTMuonsSequence 

    + HLTParticleFlowSequence 
    + hltParticleFlowRecHitECALUnseeded
    + hltParticleFlowClusterECALUncorrectedUnseeded
    + hltParticleFlowClusterECALUnseeded
    
    + HLTAK4PFJetsReconstruction 
    + hltAK4PFJetsForTaus 
    + HLTPFTauHPS 
    
    + HLTHPSDeepTauPFTauSequence 
    + hltHpsSelectedPFTauLooseTauWPDeepTau 

    +hltL1JetsHLTPFTauLooseSingleTauWPDeepTauMatch

    + hltHpsPFTau180LooseTauWPDeepTau 
    
    + HLTEndSequence 
)


