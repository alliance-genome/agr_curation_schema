package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  An annotation asserting an association between an allele and a phenotype supported by evidence.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AllelePhenotypeAnnotation extends PhenotypeAnnotation {

  private Gene inferredGene;

}