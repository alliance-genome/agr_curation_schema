package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  An interaction between two genes or gene products; this may be a physical molecular interaction between gene products (e.g. protein-protein interactions), or may be a genetic interaction between genes (e.g. phenotypic suppression)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class GeneInteraction extends GeneToGeneAssociation {

  private String curie;
  private List<CrossReference> crossReferences;
  private String interactionDataProvider;
  private String interactionType;
  private List<String> interactorARole;
  private List<String> interactorBRole;
  private String interactorAType;
  private String interactorBType;

}