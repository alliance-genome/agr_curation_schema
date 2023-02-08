package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleDatabaseStatusSlotAnnotationDTO extends SlotAnnotationDTO {

  private String databaseStatusName;

}