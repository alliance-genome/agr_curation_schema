# TemporalContext

The developmental stage and/or age of the specimen in an annotation. Developmental_stage_stop is optional. Add an uncertainty flag here?


```mermaid
 classDiagram
      AuditedObject <|-- TemporalContext
      
      TemporalContext : age
      TemporalContext : created_by
      TemporalContext : date_created
      TemporalContext : date_updated
      TemporalContext : db_date_created
      TemporalContext : db_date_updated
      TemporalContext : developmental_stage_start
      TemporalContext : developmental_stage_stop
      TemporalContext : internal
      TemporalContext : obsolete
      TemporalContext : temporal_qualifiers
      TemporalContext : updated_by
      

```



URI: [alliance:TemporalContext](http://alliancegenome.org/TemporalContext)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * **TemporalContext**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [age](age.md) | The age at which an annotated event was observed. |
| [created_by](created_by.md) | The individual that created the entity. |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [developmental_stage_start](developmental_stage_start.md) | The beginning developmental stage at which an annotated event was observed. |
| [developmental_stage_stop](developmental_stage_stop.md) | The end developmental stage at which an annotated event was observed. |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [temporal_qualifiers](temporal_qualifiers.md) | Qualifiers of the stage or age in an annotation. |
| [updated_by](updated_by.md) | The individual that last modified the entity. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:TemporalContext'] |
| native | ['alliance:TemporalContext'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TemporalContext
description: The developmental stage and/or age of the specimen in an annotation.
  Developmental_stage_stop is optional. Add an uncertainty flag here?
from_schema: https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml
is_a: AuditedObject
slots:
- developmental_stage_start
- developmental_stage_stop
- age
- temporal_qualifiers

```
</details>

### Induced

<details>
```yaml
name: TemporalContext
description: The developmental stage and/or age of the specimen in an annotation.
  Developmental_stage_stop is optional. Add an uncertainty flag here?
from_schema: https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml
is_a: AuditedObject
attributes:
  developmental_stage_start:
    name: developmental_stage_start
    description: The beginning developmental stage at which an annotated event was
      observed.
    notes:
    - Currently, we limit this to a single stage, but we could consider allowing for
      stage ranges for a single annotation.
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml
    domain: TemporalContext
    multivalued: false
    alias: developmental_stage_start
    owner: TemporalContext
    domain_of:
    - TemporalContext
    range: StageTerm
  developmental_stage_stop:
    name: developmental_stage_stop
    description: The end developmental stage at which an annotated event was observed.
    notes:
    - Currently, we limit this to a single stage, but we could consider allowing for
      stage ranges for a single annotation.
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml
    domain: TemporalContext
    multivalued: false
    alias: developmental_stage_stop
    owner: TemporalContext
    domain_of:
    - TemporalContext
    range: StageTerm
  age:
    name: age
    description: The age at which an annotated event was observed.
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml
    domain: TemporalContext
    multivalued: false
    alias: age
    owner: TemporalContext
    domain_of:
    - TemporalContext
    range: string
  temporal_qualifiers:
    name: temporal_qualifiers
    description: Qualifiers of the stage or age in an annotation.
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml
    domain: TemporalContext
    alias: temporal_qualifiers
    owner: TemporalContext
    domain_of:
    - TemporalContext
    range: temporal_qualifier_set
  created_by:
    name: created_by
    description: The individual that created the entity.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObject
    multivalued: false
    alias: created_by
    owner: TemporalContext
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
    owner: TemporalContext
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
    owner: TemporalContext
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
    owner: TemporalContext
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
    owner: TemporalContext
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
    owner: TemporalContext
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
    owner: TemporalContext
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
    owner: TemporalContext
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>