package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class SlotAnnotationDTO extends AuditedObjectDTO {

  private List<String> evidenceCuries;

}