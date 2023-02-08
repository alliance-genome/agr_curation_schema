package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  A DNA genomic entity from which one or more functional* RNA transcript molecules are transcribed, along with cis-regulatory elements responsible for regulating expression (transcription) of the gene. * A functional RNA molecule here can mean one that is directly responsible for the gene's function (e.g. catalysis, structure, etc.) or one that is translated to produce a functional polypeptide/protein. A pseudogene may be considered a gene under this definition, albeit no longer functional.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Gene extends GenomicEntity {

  private GeneSymbolSlotAnnotation geneSymbol;
  private GeneFullNameSlotAnnotation geneFullName;
  private GeneSystematicNameSlotAnnotation geneSystematicName;
  private List<GeneSynonymSlotAnnotation> geneSynonyms;
  private List<Note> relatedNotes;
  private SOTerm geneType;
  private List<SOTerm> geneTypesSecondary;
  private List<Laboratory> designatingLaboratories;
  private List<String> designatingPersons;
  private List<String> transSpliceLeaders;
  private List<String> contig;
  private List<String> anatomyFunction;
  private List<String> productBindsMatrix;
  private List<String> wbprocess;
  private boolean transposonOrigin;

}