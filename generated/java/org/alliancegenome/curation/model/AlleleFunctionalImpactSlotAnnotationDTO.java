package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleFunctionalImpactSlotAnnotationDTO extends SlotAnnotationDTO {

  private List<String> functionalImpactNames;
  private String phenotypeTermCurie;
  private String phenotypeStatement;

}