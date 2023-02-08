package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Defined by the gene of interest, the specimen, the assay, the reagents (Antibody, Probe), and the reference. It groups ExpressionAnnotations.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExpressionExperiment extends AuditedObject {

  private String curie;
  private Reference singleReference;
  private BiologicalEntity biologicalEntityAssayed;
  private MMOTerm assayUsed;
  private List<Reagent> reagentsUsed;
  private AffectedGenomicModel specimenGenomicModel;
  private List<Allele> specimenAlleles;
  private List<ConditionRelation> conditionRelations;
  private List<Note> relatedNotes;

}