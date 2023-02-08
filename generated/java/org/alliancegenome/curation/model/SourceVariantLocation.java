package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Links a paper to the variant locations described in that paper
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SourceVariantLocation extends AuditedObject {

  private List<VariantLocation> variantLocations;
  private Reference singleReference;

}