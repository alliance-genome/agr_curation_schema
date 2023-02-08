package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AuthorReference extends AuditedObject {

  private boolean correspondingAuthor;
  private boolean firstAuthor;
  private String firstName;
  private String lastName;
  private List<CrossReference> crossReferences;

}