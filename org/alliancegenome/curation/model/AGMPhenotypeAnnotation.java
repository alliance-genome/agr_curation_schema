package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  An annotation asserting an association between an AGM and a phenotype supported by evidence.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AGMPhenotypeAnnotation extends PhenotypeAnnotation {

  private Allele inferredAllele;
  private Gene inferredGene;

}