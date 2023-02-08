package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Ingest class for association between a biological entity and a disease
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class DiseaseAnnotationDTO extends AuditedObjectDTO {

  private String diseaseRelationName;
  private String doTermCurie;
  private String modEntityId;
  private boolean negated;
  private List<String> evidenceCuries;
  private List<String> evidenceCodeCuries;
  private String referenceCurie;
  private String annotationTypeName;
  private List<String> withGeneCuries;
  private List<String> diseaseQualifierNames;
  private List<ConditionRelationDTO> conditionRelationDtos;
  private String geneticSexName;
  private List<NoteDTO> noteDtos;
  private DataProviderDTO dataProviderDto;
  private DataProviderDTO secondaryDataProviderDto;
  private String diseaseGeneticModifierCurie;
  private String diseaseGeneticModifierRelationName;

}