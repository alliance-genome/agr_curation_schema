# GeneGeneticInteraction

A genetic interaction between genes (e.g. phenotypic suppression)


```mermaid
 classDiagram
      GeneInteraction <|-- GeneGeneticInteraction
      
      GeneGeneticInteraction : created_by
      GeneGeneticInteraction : cross_references
      GeneGeneticInteraction : curie
      GeneGeneticInteraction : date_created
      GeneGeneticInteraction : date_updated
      GeneGeneticInteraction : db_date_created
      GeneGeneticInteraction : db_date_updated
      GeneGeneticInteraction : evidence
      GeneGeneticInteraction : interaction_data_provider
      GeneGeneticInteraction : interaction_type
      GeneGeneticInteraction : interactor_A_genetic_perturbation
      GeneGeneticInteraction : interactor_A_role
      GeneGeneticInteraction : interactor_A_type
      GeneGeneticInteraction : interactor_B_genetic_perturbation
      GeneGeneticInteraction : interactor_B_role
      GeneGeneticInteraction : interactor_B_type
      GeneGeneticInteraction : internal
      GeneGeneticInteraction : object
      GeneGeneticInteraction : obsolete
      GeneGeneticInteraction : phenotype_or_trait
      GeneGeneticInteraction : predicate
      GeneGeneticInteraction : subject
      GeneGeneticInteraction : updated_by
      

```



