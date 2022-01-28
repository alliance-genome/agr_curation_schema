package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;


@Data
@EqualsAndHashCode(callSuper=false)
public class Ingest  {

  private List<Allele> alleleIngestSet;
  private List<AlleleDiseaseAnnotation> diseaseAlleleIngestSet;

}