package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Base class linking a variant to a position on a genomic entity and the resulting consequence to the sequence and/or function of that genomic entity. Slots are provided for data taken from a source publication or data load and for data resulting from manual curation. Where the values are the same, the curator has confirmed the information from the source.  In other cases, the curator's analysis has resulted in different values, for instance, if the assembly is different, the source did not specify the transcript or protein isoform, the definition of the transcript or protein isoform used by the source has changed, or if there was an error in the source data.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class VariantLocation extends AuditedObject {

  private ECOTerm evidenceCode;
  private Reference singleReference;
  private Integer startPosition;
  private Integer endPosition;
  private String referenceSequence;
  private String variantSequence;
  private SOTerm consequence;

}