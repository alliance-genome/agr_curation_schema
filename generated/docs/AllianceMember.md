# AllianceMember

An organization that is a member of the Alliance of Genome Resources.


```mermaid
 classDiagram
      Organization <|-- AllianceMember
      
      AllianceMember : abbreviation
      AllianceMember : alliance_member_id
      AllianceMember : created_by
      AllianceMember : date_created
      AllianceMember : date_updated
      AllianceMember : db_date_created
      AllianceMember : db_date_updated
      AllianceMember : full_name
      AllianceMember : homepage_resource_descriptor_page
      AllianceMember : internal
      AllianceMember : obsolete
      AllianceMember : short_name
      AllianceMember : updated_by
      

```



URI: [alliance:AllianceMember](http://alliancegenome.org/AllianceMember)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * [Agent](Agent.md)
        * [Organization](Organization.md)
            * **AllianceMember**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [abbreviation](abbreviation.md) | The curie prefix, or letter code used by FMS (Alliance file management system).  e.g. MGI, FB |
| [alliance_member_id](alliance_member_id.md) | An integer referring to an AllianceMember object in the AllianceMember/MOD database table. It's a primary key in the AllianceMember/MOD table, a foreign key if used in other tables. |
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
| self | ['alliance:AllianceMember'] |
| native | ['alliance:AllianceMember'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AllianceMember
description: An organization that is a member of the Alliance of Genome Resources.
notes:
- 'We have not modeled synonyms, e.g. Mouse Genome Informatics Literature has 8 values:
  FB, MGI, RGD, SGD, WB, XB, ZFIN, GO.'
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/allianceMember
is_a: Organization
slots:
- alliance_member_id
slot_usage:
  abbreviation:
    name: abbreviation
    description: The curie prefix, or letter code used by FMS (Alliance file management
      system).  e.g. MGI, FB
    multivalued: false
    domain_of:
    - ECOTerm
    - VocabularyTerm
    - Organization
    range: string
    required: true
  date_created:
    name: date_created
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    required: true

```
</details>

### Induced

<details>
```yaml
name: AllianceMember
description: An organization that is a member of the Alliance of Genome Resources.
notes:
- 'We have not modeled synonyms, e.g. Mouse Genome Informatics Literature has 8 values:
  FB, MGI, RGD, SGD, WB, XB, ZFIN, GO.'
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/allianceMember
is_a: Organization
slot_usage:
  abbreviation:
    name: abbreviation
    description: The curie prefix, or letter code used by FMS (Alliance file management
      system).  e.g. MGI, FB
    multivalued: false
    domain_of:
    - ECOTerm
    - VocabularyTerm
    - Organization
    range: string
    required: true
  date_created:
    name: date_created
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    required: true
attributes:
  alliance_member_id:
    name: alliance_member_id
    description: An integer referring to an AllianceMember object in the AllianceMember/MOD
      database table. It's a primary key in the AllianceMember/MOD table, a foreign
      key if used in other tables.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/allianceMember
    domain: AllianceMember
    multivalued: false
    alias: alliance_member_id
    owner: AllianceMember
    domain_of:
    - AllianceMember
    - ModCorpusAssociation
    range: integer
    required: true
  abbreviation:
    name: abbreviation
    description: The curie prefix, or letter code used by FMS (Alliance file management
      system).  e.g. MGI, FB
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    alias: abbreviation
    owner: AllianceMember
    domain_of:
    - ECOTerm
    - VocabularyTerm
    - Organization
    range: string
    required: true
  full_name:
    name: full_name
    description: The full name of the Organization. e.g. Mouse Genome Database, FlyBase,
      Online Mendelian Inheritance of Man
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/person
    domain: Organization
    multivalued: false
    alias: full_name
    owner: AllianceMember
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
    owner: AllianceMember
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
    owner: AllianceMember
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
    owner: AllianceMember
    domain_of:
    - AuditedObject
    range: Person
  date_created:
    name: date_created
    description: The date on which an entity was created. This can be applied to nodes
      or edges.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: date_created
    owner: AllianceMember
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: datetime
    required: true
  updated_by:
    name: updated_by
    description: The individual that last modified the entity.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObject
    multivalued: false
    alias: updated_by
    owner: AllianceMember
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
    owner: AllianceMember
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
    owner: AllianceMember
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
    owner: AllianceMember
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
    owner: AllianceMember
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
    owner: AllianceMember
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>