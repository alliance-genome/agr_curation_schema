package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  A concept or class in a simple vocabulary.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VocabularyTerm extends AuditedObject {

  private String name;
  private String abbreviation;
  private String definition;
  private List<String> textSynonyms;

}