package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  a piece of information that typically is used as support for an assertion or annotation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InformationContentEntity extends AuditedObject {

  private String curie;

}