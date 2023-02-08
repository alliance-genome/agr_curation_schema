package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleGenerationMethodAssociation extends Association {

  private AffectedGenomicModel mutationTargetStrain;

}