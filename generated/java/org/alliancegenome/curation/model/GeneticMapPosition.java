package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  A genetic map position.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneticMapPosition extends GenomicEntity {

  private Chromosome geneticMapChromosome;
  private String geneticMapBand;
  private List<Float> geneticMapPositionCentimorgan;
  private List<Float> geneticMapPositionCentimorganError;
  private List<Float> geneticMapPositionRadiation;

}