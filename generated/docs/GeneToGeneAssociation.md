# GeneToGeneAssociation

abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.


```mermaid
 classDiagram
      Association <|-- GeneToGeneAssociation
      
      GeneToGeneAssociation : created_by
      GeneToGeneAssociation : date_created
      GeneToGeneAssociation : date_updated
      GeneToGeneAssociation : db_date_created
      GeneToGeneAssociation : db_date_updated
      GeneToGeneAssociation : evidence
      GeneToGeneAssociation : internal
      GeneToGeneAssociation : object
      GeneToGeneAssociation : obsolete
      GeneToGeneAssociation : predicate
      GeneToGeneAssociation : subject
      GeneToGeneAssociation : updated_by
      

```



URI: [alliance:GeneToGeneAssociation](http://alliancegenome.org/GeneToGeneAssociation)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * [Association](Association.md)
        * **GeneToGeneAssociation**
            * [GeneInteraction](GeneInteraction.md)





## Children

* [AuditedObject](AuditedObject.md)
    * [Association](Association.md)
        * **GeneToGeneAssociation**
            * [GeneInteraction](GeneInteraction.md)



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
| [object](object.md) | the object gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as a proxy for the gene or vice versa. |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [predicate](predicate.md) | A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type. |
| [subject](subject.md) | the subject gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as a proxy for the gene or vice versa. |
| [updated_by](updated_by.md) | The individual that last modified the entity. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:GeneToGeneAssociation'] |
| native | ['alliance:GeneToGeneAssociation'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneToGeneAssociation
description: abstract parent class for different kinds of gene-gene or gene product
  to gene product relationships. Includes homology and interaction.
from_schema: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
is_a: Association
abstract: true
slot_usage:
  subject:
    name: subject
    description: the subject gene in the association. If the relation is symmetric,
      subject vs object is arbitrary. We allow a gene product to stand as a proxy
      for the gene or vice versa.
    domain_of:
    - Association
    - VariantConsequence
    range: Gene
  object:
    name: object
    description: the object gene in the association. If the relation is symmetric,
      subject vs object is arbitrary. We allow a gene product to stand as a proxy
      for the gene or vice versa.
    domain_of:
    - Association
    - VariantConsequence
    range: Gene
defining_slots:
- subject
- object

```
</details>

### Induced

<details>
```yaml
name: GeneToGeneAssociation
description: abstract parent class for different kinds of gene-gene or gene product
  to gene product relationships. Includes homology and interaction.
from_schema: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
is_a: Association
abstract: true
slot_usage:
  subject:
    name: subject
    description: the subject gene in the association. If the relation is symmetric,
      subject vs object is arbitrary. We allow a gene product to stand as a proxy
      for the gene or vice versa.
    domain_of:
    - Association
    - VariantConsequence
    range: Gene
  object:
    name: object
    description: the object gene in the association. If the relation is symmetric,
      subject vs object is arbitrary. We allow a gene product to stand as a proxy
      for the gene or vice versa.
    domain_of:
    - Association
    - VariantConsequence
    range: Gene
attributes:
  subject:
    name: subject
    description: the subject gene in the association. If the relation is symmetric,
      subject vs object is arbitrary. We allow a gene product to stand as a proxy
      for the gene or vice versa.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    is_a: association_slot
    alias: subject
    owner: GeneToGeneAssociation
    domain_of:
    - Association
    - VariantConsequence
    range: Gene
    required: true
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
    owner: GeneToGeneAssociation
    domain_of:
    - Association
    - GeneToGeneOrthology
    range: string
    required: true
  object:
    name: object
    description: the object gene in the association. If the relation is symmetric,
      subject vs object is arbitrary. We allow a gene product to stand as a proxy
      for the gene or vice versa.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    is_a: association_slot
    alias: object
    owner: GeneToGeneAssociation
    domain_of:
    - Association
    - VariantConsequence
    range: Gene
    required: true
  evidence:
    name: evidence
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/reference
    multivalued: true
    alias: evidence
    owner: GeneToGeneAssociation
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
    owner: GeneToGeneAssociation
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
    owner: GeneToGeneAssociation
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
    owner: GeneToGeneAssociation
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
    owner: GeneToGeneAssociation
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
    owner: GeneToGeneAssociation
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
    owner: GeneToGeneAssociation
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
    owner: GeneToGeneAssociation
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
    owner: GeneToGeneAssociation
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean
defining_slots:
- subject
- object

```
</details>