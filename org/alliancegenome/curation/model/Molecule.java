package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  Molecules as described by WormBase
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Molecule  {

  private String curie;
  private String name;
  private String inchi;
  private String inchiKey;
  private String iupac;
  private String formula;
  private String smiles;
  private List<Synonym> synonyms;
  private List<CrossReference> crossReferences;
  private Integer tableKey;
  private Person createdBy;
  private String creationDate;
  private Person modifiedBy;
  private String dateLastModified;

}