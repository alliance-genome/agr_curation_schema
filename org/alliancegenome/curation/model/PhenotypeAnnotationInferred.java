package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  A curated phenotype annotation (see class PhenotypeAnnotationCurated) for which inferences have been made to apply additional information such as inferred gene or inferred allele.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PhenotypeAnnotationInferred extends PhenotypeAnnotationCurated {

  private Gene inferredGene;
  private Allele inferredAllele;

}