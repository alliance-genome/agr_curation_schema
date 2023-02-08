package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleGenerationMethodAssociationDTO extends AuditedObjectDTO {

  private String alleleCurie;
  private String predicateName;
  private GenerationMethodDTO generationMethodDto;
  private List<String> evidenceCuries;
  private String mutationTargetStrainCurie;

}