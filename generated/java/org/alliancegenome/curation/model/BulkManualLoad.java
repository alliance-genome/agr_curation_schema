package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  This bulk load is used by DQM's to submit their files to the curation system
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BulkManualLoad extends BulkLoad {

  private String backendLoadType;

}