package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class ConstructDTO extends GenomicEntityDTO {

  private List<GenomicEntityDTO> constructComponentDtos;
  private List<String> referenceCuries;

}