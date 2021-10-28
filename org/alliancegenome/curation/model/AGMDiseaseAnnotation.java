package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  An annotation asserting an association between an AGM and a disease supported by evidence.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AGMDiseaseAnnotation extends DiseaseAnnotation {

  private Allele inferredAllele;
  private Gene inferredGene;

}