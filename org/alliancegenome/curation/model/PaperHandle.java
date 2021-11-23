package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;

/**
  A pairing of a reference and a free text string that allows an object to have a reference-specific alias (or handle). For example, used for experimental conditions from ZFIN to label (in a reference-specific manner) individual experimental conditions when curating a particular reference.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PaperHandle  {

  private Reference reference;
  private String handle;

}