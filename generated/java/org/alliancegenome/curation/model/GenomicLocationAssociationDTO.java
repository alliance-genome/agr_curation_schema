package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class GenomicLocationAssociationDTO extends AuditedObjectDTO {

  private String genomicEntityCurie;
  private String predicateName;
  private String chromosomeCurie;
  private List<String> evidenceCuries;
  private String assemblyCurie;
  private int start;
  private int end;

}