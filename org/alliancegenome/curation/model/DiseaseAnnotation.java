package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  An annotation asserting an association between a biological entity and a disease supported by evidence.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DiseaseAnnotation extends Association {

  private String curie;
  private String modId;
  private Boolean negated;
  private List<ECOTerm> evidenceCodes;
  private Reference reference;
  private String annotationType;
  private Gene with;
  private String diseaseQualifiers;
  private List<ConditionRelation> conditionRelations;
  private String geneticSex;
  private String privateNote;
  private String diseaseAnnotationNote;
  private String diseaseAnnotationSummary;
  private List<String> dataProvider;
  private BiologicalEntity diseaseGeneticModifier;
  private String diseaseGeneticModifierRelation;
  private Integer tableKey;
  private Person createdBy;
  private String creationDate;
  private Person modifiedBy;
  private String dateLastModified;

}