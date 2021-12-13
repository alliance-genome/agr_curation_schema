package None;

import java.util.List;
import lombok.*;

/**
  None
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleDiseaseAnnotation extends DiseaseAnnotation {

  private Gene inferredGene;

}