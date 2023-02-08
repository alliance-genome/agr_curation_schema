package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleInheritanceModeSlotAnnotationDTO extends SlotAnnotationDTO {

  private String inheritanceModeName;
  private String phenotypeTermCurie;
  private String phenotypeStatement;

}