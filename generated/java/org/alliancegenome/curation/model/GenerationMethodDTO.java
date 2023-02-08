package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class GenerationMethodDTO extends AuditedObjectDTO {

  private List<String> mutagenesisMethodNames;
  private String mutagenesisTarget;
  private String integrationMethodName;
  private String chemicalMutagenName;
  private String irradiationMutagenName;

}