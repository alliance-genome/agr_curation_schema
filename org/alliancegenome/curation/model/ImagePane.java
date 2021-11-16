package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  Part of an Image that is relevant to some annotation. An annotation may reference many panes of an Image.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ImagePane  {

  private Image images;
  private String label;
  private Integer width;
  private Integer height;
  private Integer imageXOrigin;
  private Integer imageYOrigin;
  private Integer tableKey;
  private Person createdBy;
  private String creationDate;
  private Person modifiedBy;
  private String dateLastModified;

}