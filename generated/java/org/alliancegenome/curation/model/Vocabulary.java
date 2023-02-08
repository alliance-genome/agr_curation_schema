package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  A set of VocabularyTerm objects.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Vocabulary extends AuditedObject {

  private String name;
  private String vocabularyDescription;
  private List<VocabularyTerm> memberTerms;

}