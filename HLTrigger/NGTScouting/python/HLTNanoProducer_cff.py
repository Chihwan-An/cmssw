import FWCore.ParameterSet.Config as cms

from PhysicsTools.NanoAOD.common_cff import *

from PhysicsTools.NanoAOD.genparticles_cff import *
from PhysicsTools.PatAlgos.slimming.prunedGenParticles_cfi import *
from HLTrigger.NGTScouting.hltVertices_cfi import *
from HLTrigger.NGTScouting.hltEGammaPacker_cfi import *
from HLTrigger.NGTScouting.hltPhotons_cfi import *
from HLTrigger.NGTScouting.hltElectrons_cfi import *
from HLTrigger.NGTScouting.hltMuons_cfi import *
from HLTrigger.NGTScouting.hltTracks_cfi import *
from HLTrigger.NGTScouting.hltJets_cfi import *
from HLTrigger.NGTScouting.hltTaus_cfi import *
from HLTrigger.NGTScouting.hltTracksters_cfi import *
from HLTrigger.NGTScouting.hltTriggerAcceptFilter_cfi import hltTriggerAcceptFilter,dstTriggerAcceptFilter

#from HLTrigger.Configuration.HLT_75e33.modules.hltHpsCombinatoricRecoTaus_cfi import *
#from HLTrigger.Configuration.HLT_75e33.modules.hltHpsSelectionDiscriminator_cfi import *
#from HLTrigger.Configuration.HLT_75e33.modules.hltHpsPFTauProducerSansRefs_cfi import *
#from HLTrigger.Configuration.HLT_75e33.modules.hltHpsPFTauProducer_cfi import *
#from HLTrigger.Configuration.HLT_75e33.modules.hltAK4PFJets_cfi import *
#from HLTrigger.Configuration.HLT_75e33.modules.hltPfTICL_cfi import *
#from HLTrigger.Configuration.HLT_75e33.modules.hltParticleFlowTmpBarrel_cfi import *
#from HLTrigger.Configuration.HLT_75e33.modules.hltParticleFlowTmp_cfi import *
#from HLTrigger.Configuration.HLT_75e33.modules.hltPhase2L3Muons_cfi import *
#from HLTrigger.Configuration.HLT_75e33.modules.hltTiclTrackstersMerge_cfi import *
#from HLTrigger.Configuration.HLT_75e33.modules.hltTiclCandidate_cfi import *


#from PhysicsTools.NanoAOD.taus_cff import *
#from PhysicsTools.NanoAOD.simpleCandidateFlatTableProducer_cfi import *
#from PhysicsTools.NanoAOD.simpleGenParticleFlatTableProducer_cfi import *
#from PhysicsTools.NanoAOD.simplePATTauFlatTableProducer_cfi import *
#from PhysicsTools.JetMCAlgos.TauGenJets_cfi import * 
#from PhysicsTools.JetMCAlgos.TauGenJetsDecayModeSelectorAllHadrons_cfi import *
#from PhysicsTools.PatAlgos.patTauSignalCandidatesProducer_cfi import *


hltNanoProducer = cms.Sequence(
    prunedGenParticles
    + finalGenParticles
    + genParticleTable
    + hltTriggerAcceptFilter
    + hltVertexTable
    + hltPixelTrackTable
    + hltGeneralTrackTable
    + hltEgammaPacker
    + hltPhotonTable
    + hltElectronTable
    + hltPhase2L3MuonIdTracks
    + hltMuonTable
    + hltPFCandidateTable
    + hltJetTable
    
    + hltTrackstersTable

    #+ hltTiclCandidate
    #+ hltTiclTrackstersMerge
    #+ hltPhase2L3Muons
    #+ hltPfTICL
    #+ hltParticleFlowTmpBarrel
    #+ hltParticleFlowTmp
    #+ hltAK4PFJets
    #+ hltHpsCombinatoricRecoTaus
    #+ hltHpsSelectionDiscriminator
    #+ hltHpsPFTauProducerSansRefs
    #+ hltHpsPFTauProducer
    + hltTauTable

    #+ genVisTauTable
    #+ tauMCTable
)

dstNanoProducer = cms.Sequence(
    prunedGenParticles
    + finalGenParticles
    + genParticleTable
    + dstTriggerAcceptFilter
    + hltVertexTable
    + hltPixelTrackTable
    + hltGeneralTrackTable
    + hltEgammaPacker
    + hltPhotonTable
    + hltElectronTable
    + hltPhase2L3MuonIdTracks
    + hltMuonTable
    + hltPFCandidateTable
    + hltJetTable
    + hltTrackstersTable
    
    #+ hltTiclCandidate
    #+ hltTiclTrackstersMerge
    #+ hltPhase2L3Muons
    #+ hltPfTICL
    #+ hltParticleFlowTmpBarrel
    #+ hltParticleFlowTmp
    #+ hltAK4PFJets
    #+ hltHpsCombinatoricRecoTaus
    #+ hltHpsSelectionDiscriminator
    #+ hltHpsPFTauProducerSansRefs
    #+ hltHpsPFTauProducer
    + hltTauTable
    #+ genVisTauTable
    #+ tauMCTable
)

def hltNanoCustomize(process):

    if hasattr(process, "NANOAODSIMoutput"):
        process.prunedGenParticles.src = "genParticles"
        process.genParticleTable.externalVariables = cms.PSet() # remove iso as external variable from PhysicsTools/NanoAOD/python/genparticles_cff.py:37 (hopefully temporarily)
        process.NANOAODSIMoutput.outputCommands.append(
            "keep nanoaodFlatTable_*Table*_*_*"
        )
        process.NANOAODSIMoutput.SelectEvents = cms.untracked.PSet(
            SelectEvents = cms.vstring(
                [p for p in process.paths if p.startswith('HLT_') or p.startswith('DST_')]
            )
        )

    return process

def hltNanoValCustomize(process):
    if hasattr(process, "dstNanoProducer"):
        process.dstNanoProducer += (process.hltTrackstersAssociationOneToManyTable + process.hltSimCl2CPOneToOneFlatTable)

    return process
