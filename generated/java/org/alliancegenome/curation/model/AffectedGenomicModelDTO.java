package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Ingest class for AGMs
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AffectedGenomicModelDTO extends GenomicEntityDTO {

  private String name;
  private String subtypeName;
  private List<String> referenceCuries;
  private DataProviderDTO dataProviderDto;
  private List<String> sequenceTargetingReagentCuries;
  private List<AffectedGenomicModelComponentDTO> componentDtos;

}