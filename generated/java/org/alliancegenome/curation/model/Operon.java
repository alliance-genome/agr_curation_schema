package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  The DNA region of a group of adjacent genes whose transcription is coordinated on one or several mutually overlapping transcription units transcribed in the same direction and sharing at least one gene.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Operon extends BiologicalEntity {

  private List<Gene> genes;
  private Note relatedNote;

}