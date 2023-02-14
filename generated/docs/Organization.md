# Organization

An organization that provides information and/or materials to the Alliance. This includes Alliance member organizations (see AllianceMember subclass).


```mermaid
 classDiagram
      Agent <|-- Organization
      
      Organization : abbreviation
      Organization : created_by
      Organization : date_created
      Organization : date_updated
      Organization : db_date_created
      Organization : db_date_updated
      Organization : full_name
      Organization : homepage_resource_descriptor_page
      Organization : internal
      Organization : obsolete
      Organization : short_name
      Organization : updated_by
      

```



URI: [alliance:Organization](http://alliancegenome.org/Organization)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * [Agent](Agent.md)
        * **Organization**
            * [Laboratory](Laboratory.md)
            * [Company](Company.md)
            * [AllianceMember](AllianceMember.md)





## Children

* [AuditedObject](AuditedObject.md)
    * [Agent](Agent.md)
        * **Organization**
            * [Laboratory](Laboratory.md)
            * [Company](Company.md)
            * [AllianceMember](AllianceMember.md)



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
| self | ['alliance:Organization'] |
| native | ['alliance:Organization'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Organization
description: An organization that provides information and/or materials to the Alliance.
  This includes Alliance member organizations (see AllianceMember subclass).
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/person
is_a: Agent
slots:
- abbreviation
- full_name
- short_name
- homepage_resource_descriptor_page

```
</details>

### Induced

<details>
```yaml
name: Organization
description: An organization that provides information and/or materials to the Alliance.
  This includes Alliance member organizations (see AllianceMember subclass).
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/person
is_a: Agent
attributes:
  abbreviation:
    name: abbreviation
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    alias: abbreviation
    owner: Organization
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
    owner: Organization
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
    owner: Organization
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
    owner: Organization
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
    owner: Organization
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
    owner: Organization
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
    owner: Organization
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
    owner: Organization
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
    owner: Organization
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
    owner: Organization
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
    owner: Organization
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
    owner: Organization
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>