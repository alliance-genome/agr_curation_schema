package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  This class is use to group together curation reports
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CurationReportGroup extends AuditedObject {

  private String name;

}