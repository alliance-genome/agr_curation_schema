package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  The relationship between an allele and a cell line.  Includes mutant/ embryonic stem cell lines known to carry the allele, and parental cell line of alleles made in embryonic stem cells.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleCellLineAssociationDTO extends AuditedObjectDTO {

  private String alleleCurie;
  private String predicateName;
  private String cellLineCurie;
  private List<String> evidenceCuries;

}