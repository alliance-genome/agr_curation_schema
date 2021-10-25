package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;


@Data
@EqualsAndHashCode(callSuper=false)
public class GeneDiseaseAnnotation extends DiseaseAnnotation {

  private AffectedGenomicModel sgdStrainBackground;

}