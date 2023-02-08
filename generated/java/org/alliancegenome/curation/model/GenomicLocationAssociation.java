package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class GenomicLocationAssociation extends Association {

  private Assembly hasAssembly;
  private Integer start;
  private Integer end;

}