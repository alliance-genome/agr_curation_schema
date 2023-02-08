package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleMolecularMutationSlotAnnotation extends SlotAnnotation {

  private Allele singleAllele;
  private List<String> molecularMutations;

}