package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class NoteDTO extends AuditedObjectDTO {

  private String freeText;
  private String noteTypeName;
  private List<String> evidenceCuries;

}