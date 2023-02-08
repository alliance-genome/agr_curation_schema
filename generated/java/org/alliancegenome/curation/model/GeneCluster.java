package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  A gene cluster is a set of genes which have a biological significance, and which are probably clustered together on the genome, like histones and miRNAs
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneCluster extends BiologicalEntity {

  private List<Gene> genes;
  private Note relatedNote;

}