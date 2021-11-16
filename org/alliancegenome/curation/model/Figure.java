package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  An entity representing a figure or table in a publication.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Figure  {

  private String curie;
  private Reference hasReference;
  private String label;
  private String caption;
  private List<String> secondaryIdentifiers;
  private Integer tableKey;
  private Person createdBy;
  private String creationDate;
  private Person modifiedBy;
  private String dateLastModified;

}