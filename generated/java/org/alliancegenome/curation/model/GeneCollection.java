package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  A gene collection is a set of genes which have been grouped based on experimental evidence, for example a set of interacting genes, genes in expression cluster, or a set of ChIP binding peaks
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneCollection extends BiologicalEntity {

  private List<Gene> genes;
  private Note relatedNote;
  private List<String> experimentType;

}