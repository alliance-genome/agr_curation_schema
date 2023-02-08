package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  A subset of terms from a Vocabulary that are valid for particular applications
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VocabularyTermSet extends AuditedObject {

  private String name;
  private Vocabulary vocabularyTermSetVocabulary;
  private String vocabularyTermSetDescription;
  private List<VocabularyTerm> memberTerms;

}