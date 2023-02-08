package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  An entity representing a figure or table in a publication.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Figure extends AuditedObject {

  private String curie;
  private Reference singleReference;
  private String label;
  private String caption;
  private List<String> secondaryIdentifiers;

}