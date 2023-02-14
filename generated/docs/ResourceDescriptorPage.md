# ResourceDescriptorPage

None


```mermaid
 classDiagram
      AuditedObject <|-- ResourceDescriptorPage
      
      ResourceDescriptorPage : created_by
      ResourceDescriptorPage : date_created
      ResourceDescriptorPage : date_updated
      ResourceDescriptorPage : db_date_created
      ResourceDescriptorPage : db_date_updated
      ResourceDescriptorPage : internal
      ResourceDescriptorPage : name
      ResourceDescriptorPage : obsolete
      ResourceDescriptorPage : page_description
      ResourceDescriptorPage : updated_by
      ResourceDescriptorPage : url_template
      

```



URI: [alliance:ResourceDescriptorPage](http://alliancegenome.org/ResourceDescriptorPage)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * **ResourceDescriptorPage**




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
| [name](name.md) | a human-readable name for an entity |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [page_description](page_description.md) | Description of page |
| [updated_by](updated_by.md) | The individual that last modified the entity. |
| [url_template](url_template.md) | URL template for constructing link to resource using prodived ID, eg. "https://www.omim.org/phenotypicSeries/[%s]" |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:ResourceDescriptorPage'] |
| native | ['alliance:ResourceDescriptorPage'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ResourceDescriptorPage
from_schema: https://github.com/alliance-genome/agr_curation_schema/resourceDescriptor.yaml
is_a: AuditedObject
slots:
- name
- url_template
- page_description
slot_usage:
  name:
    name: name
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
name: ResourceDescriptorPage
from_schema: https://github.com/alliance-genome/agr_curation_schema/resourceDescriptor.yaml
is_a: AuditedObject
slot_usage:
  name:
    name: name
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
    alias: name
    owner: ResourceDescriptorPage
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
  url_template:
    name: url_template
    description: URL template for constructing link to resource using prodived ID,
      eg. "https://www.omim.org/phenotypicSeries/[%s]"
    from_schema: https://github.com/alliance-genome/agr_curation_schema/resourceDescriptor.yaml
    domain: ResourceDescriptor
    alias: url_template
    owner: ResourceDescriptorPage
    domain_of:
    - ResourceDescriptorPage
    range: string
  page_description:
    name: page_description
    description: Description of page
    from_schema: https://github.com/alliance-genome/agr_curation_schema/resourceDescriptor.yaml
    domain: ResourceDescriptorPage
    alias: page_description
    owner: ResourceDescriptorPage
    domain_of:
    - ResourceDescriptorPage
    range: string
  created_by:
    name: created_by
    description: The individual that created the entity.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObject
    multivalued: false
    alias: created_by
    owner: ResourceDescriptorPage
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
    owner: ResourceDescriptorPage
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
    owner: ResourceDescriptorPage
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
    owner: ResourceDescriptorPage
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
    owner: ResourceDescriptorPage
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
    owner: ResourceDescriptorPage
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
    owner: ResourceDescriptorPage
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
    owner: ResourceDescriptorPage
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>