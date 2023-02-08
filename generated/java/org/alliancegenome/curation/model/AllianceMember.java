package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  An organization that is a member of the Alliance of Genome Resources.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AllianceMember extends Organization {

  private int allianceMemberId;

}