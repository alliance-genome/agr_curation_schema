package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Object used to describe the indiviual run of this BulkLoadFile
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BulkLoadFileHistory extends AuditedObject {

  private String loadStarted;
  private String loadFinished;
  private Integer totalRecords;
  private Integer failedRecords;
  private String completedRecords;
  private List<String> loadExceptions;

}