package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  This bulk load automatically pulls files from a defined BulkURLLoad
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BulkURLLoad extends BulkScheduledLoad {

  private String bulkloadUrl;

}