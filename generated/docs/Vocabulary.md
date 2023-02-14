# Vocabulary

A set of VocabularyTerm objects.


```mermaid
 classDiagram
      AuditedObject <|-- Vocabulary
      
      Vocabulary : created_by
      Vocabulary : date_created
      Vocabulary : date_updated
      Vocabulary : db_date_created
      Vocabulary : db_date_updated
      Vocabulary : internal
      Vocabulary : member_terms
      Vocabulary : name
      Vocabulary : obsolete
      Vocabulary : updated_by
      Vocabulary : vocabulary_description
      

```



URI: [alliance:Vocabulary](http://alliancegenome.org/Vocabulary)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * **Vocabulary**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [created_by](created_by.md) | The individual that created the entity. |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [member_terms](member_terms.md) | Set of VocabularyTerm objects in a Vocabulary object set |
| [name](name.md) | a human-readable name for an entity |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [updated_by](updated_by.md) | The individual that last modified the entity. |
| [vocabulary_description](vocabulary_description.md) | The free text description of a Vocabulary including its intended use. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:Vocabulary'] |
| native | ['alliance:Vocabulary'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Vocabulary
description: A set of VocabularyTerm objects.
from_schema: https://github.com/alliance-genome/agr_curation_schema/controlledVocabulary.yaml
is_a: AuditedObject
slots:
- name
- vocabulary_description
- member_terms
slot_usage:
  name:
    name: name
    identifier: true
    domain_of:
    - OntologyTerm
    - ResourceDescriptor
    - ResourceDescriptorPage
    - AffectedGenomicModel
    - AffectedGenomicModelDTO
    - VocabularyTerm
    - Vocabulary
    - VocabularyTermSet
    - Antibody
    - CurationReportGroup
    - CurationReport
    - BulkLoadGroup
    - BulkLoad
    required: true

```
</details>

### Induced

<details>
```yaml
name: Vocabulary
description: A set of VocabularyTerm objects.
from_schema: https://github.com/alliance-genome/agr_curation_schema/controlledVocabulary.yaml
is_a: AuditedObject
slot_usage:
  name:
    name: name
    identifier: true
    domain_of:
    - OntologyTerm
    - ResourceDescriptor
    - ResourceDescriptorPage
    - AffectedGenomicModel
    - AffectedGenomicModelDTO
    - VocabularyTerm
    - Vocabulary
    - VocabularyTermSet
    - Antibody
    - CurationReportGroup
    - CurationReport
    - BulkLoadGroup
    - BulkLoad
    required: true
attributes:
  name:
    name: name
    description: a human-readable name for an entity
    from_schema: https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel
    multivalued: false
    identifier: true
    alias: name
    owner: Vocabulary
    domain_of:
    - OntologyTerm
    - ResourceDescriptor
    - ResourceDescriptorPage
    - AffectedGenomicModel
    - AffectedGenomicModelDTO
    - VocabularyTerm
    - Vocabulary
    - VocabularyTermSet
    - Antibody
    - CurationReportGroup
    - CurationReport
    - BulkLoadGroup
    - BulkLoad
    range: string
    required: true
  vocabulary_description:
    name: vocabulary_description
    description: The free text description of a Vocabulary including its intended
      use.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/controlledVocabulary.yaml
    alias: vocabulary_description
    owner: Vocabulary
    domain_of:
    - Vocabulary
    range: string
  member_terms:
    name: member_terms
    description: Set of VocabularyTerm objects in a Vocabulary object set
    from_schema: https://github.com/alliance-genome/agr_curation_schema/controlledVocabulary.yaml
    multivalued: true
    alias: member_terms
    owner: Vocabulary
    domain_of:
    - Vocabulary
    - VocabularyTermSet
    range: VocabularyTerm
  created_by:
    name: created_by
    description: The individual that created the entity.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObject
    multivalued: false
    alias: created_by
    owner: Vocabulary
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
    owner: Vocabulary
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
    owner: Vocabulary
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
    owner: Vocabulary
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
    owner: Vocabulary
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
    owner: Vocabulary
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
    owner: Vocabulary
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
    owner: Vocabulary
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>