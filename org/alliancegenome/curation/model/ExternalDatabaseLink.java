package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  Base relation that holds the identifier prefix, base url and url suffix to help in generating URLs in crossReferences.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExternalDatabaseLink  {

  private String dbkey;
  private String prefix;
  private String urlPrefix;
  private String urlSuffix;
  private String prefixPage;
  private String prefixOrder;

}