package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  This class is used to hold version of the files being loaded
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BulkLoadFile extends AuditedObject {

  private String bulkloadStatus;
  private String md5Sum;
  private String localFilePath;
  private Integer fileSize;
  private String s3Path;
  private String s3Url;
  private Integer recordCount;
  private String errorMessage;
  private BulkLoad bulkLoad;
  private String dateLastLoaded;

}