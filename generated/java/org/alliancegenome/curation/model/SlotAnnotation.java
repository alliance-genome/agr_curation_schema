package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  SlotAnnotation classes should be used when we need to attach metadata (in particular evidence and provenance) to a slot in the context of its referencing class, that can not be fully captured using an Association between the full class itself, and an InformationContentEntity. Evidence and provenance can exist here in the form of an evidence code, a publication, a personal communication or any other kind of InformationContentEntity. SlotAnnotation classes are used where the slot is not referencing a class in and of itself, and often has a scalar range.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlotAnnotation extends AuditedObject {

  private List<InformationContentEntity> evidence;

}