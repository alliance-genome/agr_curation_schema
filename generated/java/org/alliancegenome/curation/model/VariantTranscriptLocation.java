package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Links a variant to a position on a specified transcript and the resulting consequence to the sequence and/or function of that transcript.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VariantTranscriptLocation extends VariantLocation {

  private Transcript transcript;

}