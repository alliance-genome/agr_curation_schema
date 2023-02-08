package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Association between an allele and a gene
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleGeneAssociationDTO extends AlleleGenomicEntityAssociationDTO {

  private String geneCurie;

}