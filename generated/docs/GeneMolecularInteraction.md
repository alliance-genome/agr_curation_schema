# GeneMolecularInteraction

A physical molecular interaction between gene products (e.g. protein-protein interactions or protein-RNA interactions) or between genes and DNA-binding factors (e.g. protein-DNA interactions)


```mermaid
 classDiagram
      GeneInteraction <|-- GeneMolecularInteraction
      
      GeneMolecularInteraction : aggregation_database
      GeneMolecularInteraction : created_by
      GeneMolecularInteraction : cross_references
      GeneMolecularInteraction : curie
      GeneMolecularInteraction : date_created
      GeneMolecularInteraction : date_updated
      GeneMolecularInteraction : db_date_created
      GeneMolecularInteraction : db_date_updated
      GeneMolecularInteraction : detection_method
      GeneMolecularInteraction : evidence
      GeneMolecularInteraction : interaction_data_provider
      GeneMolecularInteraction : interaction_type
      GeneMolecularInteraction : interactor_A_role
      GeneMolecularInteraction : interactor_A_type
      GeneMolecularInteraction : interactor_B_role
      GeneMolecularInteraction : interactor_B_type
      GeneMolecularInteraction : internal
      GeneMolecularInteraction : object
      GeneMolecularInteraction : obsolete
      GeneMolecularInteraction : predicate
      GeneMolecularInteraction : subject
      GeneMolecularInteraction : updated_by
      

```



URI: [alliance:GeneMolecularInteraction](http://alliancegenome.org/GeneMolecularInteraction)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * [Association](Association.md)
        * [GeneToGeneAssociation](GeneToGeneAssociation.md)
            * [GeneInteraction](GeneInteraction.md)
                * **GeneMolecularInteraction**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [aggregation_database](aggregation_database.md) | The database that collected the interaction annotation from another resource and aggregated it into a consolidated resource. e.g. IMEx |
| [created_by](created_by.md) | The individual that created the entity. |
| [cross_references](cross_references.md) | Holds between an object and its CrossReferences. |
| [curie](curie.md) | A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [detection_method](detection_method.md) | The experimental method used to identify the physical interaction between two molecules |
| [evidence](evidence.md) |  |
| [interaction_data_provider](interaction_data_provider.md) | The interaction database that curated the interaction. e.g. BioGRID |
| [interaction_type](interaction_type.md) | The type of interaction between the two genes or gene products. e.g. physical association |
| [interactor_A_role](interactor_A_role.md) | None |
| [interactor_A_type](interactor_A_type.md) | None |
| [interactor_B_role](interactor_B_role.md) | None |
| [interactor_B_type](interactor_B_type.md) | None |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [object](object.md) | connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object. |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [predicate](predicate.md) | A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type. |
| [subject](subject.md) | connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object. |
| [updated_by](updated_by.md) | The individual that last modified the entity. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:GeneMolecularInteraction'] |
| native | ['alliance:GeneMolecularInteraction'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneMolecularInteraction
description: A physical molecular interaction between gene products (e.g. protein-protein
  interactions or protein-RNA interactions) or between genes and DNA-binding factors
  (e.g. protein-DNA interactions)
from_schema: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
is_a: GeneInteraction
slots:
- aggregation_database
- detection_method
slot_usage:
  aggregation_database:
    name: aggregation_database
    description: The database that collected the interaction annotation from another
      resource and aggregated it into a consolidated resource. e.g. IMEx
    domain_of:
    - GeneMolecularInteraction
    range: aggregation_database_enum
  detection_method:
    name: detection_method
    description: The experimental method used to identify the physical interaction
      between two molecules
    domain_of:
    - GeneMolecularInteraction
    range: detection_methods_enum
  predicate:
    name: predicate
    domain_of:
    - Association
    - GeneToGeneOrthology
    subproperty_of: physically_interacts_with
    symmetric: true

```
</details>

### Induced

<details>
```yaml
name: GeneMolecularInteraction
description: A physical molecular interaction between gene products (e.g. protein-protein
  interactions or protein-RNA interactions) or between genes and DNA-binding factors
  (e.g. protein-DNA interactions)
from_schema: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
is_a: GeneInteraction
slot_usage:
  aggregation_database:
    name: aggregation_database
    description: The database that collected the interaction annotation from another
      resource and aggregated it into a consolidated resource. e.g. IMEx
    domain_of:
    - GeneMolecularInteraction
    range: aggregation_database_enum
  detection_method:
    name: detection_method
    description: The experimental method used to identify the physical interaction
      between two molecules
    domain_of:
    - GeneMolecularInteraction
    range: detection_methods_enum
  predicate:
    name: predicate
    domain_of:
    - Association
    - GeneToGeneOrthology
    subproperty_of: physically_interacts_with
    symmetric: true
attributes:
  aggregation_database:
    name: aggregation_database
    description: The database that collected the interaction annotation from another
      resource and aggregated it into a consolidated resource. e.g. IMEx
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
    multivalued: false
    alias: aggregation_database
    owner: GeneMolecularInteraction
    domain_of:
    - GeneMolecularInteraction
    range: aggregation_database_enum
    required: false
  detection_method:
    name: detection_method
    description: The experimental method used to identify the physical interaction
      between two molecules
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
    alias: detection_method
    owner: GeneMolecularInteraction
    domain_of:
    - GeneMolecularInteraction
    range: detection_methods_enum
  curie:
    name: curie
    description: A unique identifier for a thing. Must be either a CURIE shorthand
      for a URI or a complete URI
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    identifier: true
    alias: curie
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
    domain_of:
    - Association
    - GeneToGeneOrthology
    subproperty_of: physically_interacts_with
    symmetric: true
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
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
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
    owner: GeneMolecularInteraction
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>