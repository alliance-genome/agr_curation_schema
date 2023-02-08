package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class CrossReferenceDTO extends AuditedObjectDTO {

  private String referencedCurie;
  private String pageArea;
  private String displayName;
  private String prefix;

}