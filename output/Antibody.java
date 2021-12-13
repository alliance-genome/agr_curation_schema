package None;

import java.util.List;
import lombok.*;

/**
  Immunoglobulin proteins that bind specific molecule(s). Can be used experimentally for the purposes of detection or purification.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Antibody extends BiologicalEntity {

  private String name;
  private String antigenTaxon;
  private String clonality;
  private String heavyChainIsotype;
  private String lightChainIsotype;
  private List<Gene> antibodyTargetGenes;
  private List<CrossReference> crossReferences;
  private List<String> secondaryIdentifiers;
  private List<Reference> references;
  private Reference originalReference;
  private List<Agent> generatedBy;
  private List<Agent> manufacturedBy;

}