package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public abstract class BiologicalEntityDTO extends AuditedObjectDTO {

  private String curie;
  private String taxonCurie;

}