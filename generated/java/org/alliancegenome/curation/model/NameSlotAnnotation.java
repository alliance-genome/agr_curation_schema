package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Some symbol or name for an object, including current names as well as aliases, with accompanying metadata. The entity to which the symbol/name applies is specified in objects that inherit from this object.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class NameSlotAnnotation extends SlotAnnotation {

  private VocabularyTerm nameType;
  private String formatText;
  private String displayText;
  private String synonymUrl;
  private VocabularyTerm synonymScope;

}