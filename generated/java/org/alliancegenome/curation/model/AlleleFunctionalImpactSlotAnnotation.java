package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleFunctionalImpactSlotAnnotation extends SlotAnnotation {

  private Allele singleAllele;
  private List<VocabularyTerm> functionalImpacts;
  private PhenotypeTerm phenotypeTerm;
  private String phenotypeStatement;

}