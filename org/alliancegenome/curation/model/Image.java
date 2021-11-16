package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  The set of files and metadata that constitute an image.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Image  {

  private String curie;
  private Figure hasFigure;
  private Integer width;
  private Integer height;
  private File imageFile;
  private File imageMediumFile;
  private File imageThumbnailFile;
  private Image croppedFrom;
  private Integer imageXOrigin;
  private Integer imageYOrigin;
  private Boolean videoStill;
  private List<String> secondaryIdentifiers;
  private Integer tableKey;
  private Person createdBy;
  private String creationDate;
  private Person modifiedBy;
  private String dateLastModified;

}