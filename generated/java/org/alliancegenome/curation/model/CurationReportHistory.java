package org.alliancegenome.curation.model;

import java.util.List;
import lombok.*;






/**
  Object used to describe the indiviual run of this curation report
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CurationReportHistory extends AuditedObject {

  private CurationReport curationReport;
  private String curationReportTimestamp;
  private String pdfFilePath;
  private String xlsFilePath;
  private String htmlFilePath;
  private String curationReportStatus;

}