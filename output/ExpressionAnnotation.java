package None;

import java.util.List;
import lombok.*;

/**
  A description of when and where gene products are observed to be present, including experimental details, supporting evidence, and curator notes.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExpressionAnnotation  {

  private String curie;
  private Gene gene;
  private TemporalContext whenExpressed;
  private AnatomicalSite whereExpressed;
  private MMOTerm assay;
  private List<Reagent> reagents;
  private String expressionQualifiers;
  private String perturbedExpressionQualifiers;
  private Boolean perturbed;
  private Boolean negated;
  private Boolean uncertain;
  private List<BiologicalEntity> primaryGeneticEntities;
  private String whenExpressedNote;
  private String whereExpressedNote;
  private String expressionAnnotationNote;
  private Reference hasReference;
  private Figure hasFigure;
  private Integer tableKey;
  private Person producedBy;
  private String creationDate;
  private Person modifiedBy;
  private String dateLastModified;

}