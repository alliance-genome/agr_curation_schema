package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  An entity of biological origin that can be unambiguously attributed to a single species.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class BiologicalEntity extends AuditedObject {

  private String curie;
  private NCBITaxonTerm taxon;

}