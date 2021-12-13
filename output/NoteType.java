package None;

import java.util.List;
import lombok.*;

/**
  Describes the relation between a note and an object
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NoteType  {

  private String noteAssociation;
  private List<String> notes;

}