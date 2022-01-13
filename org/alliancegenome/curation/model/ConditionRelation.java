package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  A pairing of an experimental condition relation (i.e. has_condition) with a list of 1 or more ExperimentalCondition objects. Annotation objects can connect directly to a set of 0 or more of these ConditionRelation objects via a 'condition_relations' slot to express the experimental conditions relevant to the annotation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ConditionRelation  {

  private String uniqueId;
  private String conditionRelationType;
  private List<ExperimentalCondition> conditions;

}