package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  Molecules as described by WormBase
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Molecule extends ChemicalTerm {

  private Integer tableKey;
  private Person createdBy;
  private String creationDate;
  private Person modifiedBy;
  private String dateLastModified;

}