package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Base class for all other LinkML classes. Some entity for which changes are tracked, including date/time of change, the agent responsible for the change, and whether the entity is internal (private).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AuditedObject  {

  private Person createdBy;
  private String dateCreated;
  private Person updatedBy;
  private String dateUpdated;
  private String dbDateCreated;
  private String dbDateUpdated;
  private boolean internal;
  private boolean obsolete;

}