package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  This class is use to group together bulk load_files
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BulkLoadGroup extends AuditedObject {

  private String name;
  private List<BulkLoad> loads;

}