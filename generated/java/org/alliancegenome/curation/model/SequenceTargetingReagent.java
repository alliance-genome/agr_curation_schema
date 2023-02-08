package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class SequenceTargetingReagent extends GenomicEntity {

  private List<Reference> references;

}