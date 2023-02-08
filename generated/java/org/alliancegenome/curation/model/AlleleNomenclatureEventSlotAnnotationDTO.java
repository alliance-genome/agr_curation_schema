package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleNomenclatureEventSlotAnnotationDTO extends SlotAnnotationDTO {

  private String nomenclatureEventName;

}