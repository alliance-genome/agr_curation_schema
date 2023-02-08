package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  the relationship between a Sequence Targeting Reagent and its targeted genes. The predicate should be a VocabularyTerm with one of the following values - targets
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SequenceTargetingReagentToGeneAssociation extends Association {

  private List<Reference> references;

}