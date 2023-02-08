package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Links a variant to a genomic position and the resulting consequence to the sequence and/or function. In practice, functional consequences for variants which overlap genes are not generally provided at the genome level but rather are calculated and annotated relative to a specific transcript or protein isoform.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VariantGenomeLocation extends VariantLocation {

  private Assembly assembly;
  private Chromosome chromosome;

}