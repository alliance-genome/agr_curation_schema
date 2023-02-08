package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Association between an allele and a protein
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleProteinAssociationDTO extends AlleleGenomicEntityAssociationDTO {

  private String proteinCurie;

}