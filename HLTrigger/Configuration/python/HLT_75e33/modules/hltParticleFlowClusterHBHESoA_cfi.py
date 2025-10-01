import FWCore.ParameterSet.Config as cms

hltParticleFlowClusterHBHESoA = cms.EDProducer( "PFClusterSoAProducer@alpaka",
    pfRecHits = cms.InputTag( "hltParticleFlowRecHitHBHESoA" ),
    topology = cms.ESInputTag( "hltESPPFRecHitHCALTopology","" ),
    seedFinder = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.vdouble( 0.125, 0.25, 0.35, 0.35 ),
          detector = cms.string( "HCAL_BARREL1" )
        ),
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.vdouble( 0.1375, 0.275, 0.275, 0.275, 0.275, 0.275, 0.275 ),
          detector = cms.string( "HCAL_ENDCAP" )
        )
      ),
      nNeighbours = cms.int32( 4 )
    ),
    initialClusteringStep = cms.PSet(  thresholdsByDetector = cms.VPSet( 
  cms.PSet(  gatheringThreshold = cms.vdouble( 0.1, 0.2, 0.3, 0.3 ),
    detector = cms.string( "HCAL_BARREL1" )
  ),
  cms.PSet(  gatheringThreshold = cms.vdouble( 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2 ),
    detector = cms.string( "HCAL_ENDCAP" )
  )
) ),
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      maxIterations = cms.uint32( 5 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  recHitEnergyNorm = cms.vdouble( 0.1, 0.2, 0.3, 0.3 ),
          detector = cms.string( "HCAL_BARREL1" )
        ),
        cms.PSet(  recHitEnergyNorm = cms.vdouble( 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2 ),
          detector = cms.string( "HCAL_ENDCAP" )
        )
      ),
      showerSigma = cms.double( 10.0 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      timeResolutionCalcBarrel = cms.PSet( 
        corrTermLowE = cms.double( 0.0 ),
        threshLowE = cms.double( 6.0 ),
        noiseTerm = cms.double( 21.86 ),
        constantTermLowE = cms.double( 4.24 ),
        noiseTermLowE = cms.double( 8.0 ),
        threshHighE = cms.double( 15.0 ),
        constantTerm = cms.double( 2.82 )
      ),
      timeResolutionCalcEndcap = cms.PSet( 
        corrTermLowE = cms.double( 0.0 ),
        threshLowE = cms.double( 6.0 ),
        noiseTerm = cms.double( 21.86 ),
        constantTermLowE = cms.double( 4.24 ),
        noiseTermLowE = cms.double( 8.0 ),
        threshHighE = cms.double( 15.0 ),
        constantTerm = cms.double( 2.82 )
      )
    ),
    synchronise = cms.bool( False ),
    alpaka = cms.untracked.PSet(  backend = cms.untracked.string( "" ) )
)
