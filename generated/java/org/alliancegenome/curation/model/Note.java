package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Note object for capturing free-text describing some attribute of an entity, coupled with a 'note type', internal boolean, and an optional list of references. Permissible values for note_type can be viewed and managed in the A-Team curation UI Controlled Vocabulary Terms Table.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Note extends AuditedObject {

  private String freeText;
  private VocabularyTerm noteType;
  private List<InformationContentEntity> evidence;

}