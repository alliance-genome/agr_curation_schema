package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  The set of files and metadata that constitute an image.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Image extends AuditedObject {

  private String curie;
  private Figure associatedWithFigure;
  private int width;
  private int height;
  private File imageFile;
  private File imageMediumFile;
  private File imageThumbnailFile;
  private Image croppedFrom;
  private Integer imageXOrigin;
  private Integer imageYOrigin;
  private boolean videoStill;
  private List<String> secondaryIdentifiers;

}