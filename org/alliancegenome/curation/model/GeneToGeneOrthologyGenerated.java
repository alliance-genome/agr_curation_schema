package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  Class that holds the properties necessary to record an orthology record from DIOPT
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneToGeneOrthologyGenerated extends GeneToGeneOrthology {

  private String isBestScore;
  private String isBestReverseScore;
  private String confidence;
  private String strictFilter;
  private String moderateFilter;

}