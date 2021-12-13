package None;

import java.util.List;
import lombok.*;

/**
  
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Construct extends GenomicEntity {

  private List<ConstructComponent> constructComponents;

}