package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Ingest class for an Allele object
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleDTO extends GenomicEntityDTO {

  private SymbolSlotAnnotationDTO alleleSymbolDto;
  private FullNameSlotAnnotationDTO alleleFullNameDto;
  private List<String> referenceCuries;
  private String inCollectionName;
  private String laboratoryOfOriginCurie;
  private boolean isExtinct;
  private boolean isExtrachromosomal;
  private boolean isIntegrated;
  private String transgeneChromosomeLocationCurie;
  private List<AlleleMutationTypeSlotAnnotationDTO> alleleMutationTypeDtos;
  private List<AlleleInheritanceModeSlotAnnotationDTO> alleleInheritanceModeDtos;
  private AlleleGermlineTransmissionStatusSlotAnnotationDTO alleleGermlineTransmissionStatusDto;
  private List<AlleleFunctionalImpactSlotAnnotationDTO> alleleFunctionalImpactDtos;
  private List<AlleleMolecularMutationSlotAnnotationDTO> alleleMolecularMutationDtos;
  private AlleleDatabaseStatusSlotAnnotationDTO alleleDatabaseStatusDto;
  private List<AlleleSecondaryIdSlotAnnotationDTO> alleleSecondaryIdDtos;
  private List<AlleleNomenclatureEventSlotAnnotationDTO> alleleNomenclatureEventDtos;
  private List<AlleleNoteSlotAnnotationDTO> alleleNoteDtos;
  private List<NameSlotAnnotationDTO> alleleSynonymDtos;

}