package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class LoggedInPerson extends Person {

  private String oktaId;
  private String oktaEmail;
  private String userSettings;
  private String apiToken;

}