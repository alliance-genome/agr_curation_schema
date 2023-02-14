# AlleleMutationTypeSlotAnnotation

None


```mermaid
 classDiagram
      SlotAnnotation <|-- AlleleMutationTypeSlotAnnotation
      
      AlleleMutationTypeSlotAnnotation : created_by
      AlleleMutationTypeSlotAnnotation : date_created
      AlleleMutationTypeSlotAnnotation : date_updated
      AlleleMutationTypeSlotAnnotation : db_date_created
      AlleleMutationTypeSlotAnnotation : db_date_updated
      AlleleMutationTypeSlotAnnotation : evidence
      AlleleMutationTypeSlotAnnotation : internal
      AlleleMutationTypeSlotAnnotation : mutation_types
      AlleleMutationTypeSlotAnnotation : obsolete
      AlleleMutationTypeSlotAnnotation : single_allele
      AlleleMutationTypeSlotAnnotation : updated_by
      

```



URI: [alliance:AlleleMutationTypeSlotAnnotation](http://alliancegenome.org/AlleleMutationTypeSlotAnnotation)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * [SlotAnnotation](SlotAnnotation.md)
        * **AlleleMutationTypeSlotAnnotation**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [created_by](created_by.md) | The individual that created the entity. |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [evidence](evidence.md) |  |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [mutation_types](mutation_types.md) | SO term for type of mutation |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [single_allele](single_allele.md) | None |
| [updated_by](updated_by.md) | The individual that last modified the entity. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:AlleleMutationTypeSlotAnnotation'] |
| native | ['alliance:AlleleMutationTypeSlotAnnotation'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AlleleMutationTypeSlotAnnotation
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/allele
is_a: SlotAnnotation
slots:
- single_allele
- mutation_types
slot_usage:
  single_allele:
    name: single_allele
    domain_of:
    - AlleleDatabaseStatusSlotAnnotation
    - AlleleFullNameSlotAnnotation
    - AlleleFunctionalImpactSlotAnnotation
    - AlleleGermlineTransmissionStatusSlotAnnotation
    - AlleleInheritanceModeSlotAnnotation
    - AlleleMolecularMutationSlotAnnotation
    - AlleleMutationTypeSlotAnnotation
    - AlleleNomenclatureEventSlotAnnotation
    - AlleleNoteSlotAnnotation
    - AlleleSecondaryIdSlotAnnotation
    - AlleleSymbolSlotAnnotation
    - AlleleSynonymSlotAnnotation
    - AffectedGenomicModelComponent
    required: true

```
</details>

### Induced

<details>
```yaml
name: AlleleMutationTypeSlotAnnotation
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/allele
is_a: SlotAnnotation
slot_usage:
  single_allele:
    name: single_allele
    domain_of:
    - AlleleDatabaseStatusSlotAnnotation
    - AlleleFullNameSlotAnnotation
    - AlleleFunctionalImpactSlotAnnotation
    - AlleleGermlineTransmissionStatusSlotAnnotation
    - AlleleInheritanceModeSlotAnnotation
    - AlleleMolecularMutationSlotAnnotation
    - AlleleMutationTypeSlotAnnotation
    - AlleleNomenclatureEventSlotAnnotation
    - AlleleNoteSlotAnnotation
    - AlleleSecondaryIdSlotAnnotation
    - AlleleSymbolSlotAnnotation
    - AlleleSynonymSlotAnnotation
    - AffectedGenomicModelComponent
    required: true
attributes:
  single_allele:
    name: single_allele
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/allele
    multivalued: false
    alias: single_allele
    owner: AlleleMutationTypeSlotAnnotation
    domain_of:
    - AlleleDatabaseStatusSlotAnnotation
    - AlleleFullNameSlotAnnotation
    - AlleleFunctionalImpactSlotAnnotation
    - AlleleGermlineTransmissionStatusSlotAnnotation
    - AlleleInheritanceModeSlotAnnotation
    - AlleleMolecularMutationSlotAnnotation
    - AlleleMutationTypeSlotAnnotation
    - AlleleNomenclatureEventSlotAnnotation
    - AlleleNoteSlotAnnotation
    - AlleleSecondaryIdSlotAnnotation
    - AlleleSymbolSlotAnnotation
    - AlleleSynonymSlotAnnotation
    - AffectedGenomicModelComponent
    range: Allele
    required: true
  mutation_types:
    name: mutation_types
    description: SO term for type of mutation
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/allele
    domain: AlleleMutationTypeSlotAnnotation
    multivalued: true
    alias: mutation_types
    owner: AlleleMutationTypeSlotAnnotation
    domain_of:
    - AlleleMutationTypeSlotAnnotation
    range: SOTerm
    required: true
  evidence:
    name: evidence
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/reference
    multivalued: true
    alias: evidence
    owner: AlleleMutationTypeSlotAnnotation
    domain_of:
    - AlleleGenerationMethodAssociation
    - Note
    - SlotAnnotation
    - Association
    range: InformationContentEntity
  created_by:
    name: created_by
    description: The individual that created the entity.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObject
    multivalued: false
    alias: created_by
    owner: AlleleMutationTypeSlotAnnotation
    domain_of:
    - AuditedObject
    range: Person
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
    owner: AlleleMutationTypeSlotAnnotation
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: datetime
  updated_by:
    name: updated_by
    description: The individual that last modified the entity.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObject
    multivalued: false
    alias: updated_by
    owner: AlleleMutationTypeSlotAnnotation
    domain_of:
    - AuditedObject
    range: Person
  date_updated:
    name: date_updated
    description: Date on which an entity was last modified.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    aliases:
    - date_last_modified
    alias: date_updated
    owner: AlleleMutationTypeSlotAnnotation
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
    owner: AlleleMutationTypeSlotAnnotation
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
    owner: AlleleMutationTypeSlotAnnotation
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
    owner: AlleleMutationTypeSlotAnnotation
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
    owner: AlleleMutationTypeSlotAnnotation
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>