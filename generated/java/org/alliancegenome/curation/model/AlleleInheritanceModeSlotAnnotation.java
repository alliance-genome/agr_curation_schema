package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleInheritanceModeSlotAnnotation extends SlotAnnotation {

  private Allele singleAllele;
  private VocabularyTerm inheritanceMode;
  private PhenotypeTerm phenotypeTerm;
  private String phenotypeStatement;

}