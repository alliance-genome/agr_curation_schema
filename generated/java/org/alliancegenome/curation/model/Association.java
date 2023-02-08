package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  A typed association between two entities, supported by evidence.  Associations have three base slots: subject, object, and predicate, but they can have any number of additional attributes that help qualify the relationship between the subject and the object.  The subject is the curie (or identifier) of the class that is the subject of the association, and likewise the object is the curie (or identifier of the class that is the object. The relationship between subject and object is defined by the predicate slot (which can also be constrained using the range of the predicate).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Association extends AuditedObject {

  private String subject;
  private String predicate;
  private String object;
  private List<InformationContentEntity> evidence;

}