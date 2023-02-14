# Company

None


```mermaid
 classDiagram
      Organization <|-- Company
      
      Company : abbreviation
      Company : created_by
      Company : date_created
      Company : date_updated
      Company : db_date_created
      Company : db_date_updated
      Company : full_name
      Company : homepage_resource_descriptor_page
      Company : internal
      Company : obsolete
      Company : short_name
      Company : updated_by
      

```



URI: [alliance:Company](http://alliancegenome.org/Company)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * [Agent](Agent.md)
        * [Organization](Organization.md)
            * **Company**




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
| [full_name](full_name.md) | The full name of the Organization. e.g. Mouse Genome Database, FlyBase, Online Mendelian Inheritance of Man |
| [homepage_resource_descriptor_page](homepage_resource_descriptor_page.md) | ResourceDescriptorPage containing URL template for organization's homepage |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [short_name](short_name.md) | The short name of the organization. For Alliance Members, this is the short name used in the Members list on the website. e.g. MGD, FB, OMIM |
| [updated_by](updated_by.md) | The individual that last modified the entity. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:Company'] |
| native | ['alliance:Company'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Company
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/person
is_a: Organization

```
</details>

### Induced

<details>
```yaml
name: Company
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/person
is_a: Organization
attributes:
  abbreviation:
    name: abbreviation
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    alias: abbreviation
    owner: Company
    domain_of:
    - ECOTerm
    - VocabularyTerm
    - Organization
    range: string
  full_name:
    name: full_name
    description: The full name of the Organization. e.g. Mouse Genome Database, FlyBase,
      Online Mendelian Inheritance of Man
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/person
    domain: Organization
    multivalued: false
    alias: full_name
    owner: Company
    domain_of:
    - Organization
    range: string
    required: true
  short_name:
    name: short_name
    description: The short name of the organization. For Alliance Members, this is
      the short name used in the Members list on the website. e.g. MGD, FB, OMIM
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/person
    domain: Organization
    multivalued: false
    alias: short_name
    owner: Company
    domain_of:
    - Organization
    range: string
    required: true
  homepage_resource_descriptor_page:
    name: homepage_resource_descriptor_page
    description: ResourceDescriptorPage containing URL template for organization's
      homepage
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/person
    domain: Organization
    alias: homepage_resource_descriptor_page
    owner: Company
    domain_of:
    - Organization
    range: ResourceDescriptorPage
  created_by:
    name: created_by
    description: The individual that created the entity.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObject
    multivalued: false
    alias: created_by
    owner: Company
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
    owner: Company
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
    owner: Company
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
    owner: Company
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
    owner: Company
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
    owner: Company
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
    owner: Company
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
    owner: Company
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>