package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Ingest class for the pairing of an experimental condition relation with a list of one or more conditions
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ConditionRelationDTO extends AuditedObjectDTO {

  private String handle;
  private String referenceCurie;
  private String conditionRelationTypeName;
  private List<ExperimentalConditionDTO> conditionDtos;

}