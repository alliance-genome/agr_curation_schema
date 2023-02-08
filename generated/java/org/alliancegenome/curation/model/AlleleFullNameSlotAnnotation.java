package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  The one current full name for the allele.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleFullNameSlotAnnotation extends NameSlotAnnotation {

  private Allele singleAllele;

}