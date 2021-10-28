package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  An annotation asserting an association between a gene and a disease supported by evidence.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneDiseaseAnnotation extends DiseaseAnnotation {

  private AffectedGenomicModel sgdStrainBackground;

}