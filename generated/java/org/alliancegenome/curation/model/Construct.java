package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class Construct extends GenomicEntity {

  private List<GenomicEntity> constructComponents;
  private List<Reference> references;

}