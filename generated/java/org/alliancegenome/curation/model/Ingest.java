package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class Ingest  {

  private String linkmlVersion;
  private List<AlleleDTO> alleleIngestSet;
  private List<AlleleDiseaseAnnotationDTO> diseaseAlleleIngestSet;
  private List<AGMDiseaseAnnotationDTO> diseaseAgmIngestSet;
  private List<GeneDiseaseAnnotationDTO> diseaseGeneIngestSet;
  private List<GeneDTO> geneIngestSet;
  private List<Variant> variantIngestSet;
  private List<AlleleVariantAssociationDTO> alleleVariantAssociationIngestSet;
  private List<AlleleGeneAssociationDTO> alleleGeneAssociationIngestSet;
  private List<AlleleTranscriptAssociationDTO> alleleTranscriptAssociationIngestSet;
  private List<AlleleProteinAssociationDTO> alleleProteinAssociationIngestSet;
  private List<AlleleConstructAssociationDTO> alleleConstructAssociationIngestSet;
  private List<AlleleCellLineAssociationDTO> alleleCellLineAssociationIngestSet;
  private List<AlleleOriginAssociationDTO> alleleOriginAssociationIngestSet;
  private List<AlleleImageAssociationDTO> alleleImageAssociationIngestSet;
  private List<AlleleGenerationMethodAssociationDTO> alleleGenerationMethodAssociationIngestSet;
  private List<GenomicLocationAssociationDTO> alleleGenomicLocationAssociationIngestSet;
  private List<AffectedGenomicModelDTO> agmIngestSet;
  private List<SequenceTargetingReagentDTO> sqtrIngestSet;
  private List<OntologyTermClosure> ontologyClosureIngestSet;

}