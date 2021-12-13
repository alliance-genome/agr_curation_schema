package None;

import java.util.List;
import lombok.*;

/**
  None
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VariantGenomicLocation  {

  private Variant subject;
  private String predicate;
  private Chromosome object;
  private Chromosome hasAssembly;
  private String start;
  private String end;

}