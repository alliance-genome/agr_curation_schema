package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  All aliases (non-preferred names) for the allele. Any type of synonym is acceptable.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleSynonymSlotAnnotation extends NameSlotAnnotation {

  private Allele singleAllele;

}