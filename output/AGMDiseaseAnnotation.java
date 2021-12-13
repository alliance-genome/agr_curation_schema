package None;

import java.util.List;
import lombok.*;

/**
  None
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AGMDiseaseAnnotation extends DiseaseAnnotation {

  private Allele inferredAllele;
  private Gene inferredGene;

}