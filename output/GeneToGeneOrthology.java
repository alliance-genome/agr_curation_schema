package None;

import java.util.List;
import lombok.*;

/**
  
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneToGeneOrthology  {

  private Gene geneSubject;
  private String predicate;
  private Gene geneObject;

}