# AnatomicalSite

The developmental stage and/or age of the specimen in an annotation.


```mermaid
 classDiagram
      AuditedObject <|-- AnatomicalSite
      
      AnatomicalSite : anatomical_structure
      AnatomicalSite : anatomical_substructure
      AnatomicalSite : cellular_component
      AnatomicalSite : created_by
      AnatomicalSite : date_created
      AnatomicalSite : date_updated
      AnatomicalSite : db_date_created
      AnatomicalSite : db_date_updated
      AnatomicalSite : internal
      AnatomicalSite : obsolete
      AnatomicalSite : spatial_qualifiers
      AnatomicalSite : updated_by
      

```



URI: [alliance:AnatomicalSite](http://alliancegenome.org/AnatomicalSite)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * **AnatomicalSite**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [anatomical_structure](anatomical_structure.md) | None |
| [anatomical_substructure](anatomical_substructure.md) | None |
| [cellular_component](cellular_component.md) | None |
| [created_by](created_by.md) | The individual that created the entity. |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [spatial_qualifiers](spatial_qualifiers.md) | Qualifiers that describe the spatial characteristics of an event. |
| [updated_by](updated_by.md) | The individual that last modified the entity. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:AnatomicalSite'] |
| native | ['alliance:AnatomicalSite'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnatomicalSite
description: The developmental stage and/or age of the specimen in an annotation.
from_schema: https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml
is_a: AuditedObject
slots:
- anatomical_structure
- anatomical_substructure
- cellular_component
- spatial_qualifiers

```
</details>

### Induced

<details>
```yaml
name: AnatomicalSite
description: The developmental stage and/or age of the specimen in an annotation.
from_schema: https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml
is_a: AuditedObject
attributes:
  anatomical_structure:
    name: anatomical_structure
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml
    domain: AnatomicalTerm
    alias: anatomical_structure
    owner: AnatomicalSite
    domain_of:
    - AnatomicalSite
    range: AnatomicalTerm
  anatomical_substructure:
    name: anatomical_substructure
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml
    domain: AnatomicalTerm
    alias: anatomical_substructure
    owner: AnatomicalSite
    domain_of:
    - AnatomicalSite
    range: AnatomicalTerm
  cellular_component:
    name: cellular_component
    notes:
    - I would like to restrict the range to GOTerm in cellular_component branch, but
      I'm not sure how to do this.
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml
    domain: AnatomicalSite
    alias: cellular_component
    owner: AnatomicalSite
    domain_of:
    - AnatomicalSite
    range: GOTerm
  spatial_qualifiers:
    name: spatial_qualifiers
    description: Qualifiers that describe the spatial characteristics of an event.
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml
    domain: AnatomicalSite
    alias: spatial_qualifiers
    owner: AnatomicalSite
    domain_of:
    - AnatomicalSite
    range: spatial_qualifier_set
  created_by:
    name: created_by
    description: The individual that created the entity.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObject
    multivalued: false
    alias: created_by
    owner: AnatomicalSite
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
    owner: AnatomicalSite
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
    owner: AnatomicalSite
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
    owner: AnatomicalSite
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
    owner: AnatomicalSite
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
    owner: AnatomicalSite
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
    owner: AnatomicalSite
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
    owner: AnatomicalSite
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>