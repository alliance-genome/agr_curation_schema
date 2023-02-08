package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public abstract class AlleleGenomicEntityAssociationDTO extends AuditedObjectDTO {

  private String alleleCurie;
  private String predicateName;
  private List<String> evidenceCuries;
  private String evidenceCodeCurie;
  private NoteDTO noteDto;

}