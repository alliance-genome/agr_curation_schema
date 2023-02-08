package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  An entity that is part of a genome (i.e. segment of the DNA molecule), is derived directly from the genome (i.e. RNA transcript molecule), or is derived indirectly from the genome (i.e. polypeptide or protein via RNA transcript translation).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GenomicEntity extends BiologicalEntity {

  private List<CrossReference> crossReferences;
  private List<String> secondaryIdentifiers;
  private List<GenomicLocationAssociation> genomicLocationAssociations;

}