package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  This bulk load automatically pulls files from the BulkFMSLoad
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BulkFMSLoad extends BulkScheduledLoad {

  private String fmsDataType;
  private String fmsDataSubType;

}