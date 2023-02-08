package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Ingest class for genes
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneDTO extends GenomicEntityDTO {

  private SymbolSlotAnnotationDTO geneSymbolDto;
  private FullNameSlotAnnotationDTO geneFullNameDto;
  private SystematicNameSlotAnnotationDTO geneSystematicNameDto;
  private List<NameSlotAnnotationDTO> geneSynonymDtos;
  private String geneTypeCurie;

}