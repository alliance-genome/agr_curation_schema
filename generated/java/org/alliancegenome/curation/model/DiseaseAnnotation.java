package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  An annotation asserting an association between a biological entity and a disease supported by evidence.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class DiseaseAnnotation extends Association {

  private String curie;
  private String uniqueId;
  private String modEntityId;
  private boolean negated;
  private List<ECOTerm> evidenceCodes;
  private Reference singleReference;
  private VocabularyTerm annotationType;
  private List<Gene> withOrFrom;
  private List<VocabularyTerm> diseaseQualifiers;
  private List<ConditionRelation> conditionRelations;
  private VocabularyTerm geneticSex;
  private List<Note> relatedNotes;
  private DataProvider dataProvider;
  private DataProvider secondaryDataProvider;
  private String diseaseGeneticModifier;
  private VocabularyTerm diseaseGeneticModifierRelation;

}