package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  The relationship between an allele and an image.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleImageAssociationDTO extends AuditedObjectDTO {

  private String alleleCurie;
  private String predicateName;
  private String imageCurie;
  private boolean primaryImage;
  private List<String> evidenceCuries;

}