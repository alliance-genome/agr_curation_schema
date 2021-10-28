package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  An annotation asserting an association between an allele and a disease supported by evidence.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleDiseaseAnnotation extends DiseaseAnnotation {

  private Gene inferredGene;

}