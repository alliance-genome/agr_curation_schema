# GeneToGeneOrthology




```mermaid
 classDiagram
      AuditedObject <|-- GeneToGeneOrthology
      
      GeneToGeneOrthology : created_by
      GeneToGeneOrthology : date_created
      GeneToGeneOrthology : date_updated
      GeneToGeneOrthology : db_date_created
      GeneToGeneOrthology : db_date_updated
      GeneToGeneOrthology : gene_object
      GeneToGeneOrthology : gene_subject
      GeneToGeneOrthology : internal
      GeneToGeneOrthology : obsolete
      GeneToGeneOrthology : predicate
      GeneToGeneOrthology : updated_by
      

```



URI: [alliance:GeneToGeneOrthology](http://alliancegenome.org/GeneToGeneOrthology)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * **GeneToGeneOrthology**
        * [GeneToGeneOrthologyCurated](GeneToGeneOrthologyCurated.md)
        * [GeneToGeneOrthologyGenerated](GeneToGeneOrthologyGenerated.md)





## Children

* [AuditedObject](AuditedObject.md)
    * **GeneToGeneOrthology**
        * [GeneToGeneOrthologyCurated](GeneToGeneOrthologyCurated.md)
        * [GeneToGeneOrthologyGenerated](GeneToGeneOrthologyGenerated.md)



## Slots

| Name | Description  |
| ---  | ---  |
| [created_by](created_by.md) | The individual that created the entity. |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [gene_object](gene_object.md) | None |
| [gene_subject](gene_subject.md) | None |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [predicate](predicate.md) | orthologous relationship type |
| [updated_by](updated_by.md) | The individual that last modified the entity. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:GeneToGeneOrthology'] |
| native | ['alliance:GeneToGeneOrthology'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneToGeneOrthology
description: ''
from_schema: https://github.com/alliance-genome/agr_curation_schema/ontologyTerm
is_a: AuditedObject
slots:
- gene_subject
- predicate
- gene_object
slot_usage:
  gene_subject:
    name: gene_subject
    domain_of:
    - GeneToGeneOrthology
    range: Gene
  gene_object:
    name: gene_object
    domain_of:
    - GeneToGeneOrthology
    range: Gene
  predicate:
    name: predicate
    description: orthologous relationship type
    domain_of:
    - Association
    - GeneToGeneOrthology
    subproperty_of: orthologous_to
    symmetric: true

```
</details>

### Induced

<details>
```yaml
name: GeneToGeneOrthology
description: ''
from_schema: https://github.com/alliance-genome/agr_curation_schema/ontologyTerm
is_a: AuditedObject
slot_usage:
  gene_subject:
    name: gene_subject
    domain_of:
    - GeneToGeneOrthology
    range: Gene
  gene_object:
    name: gene_object
    domain_of:
    - GeneToGeneOrthology
    range: Gene
  predicate:
    name: predicate
    description: orthologous relationship type
    domain_of:
    - Association
    - GeneToGeneOrthology
    subproperty_of: orthologous_to
    symmetric: true
attributes:
  gene_subject:
    name: gene_subject
    from_schema: https://github.com/alliance-genome/agr_curation_schema/ontologyTerm
    alias: gene_subject
    owner: GeneToGeneOrthology
    domain_of:
    - GeneToGeneOrthology
    range: Gene
  predicate:
    name: predicate
    description: orthologous relationship type
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    is_a: association_slot
    alias: predicate
    owner: GeneToGeneOrthology
    domain_of:
    - Association
    - GeneToGeneOrthology
    subproperty_of: orthologous_to
    symmetric: true
    range: string
    required: true
  gene_object:
    name: gene_object
    from_schema: https://github.com/alliance-genome/agr_curation_schema/ontologyTerm
    alias: gene_object
    owner: GeneToGeneOrthology
    domain_of:
    - GeneToGeneOrthology
    range: Gene
  created_by:
    name: created_by
    description: The individual that created the entity.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObject
    multivalued: false
    alias: created_by
    owner: GeneToGeneOrthology
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
    owner: GeneToGeneOrthology
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
    owner: GeneToGeneOrthology
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
    owner: GeneToGeneOrthology
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
    owner: GeneToGeneOrthology
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
    owner: GeneToGeneOrthology
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
    owner: GeneToGeneOrthology
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
    owner: GeneToGeneOrthology
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>