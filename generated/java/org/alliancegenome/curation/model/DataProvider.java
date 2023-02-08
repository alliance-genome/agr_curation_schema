package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class DataProvider extends AuditedObject {

  private Organization sourceOrganization;
  private CrossReference crossReference;

}