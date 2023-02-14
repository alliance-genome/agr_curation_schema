# GenomicLocationAssociationDTO

None


```mermaid
 classDiagram
      AuditedObjectDTO <|-- GenomicLocationAssociationDTO
      
      GenomicLocationAssociationDTO : assembly_curie
      GenomicLocationAssociationDTO : chromosome_curie
      GenomicLocationAssociationDTO : created_by_curie
      GenomicLocationAssociationDTO : date_created
      GenomicLocationAssociationDTO : date_updated
      GenomicLocationAssociationDTO : db_date_created
      GenomicLocationAssociationDTO : db_date_updated
      GenomicLocationAssociationDTO : end
      GenomicLocationAssociationDTO : evidence_curies
      GenomicLocationAssociationDTO : genomic_entity_curie
      GenomicLocationAssociationDTO : internal
      GenomicLocationAssociationDTO : obsolete
      GenomicLocationAssociationDTO : predicate_name
      GenomicLocationAssociationDTO : start
      GenomicLocationAssociationDTO : updated_by_curie
      

```



URI: [alliance:GenomicLocationAssociationDTO](http://alliancegenome.org/GenomicLocationAssociationDTO)


## Parent Classes

* [AuditedObjectDTO](AuditedObjectDTO.md)
    * **GenomicLocationAssociationDTO**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [assembly_curie](assembly_curie.md) | None |
| [chromosome_curie](chromosome_curie.md) | None |
| [created_by_curie](created_by_curie.md) | Curie of the Person object representing the individual that created the entity |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [end](end.md) | The end of the feature in positive 1-based integer coordinates |
| [evidence_curies](evidence_curies.md) | Curies of InformationContentEntity objects given as evidence |
| [genomic_entity_curie](genomic_entity_curie.md) | None |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [predicate_name](predicate_name.md) | Name of VocabularyTerm representing predicate of an Association |
| [start](start.md) | The start of the feature in positive 1-based integer coordinates |
| [updated_by_curie](updated_by_curie.md) | Curie of the Person object representing the individual that updated the entity |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:GenomicLocationAssociationDTO'] |
| native | ['alliance:GenomicLocationAssociationDTO'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GenomicLocationAssociationDTO
from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
is_a: AuditedObjectDTO
slots:
- genomic_entity_curie
- predicate_name
- chromosome_curie
- evidence_curies
- assembly_curie
- start
- end
slot_usage:
  genomic_entity_curie:
    name: genomic_entity_curie
    domain_of:
    - GenomicLocationAssociationDTO
    required: true
  predicate_name:
    name: predicate_name
    domain_of:
    - AlleleCellLineAssociationDTO
    - AlleleGenerationMethodAssociationDTO
    - AlleleGenomicEntityAssociationDTO
    - AlleleImageAssociationDTO
    - AlleleOriginAssociationDTO
    - GenomicLocationAssociationDTO
    required: true
    any_of:
    - equals_string: has_genomic_location
  chromosome_curie:
    name: chromosome_curie
    domain_of:
    - GenomicLocationAssociationDTO
    required: true
  assembly_curie:
    name: assembly_curie
    domain_of:
    - GenomicLocationAssociationDTO
    required: true
  start:
    name: start
    domain_of:
    - GenomicLocationAssociation
    - GenomicLocationAssociationDTO
    required: true
  end:
    name: end
    domain_of:
    - GenomicLocationAssociation
    - GenomicLocationAssociationDTO
    required: true

```
</details>

### Induced

<details>
```yaml
name: GenomicLocationAssociationDTO
from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
is_a: AuditedObjectDTO
slot_usage:
  genomic_entity_curie:
    name: genomic_entity_curie
    domain_of:
    - GenomicLocationAssociationDTO
    required: true
  predicate_name:
    name: predicate_name
    domain_of:
    - AlleleCellLineAssociationDTO
    - AlleleGenerationMethodAssociationDTO
    - AlleleGenomicEntityAssociationDTO
    - AlleleImageAssociationDTO
    - AlleleOriginAssociationDTO
    - GenomicLocationAssociationDTO
    required: true
    any_of:
    - equals_string: has_genomic_location
  chromosome_curie:
    name: chromosome_curie
    domain_of:
    - GenomicLocationAssociationDTO
    required: true
  assembly_curie:
    name: assembly_curie
    domain_of:
    - GenomicLocationAssociationDTO
    required: true
  start:
    name: start
    domain_of:
    - GenomicLocationAssociation
    - GenomicLocationAssociationDTO
    required: true
  end:
    name: end
    domain_of:
    - GenomicLocationAssociation
    - GenomicLocationAssociationDTO
    required: true
attributes:
  genomic_entity_curie:
    name: genomic_entity_curie
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: genomic_entity_curie
    owner: GenomicLocationAssociationDTO
    domain_of:
    - GenomicLocationAssociationDTO
    range: string
    required: true
  predicate_name:
    name: predicate_name
    description: Name of VocabularyTerm representing predicate of an Association
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: predicate_name
    owner: GenomicLocationAssociationDTO
    domain_of:
    - AlleleCellLineAssociationDTO
    - AlleleGenerationMethodAssociationDTO
    - AlleleGenomicEntityAssociationDTO
    - AlleleImageAssociationDTO
    - AlleleOriginAssociationDTO
    - GenomicLocationAssociationDTO
    range: string
    required: true
    any_of:
    - equals_string: has_genomic_location
  chromosome_curie:
    name: chromosome_curie
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: chromosome_curie
    owner: GenomicLocationAssociationDTO
    domain_of:
    - GenomicLocationAssociationDTO
    range: string
    required: true
  evidence_curies:
    name: evidence_curies
    description: Curies of InformationContentEntity objects given as evidence
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/reference
    multivalued: true
    alias: evidence_curies
    owner: GenomicLocationAssociationDTO
    domain_of:
    - DiseaseAnnotationDTO
    - AlleleCellLineAssociationDTO
    - AlleleGenerationMethodAssociationDTO
    - AlleleGenomicEntityAssociationDTO
    - AlleleImageAssociationDTO
    - AlleleOriginAssociationDTO
    - NoteDTO
    - SlotAnnotationDTO
    - GenomicLocationAssociationDTO
    range: string
  assembly_curie:
    name: assembly_curie
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: assembly_curie
    owner: GenomicLocationAssociationDTO
    domain_of:
    - GenomicLocationAssociationDTO
    range: string
    required: true
  start:
    name: start
    description: The start of the feature in positive 1-based integer coordinates
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: start
    owner: GenomicLocationAssociationDTO
    domain_of:
    - GenomicLocationAssociation
    - GenomicLocationAssociationDTO
    range: integer
    required: true
  end:
    name: end
    description: The end of the feature in positive 1-based integer coordinates
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: end
    owner: GenomicLocationAssociationDTO
    domain_of:
    - GenomicLocationAssociation
    - GenomicLocationAssociationDTO
    range: integer
    required: true
  created_by_curie:
    name: created_by_curie
    description: Curie of the Person object representing the individual that created
      the entity
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObjectDTO
    alias: created_by_curie
    owner: GenomicLocationAssociationDTO
    domain_of:
    - AuditedObjectDTO
    range: string
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
    owner: GenomicLocationAssociationDTO
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: datetime
  updated_by_curie:
    name: updated_by_curie
    description: Curie of the Person object representing the individual that updated
      the entity
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObjectDTO
    alias: updated_by_curie
    owner: GenomicLocationAssociationDTO
    domain_of:
    - AuditedObjectDTO
    range: string
  date_updated:
    name: date_updated
    description: Date on which an entity was last modified.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    aliases:
    - date_last_modified
    alias: date_updated
    owner: GenomicLocationAssociationDTO
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
    owner: GenomicLocationAssociationDTO
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
    owner: GenomicLocationAssociationDTO
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
    owner: GenomicLocationAssociationDTO
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
    owner: GenomicLocationAssociationDTO
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>