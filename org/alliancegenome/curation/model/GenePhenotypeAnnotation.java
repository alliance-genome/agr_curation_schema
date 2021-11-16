package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  An annotation asserting an association between a gene and a phenotype supported by evidence.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GenePhenotypeAnnotation extends PhenotypeAnnotation {

  private AffectedGenomicModel sgdStrainBackground;

}