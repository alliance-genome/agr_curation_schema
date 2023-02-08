package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  The relationship between an allele and constructs contained in that allele.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleConstructAssociationDTO extends AlleleGenomicEntityAssociationDTO {

  private String constructCurie;

}