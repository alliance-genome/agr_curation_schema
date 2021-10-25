package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  A high-level entity comprising .
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstractclass BiologicalEntity  {

  private String curie;
  private String taxon;
  private Integer tableKey;
  private Person producedBy;
  private String creationDate;
  private Person modifiedBy;
  private String dateLastModified;

}