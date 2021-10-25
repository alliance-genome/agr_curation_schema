package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  Class for transcript-level VEP results
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VariantTranscriptConsequence extends VariantConsequence {

  private String aminoAcidReference;
  private String aminoAcidVariant;
  private String codonReference;
  private String codonVariant;
  private Integer cdnaStart;
  private Integer cdnaEnd;
  private Integer cdsStart;
  private Integer cdsEnd;
  private Integer proteinStart;
  private Integer proteinEnd;
  private String hgvsProteinNomenclature;
  private String hgvsCodingNomenclature;

}