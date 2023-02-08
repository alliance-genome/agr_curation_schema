package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Allele that affects the model and its zygosity
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AffectedGenomicModelComponent extends AuditedObject {

  private Allele singleAllele;
  private String zygosity;

}