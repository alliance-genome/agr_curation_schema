package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  The history of a gene
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneHistory extends AuditedObject {

  private List<String> currentStatus;
  private Integer currentVersion;
  private List<Gene> mergedInto;
  private List<Gene> acquiresMerge;
  private List<Gene> splitFrom;
  private List<Gene> splitInto;

}