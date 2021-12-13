package None;

import java.util.List;
import lombok.*;

/**
  None
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Reference extends InformationContentEntity {

  private String title;
  private String allianceCategory;
  private String datePublished;
  private String yearPublished;
  private String monthPublished;
  private String dayPublished;
  private String dateArrivedInPubMed;
  private String dateLastModifiedInPubMed;
  private String volume;
  private List<String> pages;
  private String abstract;
  private String citation;
  private String pubMedType;
  private String issueName;
  private String issueDate;
  private List<String> modReferenceTypes;
  private List<AuthorReference> authors;
  private List<String> tags;
  private String topics;
  private List<CrossReference> crossReferences;
  private InformationContentEntity publisher;
  private List<String> keywords;
  private Resource fromResource;

}