package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  The one current symbol for the gene.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneSymbolSlotAnnotation extends NameSlotAnnotation {

  private Gene singleGene;

}