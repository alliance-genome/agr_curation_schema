package None;

import java.util.List;
import lombok.*;

/**
  An annotation asserting an association between a biological entity and a phenotype supported by evidence.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PhenotypeAnnotationCurated extends Association {

  private String curie;
  private Phenotype phenotypeTerm;
  private String dateAssigned;
  private Integer tableKey;
  private Person producedBy;
  private String creationDate;
  private Person modifiedBy;
  private String dateLastModified;

}