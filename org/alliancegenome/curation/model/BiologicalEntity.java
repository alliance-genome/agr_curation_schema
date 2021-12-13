package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  A high-level entity comprising .
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BiologicalEntity  {

  private String curie;
  private String taxon;
  private Integer tableKey;
  private Person createdBy;
  private String creationDate;
  private Person modifiedBy;
  private String dateLastModified;

}