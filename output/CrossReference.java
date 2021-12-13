package None;

import java.util.List;
import lombok.*;

/**
  None
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CrossReference extends InformationContentEntity {

  private List<String> pageAreas;
  private String displayName;
  private String prefix;

}