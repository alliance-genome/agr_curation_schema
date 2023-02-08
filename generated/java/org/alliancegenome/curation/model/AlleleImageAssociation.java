package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  The relationship between an allele and an image.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleImageAssociation extends Association {

  private boolean primaryImage;

}