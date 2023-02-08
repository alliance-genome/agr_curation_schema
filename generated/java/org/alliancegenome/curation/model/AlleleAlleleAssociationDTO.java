package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Association between an allele and another allele
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleAlleleAssociationDTO extends AlleleGenomicEntityAssociationDTO {

  private String objectAlleleCurie;

}