package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Links a variant to a position on a specified polypeptide and the resulting consequence to the sequence and/or function of that polypeptide.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VariantPolypeptideLocation extends VariantLocation {

  private Transcript polypeptide;
  private List<Transcript> associatedTranscripts;

}