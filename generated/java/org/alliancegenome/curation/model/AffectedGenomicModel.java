package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Includes inbred strains, stocks, disease models and mutant genotypes
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AffectedGenomicModel extends GenomicEntity {

  private String name;
  private VocabularyTerm subtype;
  private List<AffectedGenomicModelComponent> components;
  private List<SequenceTargetingReagent> sequenceTargetingReagents;
  private String parentalPopulations;
  private DataProvider dataProvider;
  private List<Reference> references;

}