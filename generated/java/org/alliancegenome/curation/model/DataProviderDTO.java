package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class DataProviderDTO extends AuditedObjectDTO {

  private String sourceOrganizationAbbreviation;
  private CrossReferenceDTO crossReferenceDto;

}