package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  This a bulk load that includes a cron scheuld
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BulkScheduledLoad extends BulkLoad {

  private boolean scheduleActive;
  private String cronSchedule;
  private String schedulingErrorMessage;

}