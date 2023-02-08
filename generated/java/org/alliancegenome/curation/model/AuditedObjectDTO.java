package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Base class for all other LinkML DTO classes.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AuditedObjectDTO  {

  private String createdByCurie;
  private String dateCreated;
  private String updatedByCurie;
  private String dateUpdated;
  private String dbDateCreated;
  private String dbDateUpdated;
  private boolean internal;
  private boolean obsolete;

}