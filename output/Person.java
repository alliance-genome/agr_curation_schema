package None;

import java.util.List;
import lombok.*;

/**
  None
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Person extends Agent {

  private InformationContentEntity lastName;
  private InformationContentEntity firstName;
  private String orcid;

}