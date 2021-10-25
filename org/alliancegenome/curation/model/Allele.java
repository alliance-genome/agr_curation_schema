package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  One of multiple possible forms of a functional genomic element (most often described as a locus or gene), differing from the reference DNA sequence.  The genomic element can be endogenous or constructed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Allele extends GenomicEntity {

  private String symbol;
  private List<BiologicalEntity> affectedEntities;
  private Construct containsConstruct;
  private MolecularMutation molecularMutation;
  private String functionalImpact;
  private String generationMethod;
  private List<ReferenceType> associatedReferences;
  private NoteType associatedNotes;
  private String germlineTransmissionStatus;
  private CellLine parentCellLine;
  private List<CellLine> mutantCellLines;
  private List<CellLine> embryonicStemCellLines;
  private Image images;
  private List<AffectedGenomicModel> origins;
  private String databaseStatus;
  private String inheritenceMode;
  private String inCollection;
  private String transposonInsertion;
  private String aberration;
  private Boolean isExtinct;

}