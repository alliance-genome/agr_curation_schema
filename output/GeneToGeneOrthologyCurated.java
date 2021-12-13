package None;

import java.util.List;
import lombok.*;

/**
  Class that holds the properties necessary to store a curated orthology record.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneToGeneOrthologyCurated extends GeneToGeneOrthology {

  private Reference hasReference;
  private String evidenceCode;

}