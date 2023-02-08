package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class NameSlotAnnotationDTO extends SlotAnnotationDTO {

  private String nameTypeName;
  private String formatText;
  private String displayText;
  private String synonymUrl;
  private String synonymScopeName;

}