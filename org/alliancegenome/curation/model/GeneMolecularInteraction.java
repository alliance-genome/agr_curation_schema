package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  A physical molecular interaction between gene products (e.g. protein-protein interactions or protein-RNA interactions) or between genes and DNA-binding factors (e.g. protein-DNA interactions)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneMolecularInteraction extends GeneInteraction {

  private String aggregationDatabase;
  private String detectionMethod;

}