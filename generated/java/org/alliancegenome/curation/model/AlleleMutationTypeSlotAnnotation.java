package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleMutationTypeSlotAnnotation extends SlotAnnotation {

  private Allele singleAllele;
  private List<SOTerm> mutationTypes;

}