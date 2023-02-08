package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Base class for all loads
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BulkLoad extends AuditedObject {

  private String name;
  private String bulkloadStatus;
  private String errorMessage;
  private String backendBulkLoadType;
  private String ontologyType;
  private BulkLoadGroup bulkloadGroup;
  private List<BulkLoadFile> loadFiles;

}