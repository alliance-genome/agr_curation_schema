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
  private List<String> emails;
  private List<String> oldEmails;
  private String modId;
  private String uniqueId;

}