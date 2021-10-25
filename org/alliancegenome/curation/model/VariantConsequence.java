package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  Parent class for gene- and transcript-level consequences
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstractclass VariantConsequence  {

  private Variant subject;
  private String object;
  private String vepConsequence;
  private String vepImpact;
  private Float polyphenScore;
  private String polyphenPrediction;
  private Float siftScore;
  private String siftPrediction;

}