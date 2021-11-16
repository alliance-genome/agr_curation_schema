package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  A set of VocabularyTerm objects.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Vocabulary  {

  private String name;
  private String vocabularyDescription;
  private Boolean isObsolete;
  private List<VocabularyTerm> memberTerms;
  private Integer tableKey;
  private Person createdBy;
  private String creationDate;
  private Person modifiedBy;
  private String dateLastModified;

}