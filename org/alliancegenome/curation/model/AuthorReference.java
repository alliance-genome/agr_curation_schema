package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;


@Data
@EqualsAndHashCode(callSuper=false)
public class AuthorReference  {

  private InformationContentEntity firstName;
  private InformationContentEntity middleNames;
  private InformationContentEntity lastName;

}