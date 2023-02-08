package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class Reference extends InformationContentEntity {

  private String abstract;
  private List<AuthorReference> authors;
  private String category;
  private List<String> dateArrivedInPubmed;
  private String dateLastModifiedInPubmed;
  private String datePublished;
  private String issueName;
  private List<String> keywords;
  private String language;
  private String mergedIntoId;
  private boolean openAccess;
  private String pageRange;
  private String plainLanguageAbstract;
  private String publisher;
  private List<String> pubmedAbstractLanguages;
  private String pubmedPublicationStatus;
  private List<String> pubmedType;
  private int referenceId;
  private Integer resourceId;
  private String title;
  private String volume;

}