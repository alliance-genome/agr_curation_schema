package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;


@Data
@EqualsAndHashCode(callSuper=false)
public class ConstructComponent extends GenomicEntity {

  private String componentRelation;

}