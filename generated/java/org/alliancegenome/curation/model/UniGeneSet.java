package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  XenBase-specific. A set of three genes from X. tropicalis and X. laevis (S and L forms) representing a single unigene.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class UniGeneSet extends BiologicalEntity {

  private List<Gene> genes;

}