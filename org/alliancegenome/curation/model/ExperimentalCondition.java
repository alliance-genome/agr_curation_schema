package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  The environmental context in which an experiment is carried out. This may (e.g. drug treatment) or may not (e.g. standard conditions) directly influence the outcome of the experiment.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExperimentalCondition  {

  private String curie;
  private OntologyTerm conditionClass;
  private String conditionStatement;
  private OntologyTerm conditionId;
  private String conditionQuantity;
  private OntologyTerm conditionAnatomy;
  private OntologyTerm conditionGeneOntology;
  private OntologyTerm conditionTaxon;
  private OntologyTerm conditionChemical;

}