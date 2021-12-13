package None;

import java.util.List;
import lombok.*;

/**
  Some entity for which changes are tracked, including date/time of change and the agent responsible for the change.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AuditedObject  {

  private Integer tableKey;
  private Person producedBy;
  private String creationDate;
  private Person modifiedBy;
  private String dateLastModified;

}