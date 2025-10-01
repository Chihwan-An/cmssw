import FWCore.ParameterSet.Config as cms

from ..modules.hltMuonDTDigis_cfi import *
from ..modules.hltDt1DRecHits_cfi import *
from ..modules.hltDt4DSegments_cfi import *
from ..modules.hltMuonCSCDigis_cfi import *
from ..modules.hltCsc2DRecHits_cfi import *
from ..modules.hltCscSegments_cfi import *
from ..modules.hltMuonRPCDigisCPPF_cfi import *
from ..modules.hltOmtfDigis_cfi import *
from ..modules.hltMuonRPCDigisTwinMux_cfi import *
from ..modules.hltMuonRPCDigis_cfi import *
from ..modules.hltRpcRecHits_cfi import *
from ..modules.hltMuonGEMDigis_cfi import *
from ..modules.hltGemRecHits_cfi import *
from ..modules.hltGemSegments_cfi import *

HLTMuonLocalRecoSequence = cms.Sequence(
    hltMuonDTDigis +
    hltDt1DRecHits + 
    hltDt4DSegments + 
    hltMuonCSCDigis + 
    hltCsc2DRecHits + 
    hltCscSegments + 
    hltMuonRPCDigisCPPF + 
    hltOmtfDigis + 
    hltMuonRPCDigisTwinMux + 
    hltMuonRPCDigis + 
    hltRpcRecHits + 
    hltMuonGEMDigis + 
    hltGemRecHits + 
    hltGemSegments )