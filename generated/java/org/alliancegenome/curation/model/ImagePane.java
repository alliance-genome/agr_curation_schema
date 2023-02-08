package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Part of an Image that is relevant to some annotation. An annotation may reference many panes of an Image.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ImagePane extends AuditedObject {

  private Image fromImage;
  private String label;
  private int width;
  private int height;
  private Integer imageXOrigin;
  private Integer imageYOrigin;

}