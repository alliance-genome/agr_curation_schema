package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;


@Data
@EqualsAndHashCode(callSuper=false)
public class Person extends Agent {

  private String lastName;
  private String middleName;
  private String firstName;
  private String orcid;
  private String emails;
  private String modId;
  private String uniqueId;

}