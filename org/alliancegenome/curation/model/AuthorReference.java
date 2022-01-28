package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;


@Data
@EqualsAndHashCode(callSuper=false)
public class AuthorReference  {

  private InformationContentEntity correspondingAuthor;
  private String firstName;
  private String middleName;
  private String lastName;
  private InformationContentEntity initials;
  private List<CrossReference> crossReferences;

}