package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  The developmental stage and/or age of the specimen in an annotation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TemporalContext  {

  private StageTerm developmentalStage;
  private String age;
  private String temporalQualifiers;

}