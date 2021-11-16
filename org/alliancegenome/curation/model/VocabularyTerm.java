package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  A concept or class in a simple vocabulary.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VocabularyTerm  {

  private String name;
  private String definition;
  private Boolean isObsolete;
  private List<String> textSynonyms;
  private Integer tableKey;
  private Person createdBy;
  private String creationDate;
  private Person modifiedBy;
  private String dateLastModified;

}