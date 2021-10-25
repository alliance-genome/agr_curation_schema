package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;


@Data
@EqualsAndHashCode(callSuper=false)
public class GenomicEntity extends BiologicalEntity {

  private String name;
  private List<Synonym> synonyms;
  private List<CrossReference> crossReferences;
  private List<String> secondaryIdentifiers;

}