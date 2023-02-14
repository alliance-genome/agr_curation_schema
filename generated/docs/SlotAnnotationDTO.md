# SlotAnnotationDTO

None


```mermaid
 classDiagram
      AuditedObjectDTO <|-- SlotAnnotationDTO
      
      SlotAnnotationDTO : created_by_curie
      SlotAnnotationDTO : date_created
      SlotAnnotationDTO : date_updated
      SlotAnnotationDTO : db_date_created
      SlotAnnotationDTO : db_date_updated
      SlotAnnotationDTO : evidence_curies
      SlotAnnotationDTO : internal
      SlotAnnotationDTO : obsolete
      SlotAnnotationDTO : updated_by_curie
      

```



URI: [alliance:SlotAnnotationDTO](http://alliancegenome.org/SlotAnnotationDTO)


## Parent Classes

* [AuditedObjectDTO](AuditedObjectDTO.md)
    * **SlotAnnotationDTO**
        * [AlleleDatabaseStatusSlotAnnotationDTO](AlleleDatabaseStatusSlotAnnotationDTO.md)
        * [AlleleFunctionalImpactSlotAnnotationDTO](AlleleFunctionalImpactSlotAnnotationDTO.md)
        * [AlleleGermlineTransmissionStatusSlotAnnotationDTO](AlleleGermlineTransmissionStatusSlotAnnotationDTO.md)
        * [AlleleInheritanceModeSlotAnnotationDTO](AlleleInheritanceModeSlotAnnotationDTO.md)
        * [AlleleMolecularMutationSlotAnnotationDTO](AlleleMolecularMutationSlotAnnotationDTO.md)
        * [AlleleMutationTypeSlotAnnotationDTO](AlleleMutationTypeSlotAnnotationDTO.md)
        * [AlleleNomenclatureEventSlotAnnotationDTO](AlleleNomenclatureEventSlotAnnotationDTO.md)
        * [AlleleNoteSlotAnnotationDTO](AlleleNoteSlotAnnotationDTO.md)
        * [AlleleSecondaryIdSlotAnnotationDTO](AlleleSecondaryIdSlotAnnotationDTO.md)
        * [NameSlotAnnotationDTO](NameSlotAnnotationDTO.md)





## Children

* [AuditedObjectDTO](AuditedObjectDTO.md)
    * **SlotAnnotationDTO**
        * [AlleleDatabaseStatusSlotAnnotationDTO](AlleleDatabaseStatusSlotAnnotationDTO.md)
        * [AlleleFunctionalImpactSlotAnnotationDTO](AlleleFunctionalImpactSlotAnnotationDTO.md)
        * [AlleleGermlineTransmissionStatusSlotAnnotationDTO](AlleleGermlineTransmissionStatusSlotAnnotationDTO.md)
        * [AlleleInheritanceModeSlotAnnotationDTO](AlleleInheritanceModeSlotAnnotationDTO.md)
        * [AlleleMolecularMutationSlotAnnotationDTO](AlleleMolecularMutationSlotAnnotationDTO.md)
        * [AlleleMutationTypeSlotAnnotationDTO](AlleleMutationTypeSlotAnnotationDTO.md)
        * [AlleleNomenclatureEventSlotAnnotationDTO](AlleleNomenclatureEventSlotAnnotationDTO.md)
        * [AlleleNoteSlotAnnotationDTO](AlleleNoteSlotAnnotationDTO.md)
        * [AlleleSecondaryIdSlotAnnotationDTO](AlleleSecondaryIdSlotAnnotationDTO.md)
        * [NameSlotAnnotationDTO](NameSlotAnnotationDTO.md)



## Slots

| Name | Description  |
| ---  | ---  |
| [created_by_curie](created_by_curie.md) | Curie of the Person object representing the individual that created the entity |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [evidence_curies](evidence_curies.md) | Curies of InformationContentEntity objects given as evidence |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [updated_by_curie](updated_by_curie.md) | Curie of the Person object representing the individual that updated the entity |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:SlotAnnotationDTO'] |
| native | ['alliance:SlotAnnotationDTO'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SlotAnnotationDTO
from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
is_a: AuditedObjectDTO
slots:
- evidence_curies

```
</details>

### Induced

<details>
```yaml
name: SlotAnnotationDTO
from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
is_a: AuditedObjectDTO
attributes:
  evidence_curies:
    name: evidence_curies
    description: Curies of InformationContentEntity objects given as evidence
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/reference
    multivalued: true
    alias: evidence_curies
    owner: SlotAnnotationDTO
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
  created_by_curie:
    name: created_by_curie
    description: Curie of the Person object representing the individual that created
      the entity
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObjectDTO
    alias: created_by_curie
    owner: SlotAnnotationDTO
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
    owner: SlotAnnotationDTO
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
    owner: SlotAnnotationDTO
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
    owner: SlotAnnotationDTO
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
    owner: SlotAnnotationDTO
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
    owner: SlotAnnotationDTO
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
    owner: SlotAnnotationDTO
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
    owner: SlotAnnotationDTO
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>