package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class CrossReference extends AuditedObject {

  private String referencedCurie;
  private ResourceDescriptorPage resourceDescriptorPage;
  private String displayName;

}