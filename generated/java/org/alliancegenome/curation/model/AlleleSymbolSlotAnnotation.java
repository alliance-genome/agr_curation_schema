package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  The one current symbol for the allele.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleSymbolSlotAnnotation extends NameSlotAnnotation {

  private Allele singleAllele;

}