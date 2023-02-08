package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Base class for all curation reports
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CurationReport extends AuditedObject {

  private String name;
  private String birtReportFilePath;
  private boolean scheduleActive;
  private String cronSchedule;
  private String curationReportStatus;
  private CurationReportGroup curationReportGroup;
  private String errorMessage;
  private String schedulingErrorMessage;

}