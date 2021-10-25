package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  Free-text describing some aspect of an entity.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EntityStatement  {

  private String statementSubject;
  private String statementType;
  private String statementText;
  private List<Reference> references;

}