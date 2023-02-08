package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class IdentifiersRange  {

  private Identifier first;
  private Identifier last;

}