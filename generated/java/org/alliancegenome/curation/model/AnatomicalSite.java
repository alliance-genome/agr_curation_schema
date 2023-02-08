package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  The developmental stage and/or age of the specimen in an annotation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AnatomicalSite extends AuditedObject {

  private AnatomicalTerm anatomicalStructure;
  private AnatomicalTerm anatomicalSubstructure;
  private GOTerm cellularComponent;
  private String spatialQualifiers;

}