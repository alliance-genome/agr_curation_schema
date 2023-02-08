package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  One of multiple possible forms of a functional genomic element (most often described as a locus or gene), differing from the reference DNA sequence.  The genomic element can be endogenous or constructed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Allele extends GenomicEntity {

  private AlleleSymbolSlotAnnotation alleleSymbol;
  private AlleleFullNameSlotAnnotation alleleFullName;
  private List<Reference> references;
  private VocabularyTerm inCollection;
  private Laboratory laboratoryOfOrigin;
  private boolean isExtinct;
  private boolean isExtrachromosomal;
  private boolean isIntegrated;
  private Chromosome transgeneChromosomeLocation;
  private List<AlleleMutationTypeSlotAnnotation> alleleMutationTypes;
  private List<AlleleInheritanceModeSlotAnnotation> alleleInheritanceModes;
  private AlleleGermlineTransmissionStatusSlotAnnotation alleleGermlineTransmissionStatus;
  private List<AlleleFunctionalImpactSlotAnnotation> alleleFunctionalImpacts;
  private List<AlleleMolecularMutationSlotAnnotation> alleleMolecularMutations;
  private AlleleDatabaseStatusSlotAnnotation alleleDatabaseStatus;
  private List<AlleleSecondaryIdSlotAnnotation> alleleSecondaryIds;
  private List<AlleleNomenclatureEventSlotAnnotation> alleleNomenclatureEvents;
  private List<AlleleNoteSlotAnnotation> alleleNotes;
  private List<AlleleSynonymSlotAnnotation> alleleSynonyms;
  private List<AlleleGeneAssociation> alleleGeneAssociations;
  private List<AlleleTranscriptAssociation> alleleTranscriptAssociations;
  private List<AlleleProteinAssociation> alleleProteinAssociations;
  private List<AlleleAlleleAssociation> alleleAlleleAssociations;
  private List<AlleleVariantAssociation> alleleVariantAssociations;
  private List<AlleleConstructAssociation> alleleConstructAssociations;
  private List<AlleleCellLineAssociation> alleleCellLineAssociations;
  private List<AlleleImageAssociation> alleleImageAssociations;
  private List<AlleleOriginAssociation> alleleOriginAssociations;
  private List<AlleleGenerationMethodAssociation> alleleGenerationMethodAssociations;

}