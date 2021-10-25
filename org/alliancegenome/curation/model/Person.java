package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;


@Data
@EqualsAndHashCode(callSuper=false)
public class Person extends Agent {

  private InformationContentEntity lastName;
  private InformationContentEntity firstName;
  private String orcid;

}