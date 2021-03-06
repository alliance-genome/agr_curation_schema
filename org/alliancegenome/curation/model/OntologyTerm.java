package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  A concept or class in an ontology, vocabulary or thesaurus. Note, ontology terms can be found in multiple ontologies (ie: mireoting). defining_slots helps define an alternative key for ontology terms.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OntologyTerm  {

  private String curie;
  private String dbkey;
  private String name;
  private String definition;
  private List<String> definitionUrls;
  private String type;
  private Boolean isObsolete;
  private List<CrossReference> crossReferences;
  private List<Synonym> synonyms;
  private String namespace;
  private List<String> subsets;
  private List<String> secondaryIdentifiers;

}