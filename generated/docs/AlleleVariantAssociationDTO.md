# AlleleVariantAssociationDTO

The relationship between an allele and a variant is many to many. An Allele may have many variants and a variant can be present in many alleles.


```mermaid
 classDiagram
      AlleleGenomicEntityAssociationDTO <|-- AlleleVariantAssociationDTO
      
      AlleleVariantAssociationDTO : allele_curie
      AlleleVariantAssociationDTO : created_by_curie
      AlleleVariantAssociationDTO : date_created
      AlleleVariantAssociationDTO : date_updated
      AlleleVariantAssociationDTO : db_date_created
      AlleleVariantAssociationDTO : db_date_updated
      AlleleVariantAssociationDTO : evidence_code_curie
      AlleleVariantAssociationDTO : evidence_curies
      AlleleVariantAssociationDTO : internal
      AlleleVariantAssociationDTO : note_dto
      AlleleVariantAssociationDTO : obsolete
      AlleleVariantAssociationDTO : predicate_name
      AlleleVariantAssociationDTO : updated_by_curie
      AlleleVariantAssociationDTO : variant_curie
      

```



URI: [alliance:AlleleVariantAssociationDTO](http://alliancegenome.org/AlleleVariantAssociationDTO)


## Parent Classes

* [AuditedObjectDTO](AuditedObjectDTO.md)
    * [AlleleGenomicEntityAssociationDTO](AlleleGenomicEntityAssociationDTO.md)
        * **AlleleVariantAssociationDTO**




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
| [updated_by_curie](updated_by_curie.md) | Curie of the Person object representing the individual that updated the entity |
| [variant_curie](variant_curie.md) | None |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:AlleleVariantAssociationDTO'] |
| native | ['alliance:AlleleVariantAssociationDTO'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AlleleVariantAssociationDTO
description: The relationship between an allele and a variant is many to many. An
  Allele may have many variants and a variant can be present in many alleles.
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/alleleDTO
is_a: AlleleGenomicEntityAssociationDTO
slots:
- variant_curie

```
</details>

### Induced

<details>
```yaml
name: AlleleVariantAssociationDTO
description: The relationship between an allele and a variant is many to many. An
  Allele may have many variants and a variant can be present in many alleles.
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/alleleDTO
is_a: AlleleGenomicEntityAssociationDTO
attributes:
  variant_curie:
    name: variant_curie
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variation
    alias: variant_curie
    owner: AlleleVariantAssociationDTO
    domain_of:
    - AlleleVariantAssociationDTO
    range: string
  allele_curie:
    name: allele_curie
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/alleleDTO
    alias: allele_curie
    owner: AlleleVariantAssociationDTO
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
    owner: AlleleVariantAssociationDTO
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
    owner: AlleleVariantAssociationDTO
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
    owner: AlleleVariantAssociationDTO
    domain_of:
    - AlleleGenomicEntityAssociationDTO
    range: string
  note_dto:
    name: note_dto
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: note_dto
    owner: AlleleVariantAssociationDTO
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
    owner: AlleleVariantAssociationDTO
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
    owner: AlleleVariantAssociationDTO
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
    owner: AlleleVariantAssociationDTO
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
    owner: AlleleVariantAssociationDTO
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
    owner: AlleleVariantAssociationDTO
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
    owner: AlleleVariantAssociationDTO
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
    owner: AlleleVariantAssociationDTO
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
    owner: AlleleVariantAssociationDTO
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>