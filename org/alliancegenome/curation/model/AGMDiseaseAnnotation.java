package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;


@Data
@EqualsAndHashCode(callSuper=false)
public class AGMDiseaseAnnotation extends DiseaseAnnotation {

  private Allele inferredAllele;
  private Gene inferredGene;

}