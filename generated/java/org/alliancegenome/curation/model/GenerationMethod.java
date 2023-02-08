package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class GenerationMethod extends AuditedObject {

  private List<VocabularyTerm> mutagenesisMethods;
  private String mutagenesisTarget;
  private VocabularyTerm integrationMethod;
  private VocabularyTerm chemicalMutagen;
  private VocabularyTerm irradiationMutagen;

}