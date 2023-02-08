package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class GeneToGeneAssociation extends Association {


}