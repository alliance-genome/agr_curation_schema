package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  Placeholder.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Gene extends GenomicEntity {

  private List<GeneGenomicLocation> genomicLocations;
  private String symbol;
  private String geneSynopsis;
  private String geneSynopsisURL;
  private String type;
  private String automatedGeneDescription;

}