package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class OntologyTermClosure extends Association {

  private List<String> relationshipType;
  private Integer distanceBetween;

}