package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  A genetic interaction between genes (e.g. phenotypic suppression)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneGeneticInteraction extends GeneInteraction {

  private Allele interactorAGeneticPerturbation;
  private Allele interactorBGeneticPerturbation;
  private List<String> phenotypeOrTrait;

}