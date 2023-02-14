# CrossReferenceDTO

None


```mermaid
 classDiagram
      AuditedObjectDTO <|-- CrossReferenceDTO
      
      CrossReferenceDTO : created_by_curie
      CrossReferenceDTO : date_created
      CrossReferenceDTO : date_updated
      CrossReferenceDTO : db_date_created
      CrossReferenceDTO : db_date_updated
      CrossReferenceDTO : display_name
      CrossReferenceDTO : internal
      CrossReferenceDTO : obsolete
      CrossReferenceDTO : page_area
      CrossReferenceDTO : prefix
      CrossReferenceDTO : referenced_curie
      CrossReferenceDTO : updated_by_curie
      

```



URI: [alliance:CrossReferenceDTO](http://alliancegenome.org/CrossReferenceDTO)


## Parent Classes

* [AuditedObjectDTO](AuditedObjectDTO.md)
    * **CrossReferenceDTO**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [created_by_curie](created_by_curie.md) | Curie of the Person object representing the individual that created the entity |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [display_name](display_name.md) | None |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [page_area](page_area.md) | None |
| [prefix](prefix.md) | Denormalization to help with classifying types of crossReferences, distinguishing DOIs from PMC ids, etc. |
| [referenced_curie](referenced_curie.md) | Curie of the thing being referenced in a CrossReference |
| [updated_by_curie](updated_by_curie.md) | Curie of the Person object representing the individual that updated the entity |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:CrossReferenceDTO'] |
| native | ['alliance:CrossReferenceDTO'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CrossReferenceDTO
from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
is_a: AuditedObjectDTO
slots:
- referenced_curie
- page_area
- display_name
- prefix
slot_usage:
  prefix:
    name: prefix
    domain_of:
    - CrossReferenceDTO
    - ExternalDatabaseLink
    - ResourceDescriptor
    required: true

```
</details>

### Induced

<details>
```yaml
name: CrossReferenceDTO
from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
is_a: AuditedObjectDTO
slot_usage:
  prefix:
    name: prefix
    domain_of:
    - CrossReferenceDTO
    - ExternalDatabaseLink
    - ResourceDescriptor
    required: true
attributes:
  referenced_curie:
    name: referenced_curie
    description: Curie of the thing being referenced in a CrossReference
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: referenced_curie
    owner: CrossReferenceDTO
    domain_of:
    - CrossReference
    - CrossReferenceDTO
    range: uriorcurie
    required: true
  page_area:
    name: page_area
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    alias: page_area
    owner: CrossReferenceDTO
    domain_of:
    - CrossReferenceDTO
    range: string
    required: true
  display_name:
    name: display_name
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    alias: display_name
    owner: CrossReferenceDTO
    domain_of:
    - CrossReference
    - CrossReferenceDTO
    range: string
    required: true
  prefix:
    name: prefix
    description: Denormalization to help with classifying types of crossReferences,
      distinguishing DOIs from PMC ids, etc.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    alias: prefix
    owner: CrossReferenceDTO
    domain_of:
    - CrossReferenceDTO
    - ExternalDatabaseLink
    - ResourceDescriptor
    range: string
    required: true
  created_by_curie:
    name: created_by_curie
    description: Curie of the Person object representing the individual that created
      the entity
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObjectDTO
    alias: created_by_curie
    owner: CrossReferenceDTO
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
    owner: CrossReferenceDTO
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
    owner: CrossReferenceDTO
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
    owner: CrossReferenceDTO
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
    owner: CrossReferenceDTO
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
    owner: CrossReferenceDTO
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
    owner: CrossReferenceDTO
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
    owner: CrossReferenceDTO
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>