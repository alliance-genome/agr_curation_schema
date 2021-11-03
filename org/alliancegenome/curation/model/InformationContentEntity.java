package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  a piece of information that typically describes some topic of discourse or is used as support. Precedence of identifiers for references is as follows: PMID if available; DOI if not; actual alternate CURIE otherwise.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstractclass InformationContentEntity  {

  private String curie;

}