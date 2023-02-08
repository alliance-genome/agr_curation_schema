package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  All aliases (non-preferred names) for the gene. Any type of synonym is acceptable.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneSynonymSlotAnnotation extends NameSlotAnnotation {

  private Gene singleGene;

}