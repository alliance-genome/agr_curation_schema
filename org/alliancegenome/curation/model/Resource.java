package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;


@Data
@EqualsAndHashCode(callSuper=false)
public class Resource extends InformationContentEntity {

  private String title;
  private String isoAbbreviation;
  private String medlineAbbreviation;
  private String copyrightDate;
  private String printIssn;
  private String onlineIssn;
  private InformationContentEntity publisher;
  private String volumes;
  private String summary;
  private List<Synonym> synonyms;
  private List<AuthorReference> authors;
  private List<AuthorReference> editors;

}