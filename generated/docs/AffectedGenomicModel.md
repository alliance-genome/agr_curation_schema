# AffectedGenomicModel

Includes inbred strains, stocks, disease models and mutant genotypes


```mermaid
 classDiagram
      GenomicEntity <|-- AffectedGenomicModel
      
      AffectedGenomicModel : components
      AffectedGenomicModel : created_by
      AffectedGenomicModel : cross_references
      AffectedGenomicModel : curie
      AffectedGenomicModel : data_provider
      AffectedGenomicModel : date_created
      AffectedGenomicModel : date_updated
      AffectedGenomicModel : db_date_created
      AffectedGenomicModel : db_date_updated
      AffectedGenomicModel : genomic_location_associations
      AffectedGenomicModel : internal
      AffectedGenomicModel : name
      AffectedGenomicModel : obsolete
      AffectedGenomicModel : parental_populations
      AffectedGenomicModel : references
      AffectedGenomicModel : secondary_identifiers
      AffectedGenomicModel : sequence_targeting_reagents
      AffectedGenomicModel : subtype
      AffectedGenomicModel : taxon
      AffectedGenomicModel : updated_by
      

```



URI: [alliance:AffectedGenomicModel](http://alliancegenome.org/AffectedGenomicModel)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * [BiologicalEntity](BiologicalEntity.md)
        * [GenomicEntity](GenomicEntity.md)
            * **AffectedGenomicModel**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [components](components.md) | Collection of genomic components that make up a model, i.e. 'allele', each with a zygosity |
| [created_by](created_by.md) | The individual that created the entity. |
| [cross_references](cross_references.md) | Holds between an object and its CrossReferences. |
| [curie](curie.md) | A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI |
| [data_provider](data_provider.md) | Object representing the organization (e.g. MOD) from which the data was sourced and a CrossReference to that organisation's site |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [genomic_location_associations](genomic_location_associations.md) | None |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [name](name.md) | a human-readable name for an entity |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [parental_populations](parental_populations.md) | None |
| [references](references.md) | holds between an object and a list of references |
| [secondary_identifiers](secondary_identifiers.md) | None |
| [sequence_targeting_reagents](sequence_targeting_reagents.md) | None |
| [subtype](subtype.md) | Subtype of affected genomic model - permissible values: strain / genotype / fish |
| [taxon](taxon.md) | The taxon from which the biological entity derives. |
| [updated_by](updated_by.md) | The individual that last modified the entity. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:AffectedGenomicModel'] |
| native | ['alliance:AffectedGenomicModel'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AffectedGenomicModel
description: Includes inbred strains, stocks, disease models and mutant genotypes
from_schema: https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel
is_a: GenomicEntity
slots:
- name
- subtype
- components
- sequence_targeting_reagents
- parental_populations
- data_provider
- references

```
</details>

### Induced

<details>
```yaml
name: AffectedGenomicModel
description: Includes inbred strains, stocks, disease models and mutant genotypes
from_schema: https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel
is_a: GenomicEntity
attributes:
  name:
    name: name
    description: a human-readable name for an entity
    notes:
    - May want to convert this into a slot that uses NameSlotAnnotation.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel
    multivalued: false
    alias: name
    owner: AffectedGenomicModel
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
  subtype:
    name: subtype
    description: 'Subtype of affected genomic model - permissible values: strain /
      genotype / fish'
    from_schema: https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel
    domain: AffectedGenomicModel
    alias: subtype
    owner: AffectedGenomicModel
    domain_of:
    - AffectedGenomicModel
    range: VocabularyTerm
    required: true
  components:
    name: components
    description: Collection of genomic components that make up a model, i.e. 'allele',
      each with a zygosity
    from_schema: https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel
    singular_name: component
    domain: AffectedGenomicModel
    multivalued: true
    alias: components
    owner: AffectedGenomicModel
    domain_of:
    - AffectedGenomicModel
    range: AffectedGenomicModelComponent
  sequence_targeting_reagents:
    name: sequence_targeting_reagents
    from_schema: https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel
    singular_name: sequence_targeting_reagent
    domain: AffectedGenomicModel
    multivalued: true
    alias: sequence_targeting_reagents
    owner: AffectedGenomicModel
    domain_of:
    - AffectedGenomicModel
    range: SequenceTargetingReagent
  parental_populations:
    name: parental_populations
    from_schema: https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel
    singular_name: parental_population
    domain: AffectedGenomicModel
    alias: parental_populations
    owner: AffectedGenomicModel
    domain_of:
    - AffectedGenomicModel
    range: uriorcurie
  data_provider:
    name: data_provider
    description: Object representing the organization (e.g. MOD) from which the data
      was sourced and a CrossReference to that organisation's site
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    alias: data_provider
    owner: AffectedGenomicModel
    domain_of:
    - DiseaseAnnotation
    - AffectedGenomicModel
    range: DataProvider
  references:
    name: references
    description: holds between an object and a list of references
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    singular_name: reference
    multivalued: true
    alias: references
    owner: AffectedGenomicModel
    domain_of:
    - Allele
    - Construct
    - SequenceTargetingReagent
    - SequenceTargetingReagentToGeneAssociation
    - AffectedGenomicModel
    - Antibody
    range: Reference
  cross_references:
    name: cross_references
    description: Holds between an object and its CrossReferences.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    aliases:
    - xrefs
    singular_name: cross_reference
    multivalued: true
    alias: cross_references
    owner: AffectedGenomicModel
    domain_of:
    - OntologyTerm
    - GenomicEntity
    - AuthorReference
    - Antibody
    - GeneInteraction
    range: CrossReference
  secondary_identifiers:
    name: secondary_identifiers
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    aliases:
    - secondary_ids
    multivalued: true
    alias: secondary_identifiers
    owner: AffectedGenomicModel
    domain_of:
    - OntologyTerm
    - GenomicEntity
    - GenomicEntityDTO
    - Figure
    - Image
    - Antibody
    range: uriorcurie
  genomic_location_associations:
    name: genomic_location_associations
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: GenomicEntity
    multivalued: true
    alias: genomic_location_associations
    owner: AffectedGenomicModel
    domain_of:
    - GenomicEntity
    range: GenomicLocationAssociation
  curie:
    name: curie
    description: A unique identifier for a thing. Must be either a CURIE shorthand
      for a URI or a complete URI
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    identifier: true
    alias: curie
    owner: AffectedGenomicModel
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
  taxon:
    name: taxon
    description: The taxon from which the biological entity derives.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    alias: taxon
    owner: AffectedGenomicModel
    domain_of:
    - BiologicalEntity
    range: NCBITaxonTerm
    required: true
  created_by:
    name: created_by
    description: The individual that created the entity.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObject
    multivalued: false
    alias: created_by
    owner: AffectedGenomicModel
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
    owner: AffectedGenomicModel
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
    owner: AffectedGenomicModel
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
    owner: AffectedGenomicModel
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
    owner: AffectedGenomicModel
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
    owner: AffectedGenomicModel
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
    owner: AffectedGenomicModel
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
    owner: AffectedGenomicModel
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>