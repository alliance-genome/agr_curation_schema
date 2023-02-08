package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  The environmental context in which an experiment is carried out. This may (e.g. drug treatment) or may not (e.g. standard conditions) directly influence the outcome of the experiment.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExperimentalCondition extends AuditedObject {

  private String uniqueId;
  private ZECOTerm conditionClass;
  private String conditionSummary;
  private ExperimentalConditionOntologyTerm conditionId;
  private String conditionFreeText;
  private String conditionQuantity;
  private AnatomicalTerm conditionAnatomy;
  private GOTerm conditionGeneOntology;
  private NCBITaxonTerm conditionTaxon;
  private ChemicalTerm conditionChemical;

}