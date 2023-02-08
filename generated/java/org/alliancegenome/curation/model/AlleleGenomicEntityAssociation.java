package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Association between an allele and a genomic entity
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class AlleleGenomicEntityAssociation extends Association {

  private ECOTerm evidenceCode;
  private Note relatedNote;

}