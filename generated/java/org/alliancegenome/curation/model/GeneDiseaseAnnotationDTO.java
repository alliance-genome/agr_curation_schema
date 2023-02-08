package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Ingest class for an association between a gene and a disease
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneDiseaseAnnotationDTO extends DiseaseAnnotationDTO {

  private String geneCurie;
  private String sgdStrainBackgroundCurie;

}