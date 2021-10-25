package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  Describes the relation between a reference and an object
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ReferenceType  {

  private String referenceAssociation;
  private List<Reference> references;

}