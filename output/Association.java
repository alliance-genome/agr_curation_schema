package None;

import java.util.List;
import lombok.*;

/**
  A typed association between two entities, supported by evidence.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Association  {

  private String subject;
  private String predicate;
  private String object;
  private List<Reference> references;

}