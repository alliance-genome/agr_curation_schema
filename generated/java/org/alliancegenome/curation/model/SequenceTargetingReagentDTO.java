package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class SequenceTargetingReagentDTO extends GenomicEntityDTO {

  private List<String> referenceCuries;

}