package None;

import java.util.List;
import lombok.*;

/**
  None
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GenomicEntity extends BiologicalEntity {

  private String name;
  private List<Synonym> synonyms;
  private List<CrossReference> crossReferences;
  private List<String> secondaryIdentifiers;

}