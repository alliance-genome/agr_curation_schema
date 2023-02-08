package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleNoteSlotAnnotationDTO extends SlotAnnotationDTO {

  private NoteDTO noteDto;

}