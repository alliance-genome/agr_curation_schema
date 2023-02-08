package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Medical Subject Headings information coming from PubMed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MeshDetail extends AuditedObject {

  private int meshDetailId;
  private int referenceId;
  private String headingTerm;
  private String qualifierTerm;

}