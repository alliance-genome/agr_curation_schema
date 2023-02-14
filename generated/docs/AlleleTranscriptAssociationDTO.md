# AlleleTranscriptAssociationDTO

Association between an allele and a transcript


```mermaid
 classDiagram
      AlleleGenomicEntityAssociationDTO <|-- AlleleTranscriptAssociationDTO
      
      AlleleTranscriptAssociationDTO : allele_curie
      AlleleTranscriptAssociationDTO : created_by_curie
      AlleleTranscriptAssociationDTO : date_created
      AlleleTranscriptAssociationDTO : date_updated
      AlleleTranscriptAssociationDTO : db_date_created
      AlleleTranscriptAssociationDTO : db_date_updated
      AlleleTranscriptAssociationDTO : evidence_code_curie
      AlleleTranscriptAssociationDTO : evidence_curies
      AlleleTranscriptAssociationDTO : internal
      AlleleTranscriptAssociationDTO : note_dto
      AlleleTranscriptAssociationDTO : obsolete
      AlleleTranscriptAssociationDTO : predicate_name
      AlleleTranscriptAssociationDTO : transcript_curie
      AlleleTranscriptAssociationDTO : updated_by_curie
      

```



URI: [alliance:AlleleTranscriptAssociationDTO](http://alliancegenome.org/AlleleTranscriptAssociationDTO)


## Parent Classes

* [AuditedObjectDTO](AuditedObjectDTO.md)
    * [AlleleGenomicEntityAssociationDTO](AlleleGenomicEntityAssociationDTO.md)
        * **AlleleTranscriptAssociationDTO**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [allele_curie](allele_curie.md) | None |
| [created_by_curie](created_by_curie.md) | Curie of the Person object representing the individual that created the entity |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [evidence_code_curie](evidence_code_curie.md) | Curie of ECOTerm |
| [evidence_curies](evidence_curies.md) | Curies of InformationContentEntity objects given as evidence |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [note_dto](note_dto.md) | None |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [predicate_name](predicate_name.md) | Name of VocabularyTerm representing predicate of an Association |
| [transcript_curie](transcript_curie.md) | None |
| [updated_by_curie](updated_by_curie.md) | Curie of the Person object representing the individual that updated the entity |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:AlleleTranscriptAssociationDTO'] |
| native | ['alliance:AlleleTranscriptAssociationDTO'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AlleleTranscriptAssociationDTO
description: Association between an allele and a transcript
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/alleleDTO
is_a: AlleleGenomicEntityAssociationDTO
slots:
- transcript_curie

```
</details>

### Induced

<details>
```yaml
name: AlleleTranscriptAssociationDTO
description: Association between an allele and a transcript
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/alleleDTO
is_a: AlleleGenomicEntityAssociationDTO
attributes:
  transcript_curie:
    name: transcript_curie
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: transcript_curie
    owner: AlleleTranscriptAssociationDTO
    domain_of:
    - AlleleTranscriptAssociationDTO
    range: string
    required: true
  allele_curie:
    name: allele_curie
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/alleleDTO
    alias: allele_curie
    owner: AlleleTranscriptAssociationDTO
    domain_of:
    - AlleleDiseaseAnnotationDTO
    - AlleleCellLineAssociationDTO
    - AlleleGenerationMethodAssociationDTO
    - AlleleGenomicEntityAssociationDTO
    - AlleleImageAssociationDTO
    - AlleleOriginAssociationDTO
    - AffectedGenomicModelComponentDTO
    range: string
    required: true
  predicate_name:
    name: predicate_name
    description: Name of VocabularyTerm representing predicate of an Association
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: predicate_name
    owner: AlleleTranscriptAssociationDTO
    domain_of:
    - AlleleCellLineAssociationDTO
    - AlleleGenerationMethodAssociationDTO
    - AlleleGenomicEntityAssociationDTO
    - AlleleImageAssociationDTO
    - AlleleOriginAssociationDTO
    - GenomicLocationAssociationDTO
    range: string
    required: true
  evidence_curies:
    name: evidence_curies
    description: Curies of InformationContentEntity objects given as evidence
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/reference
    multivalued: true
    alias: evidence_curies
    owner: AlleleTranscriptAssociationDTO
    domain_of:
    - DiseaseAnnotationDTO
    - AlleleCellLineAssociationDTO
    - AlleleGenerationMethodAssociationDTO
    - AlleleGenomicEntityAssociationDTO
    - AlleleImageAssociationDTO
    - AlleleOriginAssociationDTO
    - NoteDTO
    - SlotAnnotationDTO
    - GenomicLocationAssociationDTO
    range: string
    required: true
  evidence_code_curie:
    name: evidence_code_curie
    description: Curie of ECOTerm
    from_schema: https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml
    alias: evidence_code_curie
    owner: AlleleTranscriptAssociationDTO
    domain_of:
    - AlleleGenomicEntityAssociationDTO
    range: string
  note_dto:
    name: note_dto
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: note_dto
    owner: AlleleTranscriptAssociationDTO
    domain_of:
    - AlleleNoteSlotAnnotationDTO
    - AlleleGenomicEntityAssociationDTO
    range: NoteDTO
    inlined: true
  created_by_curie:
    name: created_by_curie
    description: Curie of the Person object representing the individual that created
      the entity
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObjectDTO
    alias: created_by_curie
    owner: AlleleTranscriptAssociationDTO
    domain_of:
    - AuditedObjectDTO
    range: string
  date_created:
    name: date_created
    description: The date on which an entity was created. This can be applied to nodes
      or edges.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    aliases:
    - creation_date
    exact_mappings:
    - dct:createdOn
    - WIKIDATA_PROPERTY:P577
    alias: date_created
    owner: AlleleTranscriptAssociationDTO
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: datetime
  updated_by_curie:
    name: updated_by_curie
    description: Curie of the Person object representing the individual that updated
      the entity
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObjectDTO
    alias: updated_by_curie
    owner: AlleleTranscriptAssociationDTO
    domain_of:
    - AuditedObjectDTO
    range: string
  date_updated:
    name: date_updated
    description: Date on which an entity was last modified.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    aliases:
    - date_last_modified
    alias: date_updated
    owner: AlleleTranscriptAssociationDTO
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: datetime
  db_date_created:
    name: db_date_created
    description: The date on which an entity was created in the Alliance database.  This
      is disinct from date_created, which represents the date when the entity was
      originally created (i.e. at the MOD for imported data).
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: db_date_created
    owner: AlleleTranscriptAssociationDTO
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: datetime
  db_date_updated:
    name: db_date_updated
    description: Date on which an entity was last modified in the Alliance database.  This
      is disinct from date_updated, which represents the date when the entity was
      last modified and may predate import into the Alliance database.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: db_date_updated
    owner: AlleleTranscriptAssociationDTO
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: datetime
  internal:
    name: internal
    description: Classifies the entity as private (for internal use) or not (for public
      use).
    notes:
    - Default value is true.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: internal
    owner: AlleleTranscriptAssociationDTO
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean
    required: true
  obsolete:
    name: obsolete
    description: Entity is no longer current.
    notes:
    - Obsolete entities are preserved in the database for posterity but should not
      be publicly displayed.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: obsolete
    owner: AlleleTranscriptAssociationDTO
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>