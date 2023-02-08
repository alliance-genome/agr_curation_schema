package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Ingest class for an association between an AGM and a disease
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AGMDiseaseAnnotationDTO extends DiseaseAnnotationDTO {

  private String agmCurie;
  private String inferredGeneCurie;
  private List<String> assertedGeneCuries;
  private String inferredAlleleCurie;
  private String assertedAlleleCurie;

}