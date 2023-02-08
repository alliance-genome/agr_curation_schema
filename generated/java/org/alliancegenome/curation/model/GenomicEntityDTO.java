package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class GenomicEntityDTO extends BiologicalEntityDTO {

  private List<CrossReferenceDTO> crossReferenceDtos;
  private List<String> secondaryIdentifiers;
  private List<GenomicLocationAssociationDTO> genomicLocationAssociationDtos;

}