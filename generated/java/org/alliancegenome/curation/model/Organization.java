package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  An organization that provides information and/or materials to the Alliance. This includes Alliance member organizations (see AllianceMember subclass).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Organization extends Agent {

  private String abbreviation;
  private String fullName;
  private String shortName;
  private ResourceDescriptorPage homepageResourceDescriptorPage;

}