package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  A DNA, RNA or protein/polypeptide sequence that differs relative to a designated reference sequence.  The sequence occurs at a single position or in a range of contiguous nucleotides or amino acids.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Variant extends GenomicEntity {

  private SOTerm variantType;
  private List<Note> relatedNotes;
  private SOTerm sourceGeneralConsequence;
  private List<VariantGenomeLocation> variantGenomeLocations;
  private List<VariantPolypeptideLocation> variantPolypeptideLocations;
  private List<VariantTranscriptLocation> variantTranscriptLocations;
  private List<SourceVariantLocation> sourceVariantLocations;
  private String variantStatus;

}