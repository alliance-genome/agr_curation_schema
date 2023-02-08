package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  WB specific. A gene class is a set of genes which share nomenclature, belonging to the same gene class.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeneNomenclatureSet extends AuditedObject {

  private List<Gene> genes;
  private String curie;
  private Laboratory designatingLaboratory;
  private List<Gene> oldMembers;
  private List<String> synonyms;
  private Note relatedNote;

}