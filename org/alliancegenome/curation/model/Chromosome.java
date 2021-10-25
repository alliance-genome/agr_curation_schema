package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  The ID of the landmark used to establish the coordinate system for the current feature.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Chromosome  {

  private String curie;

}