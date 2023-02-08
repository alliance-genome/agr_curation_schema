package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  An ontology term representing a chemical or molecule
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class ChemicalTerm extends OntologyTerm {

  private String inchi;
  private String inchiKey;
  private String iupac;
  private String formula;
  private String smiles;

}