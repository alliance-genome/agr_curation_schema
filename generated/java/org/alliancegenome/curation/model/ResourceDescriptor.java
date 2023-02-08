package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class ResourceDescriptor extends AuditedObject {

  private String prefix;
  private String name;
  private List<String> synonyms;
  private String idPattern;
  private String idExample;
  private String defaultUrlTemplate;
  private List<ResourceDescriptorPage> resourcePages;

}