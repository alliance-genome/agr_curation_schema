# VocabularyTerm

A concept or class in a simple vocabulary.


```mermaid
 classDiagram
      AuditedObject <|-- VocabularyTerm
      
      VocabularyTerm : abbreviation
      VocabularyTerm : created_by
      VocabularyTerm : date_created
      VocabularyTerm : date_updated
      VocabularyTerm : db_date_created
      VocabularyTerm : db_date_updated
      VocabularyTerm : definition
      VocabularyTerm : internal
      VocabularyTerm : name
      VocabularyTerm : obsolete
      VocabularyTerm : text_synonyms
      VocabularyTerm : updated_by
      

```



URI: [alliance:VocabularyTerm](http://alliancegenome.org/VocabularyTerm)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * **VocabularyTerm**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [abbreviation](abbreviation.md) | None |
| [created_by](created_by.md) | The individual that created the entity. |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [definition](definition.md) | The explanation of the meaning of a term. |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [name](name.md) | a human-readable name for an entity |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [text_synonyms](text_synonyms.md) | Free text synonym(s) of a term, used for controlled vocabulary terms; this is distinct from the 'synonyms' slot which has a range of a Synonym class object. |
| [updated_by](updated_by.md) | The individual that last modified the entity. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:VocabularyTerm'] |
| native | ['alliance:VocabularyTerm'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VocabularyTerm
description: A concept or class in a simple vocabulary.
from_schema: https://github.com/alliance-genome/agr_curation_schema/controlledVocabulary.yaml
is_a: AuditedObject
slots:
- name
- abbreviation
- definition
- text_synonyms
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
name: VocabularyTerm
description: A concept or class in a simple vocabulary.
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
    owner: VocabularyTerm
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
  abbreviation:
    name: abbreviation
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    alias: abbreviation
    owner: VocabularyTerm
    domain_of:
    - ECOTerm
    - VocabularyTerm
    - Organization
    range: string
  definition:
    name: definition
    description: The explanation of the meaning of a term.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml
    alias: definition
    owner: VocabularyTerm
    domain_of:
    - OntologyTerm
    - VocabularyTerm
    range: string
  text_synonyms:
    name: text_synonyms
    description: Free text synonym(s) of a term, used for controlled vocabulary terms;
      this is distinct from the 'synonyms' slot which has a range of a Synonym class
      object.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/controlledVocabulary.yaml
    domain: VocabularyTerm
    multivalued: true
    alias: text_synonyms
    owner: VocabularyTerm
    domain_of:
    - VocabularyTerm
    range: string
  created_by:
    name: created_by
    description: The individual that created the entity.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObject
    multivalued: false
    alias: created_by
    owner: VocabularyTerm
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
    owner: VocabularyTerm
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
    owner: VocabularyTerm
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
    owner: VocabularyTerm
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
    owner: VocabularyTerm
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
    owner: VocabularyTerm
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
    owner: VocabularyTerm
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
    owner: VocabularyTerm
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>