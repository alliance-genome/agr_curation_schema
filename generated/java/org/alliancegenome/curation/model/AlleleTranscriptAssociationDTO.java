package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Association between an allele and a transcript
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleTranscriptAssociationDTO extends AlleleGenomicEntityAssociationDTO {

  private String transcriptCurie;

}