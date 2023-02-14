# AffectedGenomicModelDTO

Ingest class for AGMs


```mermaid
 classDiagram
      GenomicEntityDTO <|-- AffectedGenomicModelDTO
      
      AffectedGenomicModelDTO : component_dtos
      AffectedGenomicModelDTO : created_by_curie
      AffectedGenomicModelDTO : cross_reference_dtos
      AffectedGenomicModelDTO : curie
      AffectedGenomicModelDTO : data_provider_dto
      AffectedGenomicModelDTO : date_created
      AffectedGenomicModelDTO : date_updated
      AffectedGenomicModelDTO : db_date_created
      AffectedGenomicModelDTO : db_date_updated
      AffectedGenomicModelDTO : genomic_location_association_dtos
      AffectedGenomicModelDTO : internal
      AffectedGenomicModelDTO : name
      AffectedGenomicModelDTO : obsolete
      AffectedGenomicModelDTO : reference_curies
      AffectedGenomicModelDTO : secondary_identifiers
      AffectedGenomicModelDTO : sequence_targeting_reagent_curies
      AffectedGenomicModelDTO : subtype_name
      AffectedGenomicModelDTO : taxon_curie
      AffectedGenomicModelDTO : updated_by_curie
      

```



URI: [alliance:AffectedGenomicModelDTO](http://alliancegenome.org/AffectedGenomicModelDTO)


## Parent Classes

* [AuditedObjectDTO](AuditedObjectDTO.md)
    * [BiologicalEntityDTO](BiologicalEntityDTO.md)
        * [GenomicEntityDTO](GenomicEntityDTO.md)
            * **AffectedGenomicModelDTO**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [component_dtos](component_dtos.md) | None |
| [created_by_curie](created_by_curie.md) | Curie of the Person object representing the individual that created the entity |
| [cross_reference_dtos](cross_reference_dtos.md) | None |
| [curie](curie.md) | A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI |
| [data_provider_dto](data_provider_dto.md) | Ingest object representing the organization (e.g. MOD) from which the data was sourced and a CrossReference to that organisation's site |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [genomic_location_association_dtos](genomic_location_association_dtos.md) | None |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [name](name.md) | a human-readable name for an entity |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [reference_curies](reference_curies.md) | External reference curies used for ingest |
| [secondary_identifiers](secondary_identifiers.md) | None |
| [sequence_targeting_reagent_curies](sequence_targeting_reagent_curies.md) | None |
| [subtype_name](subtype_name.md) | Name of VocabularyTerm describing subtype - permissible values: strain / genotype / fish |
| [taxon_curie](taxon_curie.md) | Curie of the NCBITaxonTerm representing the taxon from which the biological entity derives |
| [updated_by_curie](updated_by_curie.md) | Curie of the Person object representing the individual that updated the entity |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:AffectedGenomicModelDTO'] |
| native | ['alliance:AffectedGenomicModelDTO'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AffectedGenomicModelDTO
description: Ingest class for AGMs
from_schema: https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel
is_a: GenomicEntityDTO
slots:
- name
- subtype_name
- reference_curies
- data_provider_dto
- sequence_targeting_reagent_curies
- component_dtos

```
</details>

### Induced

<details>
```yaml
name: AffectedGenomicModelDTO
description: Ingest class for AGMs
from_schema: https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel
is_a: GenomicEntityDTO
attributes:
  name:
    name: name
    description: a human-readable name for an entity
    notes:
    - May want to convert this into a slot that uses NameSlotAnnotation.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel
    multivalued: false
    alias: name
    owner: AffectedGenomicModelDTO
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
  subtype_name:
    name: subtype_name
    description: 'Name of VocabularyTerm describing subtype - permissible values:
      strain / genotype / fish'
    from_schema: https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel
    domain: AffectedGenomicModelDTO
    alias: subtype_name
    owner: AffectedGenomicModelDTO
    domain_of:
    - AffectedGenomicModelDTO
    range: string
    required: true
  reference_curies:
    name: reference_curies
    description: External reference curies used for ingest
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/reference
    multivalued: true
    alias: reference_curies
    owner: AffectedGenomicModelDTO
    domain_of:
    - AlleleDTO
    - ConstructDTO
    - SequenceTargetingReagentDTO
    - AffectedGenomicModelDTO
    range: string
  data_provider_dto:
    name: data_provider_dto
    description: Ingest object representing the organization (e.g. MOD) from which
      the data was sourced and a CrossReference to that organisation's site
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    alias: data_provider_dto
    owner: AffectedGenomicModelDTO
    domain_of:
    - DiseaseAnnotationDTO
    - AffectedGenomicModelDTO
    range: DataProviderDTO
    inlined: true
  sequence_targeting_reagent_curies:
    name: sequence_targeting_reagent_curies
    from_schema: https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel
    domain: AffectedGenomicModelDTO
    multivalued: true
    alias: sequence_targeting_reagent_curies
    owner: AffectedGenomicModelDTO
    domain_of:
    - AffectedGenomicModelDTO
    range: string
  component_dtos:
    name: component_dtos
    from_schema: https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel
    domain: AffectedGenomicModelDTO
    multivalued: true
    alias: component_dtos
    owner: AffectedGenomicModelDTO
    domain_of:
    - AffectedGenomicModelDTO
    range: AffectedGenomicModelComponentDTO
    inlined: true
    inlined_as_list: true
  cross_reference_dtos:
    name: cross_reference_dtos
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: true
    alias: cross_reference_dtos
    owner: AffectedGenomicModelDTO
    domain_of:
    - GenomicEntityDTO
    range: CrossReferenceDTO
    inlined: true
    inlined_as_list: true
  secondary_identifiers:
    name: secondary_identifiers
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    aliases:
    - secondary_ids
    multivalued: true
    alias: secondary_identifiers
    owner: AffectedGenomicModelDTO
    domain_of:
    - OntologyTerm
    - GenomicEntity
    - GenomicEntityDTO
    - Figure
    - Image
    - Antibody
    range: uriorcurie
  genomic_location_association_dtos:
    name: genomic_location_association_dtos
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: GenomicEntityDTO
    multivalued: true
    alias: genomic_location_association_dtos
    owner: AffectedGenomicModelDTO
    domain_of:
    - GenomicEntityDTO
    range: GenomicLocationAssociationDTO
    inlined: true
    inlined_as_list: true
  curie:
    name: curie
    description: A unique identifier for a thing. Must be either a CURIE shorthand
      for a URI or a complete URI
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    identifier: true
    alias: curie
    owner: AffectedGenomicModelDTO
    domain_of:
    - OntologyTerm
    - PhenotypeAnnotation
    - DiseaseAnnotation
    - BiologicalEntity
    - BiologicalEntityDTO
    - Chromosome
    - Assembly
    - Identifier
    - Figure
    - Image
    - Laboratory
    - InformationContentEntity
    - Reference
    - Resource
    - ModCorpusAssociation
    - GeneInteraction
    - ExpressionExperiment
    - GeneNomenclatureSet
    range: uriorcurie
    required: true
  taxon_curie:
    name: taxon_curie
    description: Curie of the NCBITaxonTerm representing the taxon from which the
      biological entity derives
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: taxon_curie
    owner: AffectedGenomicModelDTO
    domain_of:
    - BiologicalEntityDTO
    range: string
    required: true
  created_by_curie:
    name: created_by_curie
    description: Curie of the Person object representing the individual that created
      the entity
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObjectDTO
    alias: created_by_curie
    owner: AffectedGenomicModelDTO
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
    owner: AffectedGenomicModelDTO
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
    owner: AffectedGenomicModelDTO
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
    owner: AffectedGenomicModelDTO
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
    owner: AffectedGenomicModelDTO
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
    owner: AffectedGenomicModelDTO
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
    owner: AffectedGenomicModelDTO
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
    owner: AffectedGenomicModelDTO
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>