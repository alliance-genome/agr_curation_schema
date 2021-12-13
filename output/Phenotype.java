package None;

import java.util.List;
import lombok.*;

/**
  A characteristic of an organism. This may or may not be expressed as a difference in comparison to a reference organism.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Phenotype  {

  private String curie;
  private String name;

}