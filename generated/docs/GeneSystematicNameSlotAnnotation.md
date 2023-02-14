# GeneSystematicNameSlotAnnotation

The one current systematic name for the gene.


```mermaid
 classDiagram
      NameSlotAnnotation <|-- GeneSystematicNameSlotAnnotation
      
      GeneSystematicNameSlotAnnotation : created_by
      GeneSystematicNameSlotAnnotation : date_created
      GeneSystematicNameSlotAnnotation : date_updated
      GeneSystematicNameSlotAnnotation : db_date_created
      GeneSystematicNameSlotAnnotation : db_date_updated
      GeneSystematicNameSlotAnnotation : display_text
      GeneSystematicNameSlotAnnotation : evidence
      GeneSystematicNameSlotAnnotation : format_text
      GeneSystematicNameSlotAnnotation : internal
      GeneSystematicNameSlotAnnotation : name_type
      GeneSystematicNameSlotAnnotation : obsolete
      GeneSystematicNameSlotAnnotation : single_gene
      GeneSystematicNameSlotAnnotation : synonym_scope
      GeneSystematicNameSlotAnnotation : synonym_url
      GeneSystematicNameSlotAnnotation : updated_by
      

```



URI: [alliance:GeneSystematicNameSlotAnnotation](http://alliancegenome.org/GeneSystematicNameSlotAnnotation)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * [SlotAnnotation](SlotAnnotation.md)
        * [NameSlotAnnotation](NameSlotAnnotation.md)
            * **GeneSystematicNameSlotAnnotation**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [created_by](created_by.md) | The individual that created the entity. |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [display_text](display_text.md) | A version of a synonym string for display. Any UTF8 character is permitted. |
| [evidence](evidence.md) |  |
| [format_text](format_text.md) | A version of a synonym string using only ASCII characters, which is easier to type (for searches), print and parse. For example, Greek characters are transliterated. |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [name_type](name_type.md) | The type of name: e.g., symbol, full_name, systematic_name, etc. |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [single_gene](single_gene.md) | None |
| [synonym_scope](synonym_scope.md) | the scope of the synonym - permissible values are narrow / broad / related / exact |
| [synonym_url](synonym_url.md) | URL for a synonym: e.g., NCBI URL for the NCBI synonym of an object. |
| [updated_by](updated_by.md) | The individual that last modified the entity. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:GeneSystematicNameSlotAnnotation'] |
| native | ['alliance:GeneSystematicNameSlotAnnotation'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneSystematicNameSlotAnnotation
description: The one current systematic name for the gene.
from_schema: https://github.com/alliance-genome/agr_curation_schema/gene.yaml
is_a: NameSlotAnnotation
slots:
- single_gene
slot_usage:
  single_gene:
    name: single_gene
    domain_of:
    - GeneSymbolSlotAnnotation
    - GeneFullNameSlotAnnotation
    - GeneSystematicNameSlotAnnotation
    - GeneSynonymSlotAnnotation
    required: true
  name_type:
    name: name_type
    notes:
    - 'permissible_values: systematic_name (VocabularyTerm)'
    domain_of:
    - NameSlotAnnotation

```
</details>

### Induced

<details>
```yaml
name: GeneSystematicNameSlotAnnotation
description: The one current systematic name for the gene.
from_schema: https://github.com/alliance-genome/agr_curation_schema/gene.yaml
is_a: NameSlotAnnotation
slot_usage:
  single_gene:
    name: single_gene
    domain_of:
    - GeneSymbolSlotAnnotation
    - GeneFullNameSlotAnnotation
    - GeneSystematicNameSlotAnnotation
    - GeneSynonymSlotAnnotation
    required: true
  name_type:
    name: name_type
    notes:
    - 'permissible_values: systematic_name (VocabularyTerm)'
    domain_of:
    - NameSlotAnnotation
attributes:
  single_gene:
    name: single_gene
    from_schema: https://github.com/alliance-genome/agr_curation_schema/gene.yaml
    multivalued: false
    alias: single_gene
    owner: GeneSystematicNameSlotAnnotation
    domain_of:
    - GeneSymbolSlotAnnotation
    - GeneFullNameSlotAnnotation
    - GeneSystematicNameSlotAnnotation
    - GeneSynonymSlotAnnotation
    range: Gene
    required: true
  name_type:
    name: name_type
    description: 'The type of name: e.g., symbol, full_name, systematic_name, etc.'
    notes:
    - 'permissible_values: systematic_name (VocabularyTerm)'
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: NameSlotAnnotation
    multivalued: false
    alias: name_type
    owner: GeneSystematicNameSlotAnnotation
    domain_of:
    - NameSlotAnnotation
    range: VocabularyTerm
    required: true
  format_text:
    name: format_text
    description: A version of a synonym string using only ASCII characters, which
      is easier to type (for searches), print and parse. For example, Greek characters
      are transliterated.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    aliases:
    - synonym_text
    multivalued: false
    alias: format_text
    owner: GeneSystematicNameSlotAnnotation
    domain_of:
    - NameSlotAnnotation
    - NameSlotAnnotationDTO
    range: string
    required: true
  display_text:
    name: display_text
    description: A version of a synonym string for display. Any UTF8 character is
      permitted.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    aliases:
    - synonym_sgml
    multivalued: false
    alias: display_text
    owner: GeneSystematicNameSlotAnnotation
    domain_of:
    - NameSlotAnnotation
    - NameSlotAnnotationDTO
    range: string
    required: true
  synonym_url:
    name: synonym_url
    description: 'URL for a synonym: e.g., NCBI URL for the NCBI synonym of an object.'
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: synonym_url
    owner: GeneSystematicNameSlotAnnotation
    domain_of:
    - NameSlotAnnotation
    - NameSlotAnnotationDTO
    range: uri
  synonym_scope:
    name: synonym_scope
    description: the scope of the synonym - permissible values are narrow / broad
      / related / exact
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: NameSlotAnnotation
    alias: synonym_scope
    owner: GeneSystematicNameSlotAnnotation
    domain_of:
    - NameSlotAnnotation
    range: VocabularyTerm
  evidence:
    name: evidence
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/reference
    multivalued: true
    alias: evidence
    owner: GeneSystematicNameSlotAnnotation
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
    owner: GeneSystematicNameSlotAnnotation
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
    owner: GeneSystematicNameSlotAnnotation
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
    owner: GeneSystematicNameSlotAnnotation
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
    owner: GeneSystematicNameSlotAnnotation
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
    owner: GeneSystematicNameSlotAnnotation
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
    owner: GeneSystematicNameSlotAnnotation
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
    owner: GeneSystematicNameSlotAnnotation
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
    owner: GeneSystematicNameSlotAnnotation
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>