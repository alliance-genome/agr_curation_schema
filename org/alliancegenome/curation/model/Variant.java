package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  A DNA sequence that differs relative to a designated reference sequence.  The sequence occurs at a single position or in contiguous nucleotides.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Variant extends GenomicEntity {

  private String hgvsNomenclature;
  private String genomicReferenceSequence;
  private String genomicVariantSequence;
  private String paddingLeft;
  private String paddingRight;
  private String release;
  private List<String> dataProvider;
  private Gene computedGene;
  private Transcript variantOfTranscript;
  private Allele variantOfAllele;
  private String type;
  private List<Reference> references;
  private List<String> notes;
  private String proteinSequence;

}