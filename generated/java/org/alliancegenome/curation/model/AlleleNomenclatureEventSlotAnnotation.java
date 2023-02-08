package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleNomenclatureEventSlotAnnotation extends SlotAnnotation {

  private Allele singleAllele;
  private VocabularyTerm nomenclatureEvent;

}