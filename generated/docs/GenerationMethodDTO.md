# GenerationMethodDTO

None


```mermaid
 classDiagram
      AuditedObjectDTO <|-- GenerationMethodDTO
      
      GenerationMethodDTO : chemical_mutagen_name
      GenerationMethodDTO : created_by_curie
      GenerationMethodDTO : date_created
      GenerationMethodDTO : date_updated
      GenerationMethodDTO : db_date_created
      GenerationMethodDTO : db_date_updated
      GenerationMethodDTO : integration_method_name
      GenerationMethodDTO : internal
      GenerationMethodDTO : irradiation_mutagen_name
      GenerationMethodDTO : mutagenesis_method_names
      GenerationMethodDTO : mutagenesis_target
      GenerationMethodDTO : obsolete
      GenerationMethodDTO : updated_by_curie
      

```



URI: [alliance:GenerationMethodDTO](http://alliancegenome.org/GenerationMethodDTO)


## Parent Classes

* [AuditedObjectDTO](AuditedObjectDTO.md)
    * **GenerationMethodDTO**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [chemical_mutagen_name](chemical_mutagen_name.md) | The name of the chemical used to generate the mutation through mutagenesis |
| [created_by_curie](created_by_curie.md) | Curie of the Person object representing the individual that created the entity |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [integration_method_name](integration_method_name.md) | WormBase captures the method by which an extrachromosomal transgene was integrated into the genome. |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [irradiation_mutagen_name](irradiation_mutagen_name.md) | The name of the irradiation used to generate the mutation through mutagenesis |
| [mutagenesis_method_names](mutagenesis_method_names.md) | Name of the VocabularyTerm describing the mutagenesis method, e.g. spontaneous / naturally occurring / radiation-induced / recombinant / ENU / CRISPR / TALEN / gamma rays / not specified / spontaneous / DNA / DNA AND CRISPR / DNA and TALEN / zinc finger nuclease / EMS |
| [mutagenesis_target](mutagenesis_target.md) | The target of the mutation, e.g. strain / adult females / adult males / embryos / sperm / not specified |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [updated_by_curie](updated_by_curie.md) | Curie of the Person object representing the individual that updated the entity |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:GenerationMethodDTO'] |
| native | ['alliance:GenerationMethodDTO'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GenerationMethodDTO
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/alleleDTO
is_a: AuditedObjectDTO
slots:
- mutagenesis_method_names
- mutagenesis_target
- integration_method_name
- chemical_mutagen_name
- irradiation_mutagen_name

```
</details>

### Induced

<details>
```yaml
name: GenerationMethodDTO
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/alleleDTO
is_a: AuditedObjectDTO
attributes:
  mutagenesis_method_names:
    name: mutagenesis_method_names
    description: Name of the VocabularyTerm describing the mutagenesis method, e.g.
      spontaneous / naturally occurring / radiation-induced / recombinant / ENU /
      CRISPR / TALEN / gamma rays / not specified / spontaneous / DNA / DNA AND CRISPR
      / DNA and TALEN / zinc finger nuclease / EMS
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/alleleDTO
    domain: AlleleGenerationMethodAssociationDTO
    multivalued: true
    alias: mutagenesis_method_names
    owner: GenerationMethodDTO
    domain_of:
    - GenerationMethodDTO
    range: string
  mutagenesis_target:
    name: mutagenesis_target
    description: The target of the mutation, e.g. strain / adult females / adult males
      / embryos / sperm / not specified
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/allele
    aliases:
    - mutagee
    alias: mutagenesis_target
    owner: GenerationMethodDTO
    domain_of:
    - GenerationMethod
    - GenerationMethodDTO
    range: string
  integration_method_name:
    name: integration_method_name
    description: WormBase captures the method by which an extrachromosomal transgene
      was integrated into the genome.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/alleleDTO
    domain: GenerationMethodDTO
    multivalued: false
    alias: integration_method_name
    owner: GenerationMethodDTO
    domain_of:
    - GenerationMethodDTO
    range: string
  chemical_mutagen_name:
    name: chemical_mutagen_name
    description: The name of the chemical used to generate the mutation through mutagenesis
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/alleleDTO
    domain: GenerationMethodDTO
    alias: chemical_mutagen_name
    owner: GenerationMethodDTO
    domain_of:
    - GenerationMethodDTO
    range: string
  irradiation_mutagen_name:
    name: irradiation_mutagen_name
    description: The name of the irradiation used to generate the mutation through
      mutagenesis
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/alleleDTO
    domain: GenerationMethodDTO
    alias: irradiation_mutagen_name
    owner: GenerationMethodDTO
    domain_of:
    - GenerationMethodDTO
    range: string
  created_by_curie:
    name: created_by_curie
    description: Curie of the Person object representing the individual that created
      the entity
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObjectDTO
    alias: created_by_curie
    owner: GenerationMethodDTO
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
    owner: GenerationMethodDTO
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
    owner: GenerationMethodDTO
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
    owner: GenerationMethodDTO
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
    owner: GenerationMethodDTO
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
    owner: GenerationMethodDTO
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
    owner: GenerationMethodDTO
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
    owner: GenerationMethodDTO
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>