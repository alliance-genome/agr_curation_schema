package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  The relationship between an allele and a variant is many to many. An Allele may have many variants and a variant can be present in many alleles.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlleleVariantAssociation extends AlleleGenomicEntityAssociation {


}