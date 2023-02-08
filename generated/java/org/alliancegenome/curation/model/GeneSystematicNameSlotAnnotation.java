package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  The one current systematic name for the gene.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneSystematicNameSlotAnnotation extends NameSlotAnnotation {

  private Gene singleGene;

}