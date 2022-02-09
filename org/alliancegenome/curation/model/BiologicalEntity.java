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
  private NCBITaxonTerm taxon;
  private Integer tableKey;
  private Person createdBy;
  private String creationDate;
  private Person modifiedBy;
  private String dateLastModified;

}