package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleDatabaseStatusSlotAnnotation extends SlotAnnotation {

  private Allele singleAllele;
  private VocabularyTerm databaseStatus;

}