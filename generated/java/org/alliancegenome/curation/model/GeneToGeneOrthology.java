package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class GeneToGeneOrthology extends AuditedObject {

  private Gene geneSubject;
  private String predicate;
  private Gene geneObject;

}