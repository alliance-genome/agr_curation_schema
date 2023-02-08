package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Ingest class for describing the environmental context in which an experiment is carried out
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExperimentalConditionDTO extends AuditedObjectDTO {

  private String conditionClassCurie;
  private String conditionIdCurie;
  private String conditionFreeText;
  private String conditionQuantity;
  private String conditionAnatomyCurie;
  private String conditionGeneOntologyCurie;
  private String conditionTaxonCurie;
  private String conditionChemicalCurie;

}