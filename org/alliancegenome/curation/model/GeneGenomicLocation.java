package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;


@Data
@EqualsAndHashCode(callSuper=false)
public class GeneGenomicLocation  {

  private Variant subject;
  private String predicate;
  private Chromosome object;
  private Chromosome hasAssembly;
  private String start;
  private String end;

}