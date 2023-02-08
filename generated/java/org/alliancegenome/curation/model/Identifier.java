package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class Identifier  {

  private Integer counter;
  private String subdomainCode;
  private String subdomainName;
  private String curie;

}