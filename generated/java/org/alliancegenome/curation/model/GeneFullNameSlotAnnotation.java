package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  The one current full name for the gene.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneFullNameSlotAnnotation extends NameSlotAnnotation {

  private Gene singleGene;

}