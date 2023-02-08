package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class FunctionalGeneSet extends BiologicalEntity {

  private List<Gene> genes;
  private Reference singleReference;

}