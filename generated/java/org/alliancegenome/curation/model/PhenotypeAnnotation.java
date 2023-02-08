package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  An annotation asserting an association between a biological entity and a phenotype supported by evidence.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PhenotypeAnnotation extends Association {

  private String curie;
  private Reference singleReference;
  private PhenotypeTerm phenotypeTerm;
  private List<ConditionRelation> conditionRelations;

}