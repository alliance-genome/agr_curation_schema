package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  A description of when and where gene products are observed to be present, including experimental details, supporting evidence, and curator notes.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExpressionAnnotation extends AuditedObject {

  private ExpressionExperiment belongsToExpressionExperiment;
  private TemporalContext whenExpressed;
  private AnatomicalSite whereExpressed;
  private String expressionQualifiers;
  private boolean negated;
  private boolean uncertain;
  private List<Figure> associatedWithFigure;
  private List<Note> relatedNotes;

}