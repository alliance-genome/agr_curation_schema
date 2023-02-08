package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class ResourceDescriptorPage extends AuditedObject {

  private String name;
  private String urlTemplate;
  private String pageDescription;

}