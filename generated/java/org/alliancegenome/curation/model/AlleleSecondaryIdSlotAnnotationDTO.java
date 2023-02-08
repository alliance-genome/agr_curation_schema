package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleSecondaryIdSlotAnnotationDTO extends SlotAnnotationDTO {

  private String secondaryId;

}