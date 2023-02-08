package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  The relationship between an allele and the AGM origin of the allele.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleOriginAssociationDTO extends AuditedObjectDTO {

  private String alleleCurie;
  private String predicateName;
  private String agmCurie;
  private List<String> evidenceCuries;

}