URI: [alliance:GeneGeneticInteraction](http://alliancegenome.org/GeneGeneticInteraction)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * [Association](Association.md)
        * [GeneToGeneAssociation](GeneToGeneAssociation.md)
            * [GeneInteraction](GeneInteraction.md)
                * **GeneGeneticInteraction**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [created_by](created_by.md) | The individual that created the entity. |
| [cross_references](cross_references.md) | Holds between an object and its CrossReferences. |
| [curie](curie.md) | A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [evidence](evidence.md) |  |
| [interaction_data_provider](interaction_data_provider.md) | The interaction database that curated the interaction. e.g. BioGRID |
| [interaction_type](interaction_type.md) | The type of interaction between the two genes or gene products. e.g. physical association |
| [interactor_A_genetic_perturbation](interactor_A_genetic_perturbation.md) | None |
| [interactor_A_role](interactor_A_role.md) | None |
| [interactor_A_type](interactor_A_type.md) | None |
| [interactor_B_genetic_perturbation](interactor_B_genetic_perturbation.md) | None |
| [interactor_B_role](interactor_B_role.md) | None |
| [interactor_B_type](interactor_B_type.md) | None |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [object](object.md) | connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object. |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [phenotype_or_trait](phenotype_or_trait.md) | None |
| [predicate](predicate.md) | A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type. |
| [subject](subject.md) | connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object. |
| [updated_by](updated_by.md) | The individual that last modified the entity. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:GeneGeneticInteraction'] |
| native | ['alliance:GeneGeneticInteraction'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneGeneticInteraction
description: A genetic interaction between genes (e.g. phenotypic suppression)
from_schema: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
is_a: GeneInteraction
slots:
- interactor_A_genetic_perturbation
- interactor_B_genetic_perturbation
- phenotype_or_trait
slot_usage:
  predicate:
    name: predicate
    domain_of:
    - Association
    - GeneToGeneOrthology
    subproperty_of: genetically_interacts_with

```
</details>

### Induced

<details>
```yaml
name: GeneGeneticInteraction
description: A genetic interaction between genes (e.g. phenotypic suppression)
from_schema: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
is_a: GeneInteraction
slot_usage:
  predicate:
    name: predicate
    domain_of:
    - Association
    - GeneToGeneOrthology
    subproperty_of: genetically_interacts_with
attributes:
  interactor_A_genetic_perturbation:
    name: interactor_A_genetic_perturbation
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
    is_a: association_slot
    domain: GeneGeneticInteraction
    alias: interactor_A_genetic_perturbation
    owner: GeneGeneticInteraction
    domain_of:
    - GeneGeneticInteraction
    range: Allele
    required: false
  interactor_B_genetic_perturbation:
    name: interactor_B_genetic_perturbation
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
    is_a: association_slot
    domain: GeneGeneticInteraction
    alias: interactor_B_genetic_perturbation
    owner: GeneGeneticInteraction
    domain_of:
    - GeneGeneticInteraction
    range: Allele
    required: false
  phenotype_or_trait:
    name: phenotype_or_trait
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
    domain: GeneGeneticInteraction
    multivalued: true
    alias: phenotype_or_trait
    owner: GeneGeneticInteraction
    domain_of:
    - GeneGeneticInteraction
    range: string
    required: false
  curie:
    name: curie
    description: A unique identifier for a thing. Must be either a CURIE shorthand
      for a URI or a complete URI
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    identifier: true
    alias: curie
    owner: GeneGeneticInteraction
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
  cross_references:
    name: cross_references
    description: Holds between an object and its CrossReferences.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    aliases:
    - xrefs
    singular_name: cross_reference
    multivalued: true
    alias: cross_references
    owner: GeneGeneticInteraction
    domain_of:
    - OntologyTerm
    - GenomicEntity
    - AuthorReference
    - Antibody
    - GeneInteraction
    range: CrossReference
  interaction_data_provider:
    name: interaction_data_provider
    description: The interaction database that curated the interaction. e.g. BioGRID
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
    multivalued: false
    alias: interaction_data_provider
    owner: GeneGeneticInteraction
    domain_of:
    - GeneInteraction
    range: interaction_source_enum
    required: true
  interaction_type:
    name: interaction_type
    description: The type of interaction between the two genes or gene products. e.g.
      physical association
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
    is_a: association_slot
    domain: GeneInteraction
    multivalued: false
    alias: interaction_type
    owner: GeneGeneticInteraction
    domain_of:
    - GeneInteraction
    range: interaction_type_enum
    required: true
  interactor_A_role:
    name: interactor_A_role
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
    is_a: association_slot
    domain: GeneInteraction
    multivalued: true
    alias: interactor_A_role
    owner: GeneGeneticInteraction
    domain_of:
    - GeneInteraction
    range: interactor_A_role_enum
    required: false
  interactor_B_role:
    name: interactor_B_role
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
    is_a: association_slot
    domain: GeneInteraction
    multivalued: true
    alias: interactor_B_role
    owner: GeneGeneticInteraction
    domain_of:
    - GeneInteraction
    range: interactor_B_role_enum
    required: false
  interactor_A_type:
    name: interactor_A_type
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
    is_a: association_slot
    domain: GeneInteraction
    multivalued: false
    alias: interactor_A_type
    owner: GeneGeneticInteraction
    domain_of:
    - GeneInteraction
    range: interactor_type_enum
    required: true
  interactor_B_type:
    name: interactor_B_type
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
    is_a: association_slot
    domain: GeneInteraction
    multivalued: false
    alias: interactor_B_type
    owner: GeneGeneticInteraction
    domain_of:
    - GeneInteraction
    range: interactor_type_enum
    required: true
  subject:
    name: subject
    description: connects an association to the subject of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    exact_mappings:
    - owl:annotatedSource
    - biolink:subject
    is_a: association_slot
    alias: subject
    owner: GeneGeneticInteraction
    domain_of:
    - Association
    - VariantConsequence
    range: Gene
    required: true
  predicate:
    name: predicate
    description: A high-level grouping for the relationship type. This is analogous
      to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j
      this corresponds to the relationship type.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    is_a: association_slot
    alias: predicate
    owner: GeneGeneticInteraction
    domain_of:
    - Association
    - GeneToGeneOrthology
    subproperty_of: genetically_interacts_with
    range: string
    required: true
  object:
    name: object
    description: connects an association to the object of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    exact_mappings:
    - biolink:object
    is_a: association_slot
    alias: object
    owner: GeneGeneticInteraction
    domain_of:
    - Association
    - VariantConsequence
    range: Gene
    required: true
  evidence:
    name: evidence
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/reference
    multivalued: true
    alias: evidence
    owner: GeneGeneticInteraction
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
    owner: GeneGeneticInteraction
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
    owner: GeneGeneticInteraction
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
    owner: GeneGeneticInteraction
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
    owner: GeneGeneticInteraction
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
    owner: GeneGeneticInteraction
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
    owner: GeneGeneticInteraction
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
    owner: GeneGeneticInteraction
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
    owner: GeneGeneticInteraction
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>