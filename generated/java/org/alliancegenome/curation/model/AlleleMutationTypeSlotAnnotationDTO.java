package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleMutationTypeSlotAnnotationDTO extends SlotAnnotationDTO {

  private List<String> mutationTypeCuries;

}