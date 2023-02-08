package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  The developmental stage and/or age of the specimen in an annotation. Developmental_stage_stop is optional. Add an uncertainty flag here?
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TemporalContext extends AuditedObject {

  private StageTerm developmentalStageStart;
  private StageTerm developmentalStageStop;
  private String age;
  private String temporalQualifiers;

}