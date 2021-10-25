package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  A material entity used in experiments.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Reagent  {

  private List<Agent> generatedBy;
  private List<Agent> manufacturedBy;

}