package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AffectedGenomicModelComponentDTO extends AuditedObjectDTO {

  private String alleleCurie;
  private String zygosityCurie;

}