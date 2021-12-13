package None;

import java.util.List;
import lombok.*;

/**
  None
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneDiseaseAnnotation extends DiseaseAnnotation {

  private AffectedGenomicModel sgdStrainBackground;

}