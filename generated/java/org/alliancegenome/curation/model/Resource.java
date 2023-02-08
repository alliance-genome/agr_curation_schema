package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class Resource extends AuditedObject {

  private String curie;
  private String title;
  private String isoAbbreviation;
  private String medlineAbbreviation;
  private String copyrightDate;
  private String printIssn;
  private String onlineIssn;
  private String publisher;
  private String volume;
  private String summary;
  private List<String> synonyms;
  private List<AuthorReference> authors;
  private List<AuthorReference> editors;

}