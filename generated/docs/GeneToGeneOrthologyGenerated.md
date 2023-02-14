# GeneToGeneOrthologyGenerated

Class that holds the properties necessary to record an orthology record from DIOPT


```mermaid
 classDiagram
      GeneToGeneOrthology <|-- GeneToGeneOrthologyGenerated
      
      GeneToGeneOrthologyGenerated : confidence
      GeneToGeneOrthologyGenerated : created_by
      GeneToGeneOrthologyGenerated : date_created
      GeneToGeneOrthologyGenerated : date_updated
      GeneToGeneOrthologyGenerated : db_date_created
      GeneToGeneOrthologyGenerated : db_date_updated
      GeneToGeneOrthologyGenerated : gene_object
      GeneToGeneOrthologyGenerated : gene_subject
      GeneToGeneOrthologyGenerated : internal
      GeneToGeneOrthologyGenerated : is_best_reverse_score
      GeneToGeneOrthologyGenerated : is_best_score
      GeneToGeneOrthologyGenerated : moderate_filter
      GeneToGeneOrthologyGenerated : obsolete
      GeneToGeneOrthologyGenerated : predicate
      GeneToGeneOrthologyGenerated : strict_filter
      GeneToGeneOrthologyGenerated : updated_by
      

```



URI: [alliance:GeneToGeneOrthologyGenerated](http://alliancegenome.org/GeneToGeneOrthologyGenerated)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * [GeneToGeneOrthology](GeneToGeneOrthology.md)
        * **GeneToGeneOrthologyGenerated**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [confidence](confidence.md) | None |
| [created_by](created_by.md) | The individual that created the entity. |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [gene_object](gene_object.md) | None |
| [gene_subject](gene_subject.md) | None |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [is_best_reverse_score](is_best_reverse_score.md) | None |
| [is_best_score](is_best_score.md) | None |
| [moderate_filter](moderate_filter.md) | None |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [predicate](predicate.md) | A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type. |
| [strict_filter](strict_filter.md) | None |
| [updated_by](updated_by.md) | The individual that last modified the entity. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:GeneToGeneOrthologyGenerated'] |
| native | ['alliance:GeneToGeneOrthologyGenerated'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneToGeneOrthologyGenerated
description: Class that holds the properties necessary to record an orthology record
  from DIOPT
from_schema: https://github.com/alliance-genome/agr_curation_schema/ontologyTerm
is_a: GeneToGeneOrthology
slots:
- is_best_score
- is_best_reverse_score
- confidence
- strict_filter
- moderate_filter

```
</details>

### Induced

<details>
```yaml
name: GeneToGeneOrthologyGenerated
description: Class that holds the properties necessary to record an orthology record
  from DIOPT
from_schema: https://github.com/alliance-genome/agr_curation_schema/ontologyTerm
is_a: GeneToGeneOrthology
attributes:
  is_best_score:
    name: is_best_score
    from_schema: https://github.com/alliance-genome/agr_curation_schema/ontologyTerm
    alias: is_best_score
    owner: GeneToGeneOrthologyGenerated
    domain_of:
    - GeneToGeneOrthologyGenerated
    range: string
  is_best_reverse_score:
    name: is_best_reverse_score
    from_schema: https://github.com/alliance-genome/agr_curation_schema/ontologyTerm
    alias: is_best_reverse_score
    owner: GeneToGeneOrthologyGenerated
    domain_of:
    - GeneToGeneOrthologyGenerated
    range: string
  confidence:
    name: confidence
    from_schema: https://github.com/alliance-genome/agr_curation_schema/ontologyTerm
    alias: confidence
    owner: GeneToGeneOrthologyGenerated
    domain_of:
    - GeneToGeneOrthologyGenerated
    range: string
  strict_filter:
    name: strict_filter
    from_schema: https://github.com/alliance-genome/agr_curation_schema/ontologyTerm
    alias: strict_filter
    owner: GeneToGeneOrthologyGenerated
    domain_of:
    - GeneToGeneOrthologyGenerated
    range: string
  moderate_filter:
    name: moderate_filter
    from_schema: https://github.com/alliance-genome/agr_curation_schema/ontologyTerm
    alias: moderate_filter
    owner: GeneToGeneOrthologyGenerated
    domain_of:
    - GeneToGeneOrthologyGenerated
    range: string
  gene_subject:
    name: gene_subject
    from_schema: https://github.com/alliance-genome/agr_curation_schema/ontologyTerm
    alias: gene_subject
    owner: GeneToGeneOrthologyGenerated
    domain_of:
    - GeneToGeneOrthology
    range: Gene
  predicate:
    name: predicate
    description: A high-level grouping for the relationship type. This is analogous
      to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j
      this corresponds to the relationship type.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    exact_mappings:
    - biolink:predicate
    is_a: association_slot
    alias: predicate
    owner: GeneToGeneOrthologyGenerated
    domain_of:
    - Association
    - GeneToGeneOrthology
    range: string
    required: true
  gene_object:
    name: gene_object
    from_schema: https://github.com/alliance-genome/agr_curation_schema/ontologyTerm
    alias: gene_object
    owner: GeneToGeneOrthologyGenerated
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
    owner: GeneToGeneOrthologyGenerated
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
    owner: GeneToGeneOrthologyGenerated
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
    owner: GeneToGeneOrthologyGenerated
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
    owner: GeneToGeneOrthologyGenerated
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
    owner: GeneToGeneOrthologyGenerated
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
    owner: GeneToGeneOrthologyGenerated
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
    owner: GeneToGeneOrthologyGenerated
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
    owner: GeneToGeneOrthologyGenerated
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>