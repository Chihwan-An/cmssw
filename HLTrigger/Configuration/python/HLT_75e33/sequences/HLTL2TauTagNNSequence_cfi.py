import FWCore.ParameterSet.Config as cms

from ..sequences.HLTDoLocalPixelSequence_cfi import *

#from ..sequences.HLTRecoPixelTracksSequence_cfi import *
from ..sequences.HLTPhase2PixelTracksSequence_cfi import *

#from ..sequences.HLTRecopixelvertexingSequence_cfi import *
from ..modules.hltPhase2PixelVertices_cfi import *
from ..modules.hltPhase2TrimmedPixelVertices_cfi import *

#from ..sequences.HLTDoCaloSequence_cfi import *
from ..sequences.HLTDoFullUnpackingEgammaEcalSequence_cfi import *
from ..sequences.HLTDoLocalHcalSequence_cfi import *
from ..modules.hltPhase2TowerMakerForAll_cfi import *

#from ..modules.hltL1sDoubleTauBigOR_cfi import *
#from ..modules.hltL1sSingleTau_cfi import *
#from ..modules.hltL1sBigOrMuXXerIsoTauYYer_cfi import *
#from ..modules.hltL1sMu22erIsoTau40er_cfi import *
#from ..modules.hltL1sBigORDoubleTauJet_cfi import *
#from ..modules.hltL1VBFDiJetIsoTau_cfi import *
#from ..modules.hltL1sVeryBigORMu18erTauXXer2p1_cfi import *
#from ..modules.hltL1sTauVeryBigOR_cfi import *
#from ..modules.hltL1P2GTTau_cfi import *
from ..modules.hltL1SeedForDoublePuppiTau_cfi import *
from ..modules.hltPuppiTauTkIsoEle45_22L1TkFilter_cfi import *
from ..modules.hltPuppiTauTkMuon4218L1TkFilter_cfi import *
from ..modules.hltL2TauTagNNProducer_cfi import *



HLTL2TauTagNNSequence = cms.Sequence(
    HLTDoLocalPixelSequence +
    
    #HLTRecoPixelTracksSequence +
    HLTPhase2PixelTracksSequence +

    #HLTRecopixelvertexingSequence +
    hltPhase2PixelVertices + 
    hltPhase2TrimmedPixelVertices +
    
    #HLTDoCaloSequence +
    HLTDoFullUnpackingEgammaEcalSequence +
    HLTDoLocalHcalSequence +
    hltPhase2TowerMakerForAll +


    #cms.ignore(hltL1sDoubleTauBigOR) +
    #cms.ignore(hltL1sSingleTau) +
    #cms.ignore(hltL1sBigOrMuXXerIsoTauYYer) +
    #cms.ignore(hltL1sMu22erIsoTau40er) +
    #cms.ignore(hltL1sBigORDoubleTauJet) +
    #cms.ignore(hltL1VBFDiJetIsoTau) +
    #cms.ignore(hltL1sVeryBigORMu18erTauXXer2p1) +
    #cms.ignore(hltL1sTauVeryBigOR) +
    #cms.ignore(hltL1P2GTTau) +
    cms.ignore(hltL1SeedForDoublePuppiTau) +
    cms.ignore(hltPuppiTauTkIsoEle45_22L1TkFilter) +
    cms.ignore(hltPuppiTauTkMuon4218L1TkFilter) +


    hltL2TauTagNNProducer
)
