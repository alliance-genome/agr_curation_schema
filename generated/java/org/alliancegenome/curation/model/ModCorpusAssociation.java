package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  For a given reference and Mod, whether it is inside corpus, outside corpus, or needs review, as well as where this sorting came from.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ModCorpusAssociation extends AuditedObject {

  private boolean corpus;
  private int modCorpusAssociationId;
  private String modCorpusSortSource;
  private int allianceMemberId;
  private int referenceId;
  private String curie;

}