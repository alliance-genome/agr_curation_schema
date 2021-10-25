package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  Description of the DNA changes with unknown precise genomic location
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MolecularMutation  {

  private SOTerm mutationType;
  private String mutationDescription;

}