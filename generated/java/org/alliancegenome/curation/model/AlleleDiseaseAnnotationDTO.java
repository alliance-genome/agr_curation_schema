package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Ingest class for an association between an allele and a disease
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleDiseaseAnnotationDTO extends DiseaseAnnotationDTO {

  private String alleleCurie;
  private String inferredGeneCurie;
  private List<String> assertedGeneCuries;

}