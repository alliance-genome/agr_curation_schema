package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class ProteinComplex extends BiologicalEntity {

  private List<Protein> proteins;

}