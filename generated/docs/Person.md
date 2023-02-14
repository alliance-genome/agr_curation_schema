# Person

None


```mermaid
 classDiagram
      Agent <|-- Person
      
      Person : affiliated_alliance_member
      Person : created_by
      Person : date_created
      Person : date_updated
      Person : db_date_created
      Person : db_date_updated
      Person : emails
      Person : first_name
      Person : internal
      Person : last_name
      Person : middle_name
      Person : mod_entity_id
      Person : obsolete
      Person : old_emails
      Person : orcid
      Person : unique_id
      Person : updated_by
      

```



URI: [alliance:Person](http://alliancegenome.org/Person)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * [Agent](Agent.md)
        * **Person**
            * [LoggedInPerson](LoggedInPerson.md)





## Children

* [AuditedObject](AuditedObject.md)
    * [Agent](Agent.md)
        * **Person**
            * [LoggedInPerson](LoggedInPerson.md)



## Slots

| Name | Description  |
| ---  | ---  |
| [affiliated_alliance_member](affiliated_alliance_member.md) | The Alliance Member the person is affiliated with |
| [created_by](created_by.md) | The individual that created the entity. |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [emails](emails.md) | list of emails for a person |
| [first_name](first_name.md) | first name of a person |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [last_name](last_name.md) | last (family) name of a person |
| [middle_name](middle_name.md) | middle names of a person |
| [mod_entity_id](mod_entity_id.md) | The model organism database (MOD) identifier/curie for the object |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [old_emails](old_emails.md) | list of old (outdated) emails for a person |
| [orcid](orcid.md) | Open Researcher and Contributor ID |
| [unique_id](unique_id.md) | A non-curie unique identifier for a thing. |
| [updated_by](updated_by.md) | The individual that last modified the entity. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:Person'] |
| native | ['alliance:Person'] |
| exact | ['schema:person', 'foaf:Person'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Person
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/person
exact_mappings:
- schema:person
- foaf:Person
is_a: Agent
slots:
- last_name
- middle_name
- first_name
- orcid
- emails
- old_emails
- mod_entity_id
- unique_id
- affiliated_alliance_member
slot_usage:
  unique_id:
    name: unique_id
    identifier: true
    domain_of:
    - DiseaseAnnotation
    - ExperimentalCondition
    - ConditionRelation
    - Person

```
</details>

### Induced

<details>
```yaml
name: Person
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/person
exact_mappings:
- schema:person
- foaf:Person
is_a: Agent
slot_usage:
  unique_id:
    name: unique_id
    identifier: true
    domain_of:
    - DiseaseAnnotation
    - ExperimentalCondition
    - ConditionRelation
    - Person
attributes:
  last_name:
    name: last_name
    description: last (family) name of a person
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: last_name
    owner: Person
    domain_of:
    - Person
    - AuthorReference
    range: string
  middle_name:
    name: middle_name
    description: middle names of a person
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    alias: middle_name
    owner: Person
    domain_of:
    - Person
    range: string
  first_name:
    name: first_name
    description: first name of a person
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: first_name
    owner: Person
    domain_of:
    - Person
    - AuthorReference
    range: string
  orcid:
    name: orcid
    description: Open Researcher and Contributor ID
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/person
    domain: Person
    multivalued: false
    alias: orcid
    owner: Person
    domain_of:
    - Person
    range: uriorcurie
  emails:
    name: emails
    description: list of emails for a person
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/person
    multivalued: true
    alias: emails
    owner: Person
    domain_of:
    - Person
    range: string
  old_emails:
    name: old_emails
    description: list of old (outdated) emails for a person
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/person
    multivalued: true
    alias: old_emails
    owner: Person
    domain_of:
    - Person
    range: string
  mod_entity_id:
    name: mod_entity_id
    description: The model organism database (MOD) identifier/curie for the object
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: mod_entity_id
    owner: Person
    domain_of:
    - DiseaseAnnotation
    - DiseaseAnnotationDTO
    - Person
    range: string
  unique_id:
    name: unique_id
    description: A non-curie unique identifier for a thing.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    identifier: true
    alias: unique_id
    owner: Person
    domain_of:
    - DiseaseAnnotation
    - ExperimentalCondition
    - ConditionRelation
    - Person
    range: string
  affiliated_alliance_member:
    name: affiliated_alliance_member
    description: The Alliance Member the person is affiliated with
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/person
    domain: Person
    alias: affiliated_alliance_member
    owner: Person
    domain_of:
    - Person
    range: AllianceMember
  created_by:
    name: created_by
    description: The individual that created the entity.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObject
    multivalued: false
    alias: created_by
    owner: Person
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
    owner: Person
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
    owner: Person
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
    owner: Person
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
    owner: Person
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
    owner: Person
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
    owner: Person
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
    owner: Person
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>