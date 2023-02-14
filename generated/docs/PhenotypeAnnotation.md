# PhenotypeAnnotation

An annotation asserting an association between a biological entity and a phenotype supported by evidence.


```mermaid
 classDiagram
      Association <|-- PhenotypeAnnotation
      
      PhenotypeAnnotation : condition_relations
      PhenotypeAnnotation : created_by
      PhenotypeAnnotation : curie
      PhenotypeAnnotation : date_created
      PhenotypeAnnotation : date_updated
      PhenotypeAnnotation : db_date_created
      PhenotypeAnnotation : db_date_updated
      PhenotypeAnnotation : evidence
      PhenotypeAnnotation : internal
      PhenotypeAnnotation : object
      PhenotypeAnnotation : obsolete
      PhenotypeAnnotation : phenotype_term
      PhenotypeAnnotation : predicate
      PhenotypeAnnotation : single_reference
      PhenotypeAnnotation : subject
      PhenotypeAnnotation : updated_by
      

```



URI: [alliance:PhenotypeAnnotation](http://alliancegenome.org/PhenotypeAnnotation)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * [Association](Association.md)
        * **PhenotypeAnnotation**
            * [GenePhenotypeAnnotation](GenePhenotypeAnnotation.md)
            * [AllelePhenotypeAnnotation](AllelePhenotypeAnnotation.md)
            * [AGMPhenotypeAnnotation](AGMPhenotypeAnnotation.md)





## Children

* [AuditedObject](AuditedObject.md)
    * [Association](Association.md)
        * **PhenotypeAnnotation**
            * [GenePhenotypeAnnotation](GenePhenotypeAnnotation.md)
            * [AllelePhenotypeAnnotation](AllelePhenotypeAnnotation.md)
            * [AGMPhenotypeAnnotation](AGMPhenotypeAnnotation.md)



## Slots

| Name | Description  |
| ---  | ---  |
| [condition_relations](condition_relations.md) | None |
| [created_by](created_by.md) | The individual that created the entity. |
| [curie](curie.md) | A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI |
| [date_created](date_created.md) | The date of curation at the source (MOD) database. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [evidence](evidence.md) |  |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [object](object.md) | phenotype statement: The label of an individual phenotype term from a phenotype ontology or the post-composed statement of the phenotype from a post-composed terminology |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [phenotype_term](phenotype_term.md) | The phenotype ontology term used to describe the phenotype of an organism or a set of organisms. |
| [predicate](predicate.md) | A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type. |
| [single_reference](single_reference.md) | The reference in which the phenotype association was asserted/reported. |
| [subject](subject.md) | The biological entity (e.g. gene, allele, genotype) to which the phenotype is associated, by direct curation. |
| [updated_by](updated_by.md) | The individual that last modified the entity. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:PhenotypeAnnotation'] |
| native | ['alliance:PhenotypeAnnotation'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PhenotypeAnnotation
description: An annotation asserting an association between a biological entity and
  a phenotype supported by evidence.
from_schema: https://github.com/alliance-genome/agr_persistent_schema/phenotypeAndDiseaseAnnotation.yaml
is_a: Association
slots:
- curie
- single_reference
- phenotype_term
- condition_relations
slot_usage:
  subject:
    name: subject
    description: The biological entity (e.g. gene, allele, genotype) to which the
      phenotype is associated, by direct curation.
    domain_of:
    - Association
    - VariantConsequence
    range: BiologicalEntity
    required: true
  phenotype_term:
    name: phenotype_term
    examples:
    - value: HP:0002487
      description: Hyperkinesis
    - value: WBPhenotype:0000180
      description: axon morphology variant
    - value: MP:0001569
      description: abnormal circulating bilirubin level
    values_from:
    - HP
    - MP
    - WBPhenotype
    - ZP
    - APO
    - FBcv
    domain_of:
    - AlleleFunctionalImpactSlotAnnotation
    - AlleleInheritanceModeSlotAnnotation
    - PhenotypeAnnotation
    range: PhenotypeTerm
  object:
    name: object
    description: 'phenotype statement: The label of an individual phenotype term from
      a phenotype ontology or the post-composed statement of the phenotype from a
      post-composed terminology'
    domain_of:
    - Association
    - VariantConsequence
    range: string
    required: true
  single_reference:
    name: single_reference
    description: The reference in which the phenotype association was asserted/reported.
    domain_of:
    - SourceVariantLocation
    - VariantLocation
    - PhenotypeAnnotation
    - DiseaseAnnotation
    - ConditionRelation
    - Figure
    - GeneToGeneOrthologyCurated
    - ExpressionExperiment
    - FunctionalGeneSet
  date_created:
    name: date_created
    description: The date of curation at the source (MOD) database.
    multivalued: false
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    required: true

```
</details>

### Induced

<details>
```yaml
name: PhenotypeAnnotation
description: An annotation asserting an association between a biological entity and
  a phenotype supported by evidence.
from_schema: https://github.com/alliance-genome/agr_persistent_schema/phenotypeAndDiseaseAnnotation.yaml
is_a: Association
slot_usage:
  subject:
    name: subject
    description: The biological entity (e.g. gene, allele, genotype) to which the
      phenotype is associated, by direct curation.
    domain_of:
    - Association
    - VariantConsequence
    range: BiologicalEntity
    required: true
  phenotype_term:
    name: phenotype_term
    examples:
    - value: HP:0002487
      description: Hyperkinesis
    - value: WBPhenotype:0000180
      description: axon morphology variant
    - value: MP:0001569
      description: abnormal circulating bilirubin level
    values_from:
    - HP
    - MP
    - WBPhenotype
    - ZP
    - APO
    - FBcv
    domain_of:
    - AlleleFunctionalImpactSlotAnnotation
    - AlleleInheritanceModeSlotAnnotation
    - PhenotypeAnnotation
    range: PhenotypeTerm
  object:
    name: object
    description: 'phenotype statement: The label of an individual phenotype term from
      a phenotype ontology or the post-composed statement of the phenotype from a
      post-composed terminology'
    domain_of:
    - Association
    - VariantConsequence
    range: string
    required: true
  single_reference:
    name: single_reference
    description: The reference in which the phenotype association was asserted/reported.
    domain_of:
    - SourceVariantLocation
    - VariantLocation
    - PhenotypeAnnotation
    - DiseaseAnnotation
    - ConditionRelation
    - Figure
    - GeneToGeneOrthologyCurated
    - ExpressionExperiment
    - FunctionalGeneSet
  date_created:
    name: date_created
    description: The date of curation at the source (MOD) database.
    multivalued: false
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    required: true
attributes:
  curie:
    name: curie
    description: A unique identifier for a thing. Must be either a CURIE shorthand
      for a URI or a complete URI
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    identifier: true
    alias: curie
    owner: PhenotypeAnnotation
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
  single_reference:
    name: single_reference
    description: The reference in which the phenotype association was asserted/reported.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    alias: single_reference
    owner: PhenotypeAnnotation
    domain_of:
    - SourceVariantLocation
    - VariantLocation
    - PhenotypeAnnotation
    - DiseaseAnnotation
    - ConditionRelation
    - Figure
    - GeneToGeneOrthologyCurated
    - ExpressionExperiment
    - FunctionalGeneSet
    range: Reference
  phenotype_term:
    name: phenotype_term
    description: The phenotype ontology term used to describe the phenotype of an
      organism or a set of organisms.
    examples:
    - value: HP:0002487
      description: Hyperkinesis
    - value: WBPhenotype:0000180
      description: axon morphology variant
    - value: MP:0001569
      description: abnormal circulating bilirubin level
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/phenotypeAndDiseaseAnnotation.yaml
    values_from:
    - HP
    - MP
    - WBPhenotype
    - ZP
    - APO
    - FBcv
    multivalued: false
    alias: phenotype_term
    owner: PhenotypeAnnotation
    domain_of:
    - AlleleFunctionalImpactSlotAnnotation
    - AlleleInheritanceModeSlotAnnotation
    - PhenotypeAnnotation
    range: PhenotypeTerm
  condition_relations:
    name: condition_relations
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/phenotypeAndDiseaseAnnotation.yaml
    multivalued: true
    alias: condition_relations
    owner: PhenotypeAnnotation
    domain_of:
    - PhenotypeAnnotation
    - DiseaseAnnotation
    - ExpressionExperiment
    range: ConditionRelation
  subject:
    name: subject
    description: The biological entity (e.g. gene, allele, genotype) to which the
      phenotype is associated, by direct curation.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    is_a: association_slot
    alias: subject
    owner: PhenotypeAnnotation
    domain_of:
    - Association
    - VariantConsequence
    range: BiologicalEntity
    required: true
  predicate:
    name: predicate
    description: A high-level grouping for the relationship type. This is analogous
      to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j
      this corresponds to the relationship type.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    exact_mappings:
    - biolink:predicate
    is_a: association_slot
    alias: predicate
    owner: PhenotypeAnnotation
    domain_of:
    - Association
    - GeneToGeneOrthology
    range: string
    required: true
  object:
    name: object
    description: 'phenotype statement: The label of an individual phenotype term from
      a phenotype ontology or the post-composed statement of the phenotype from a
      post-composed terminology'
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    is_a: association_slot
    alias: object
    owner: PhenotypeAnnotation
    domain_of:
    - Association
    - VariantConsequence
    range: string
    required: true
  evidence:
    name: evidence
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/reference
    multivalued: true
    alias: evidence
    owner: PhenotypeAnnotation
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
    owner: PhenotypeAnnotation
    domain_of:
    - AuditedObject
    range: Person
  date_created:
    name: date_created
    description: The date of curation at the source (MOD) database.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    alias: date_created
    owner: PhenotypeAnnotation
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
    owner: PhenotypeAnnotation
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
    owner: PhenotypeAnnotation
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
    owner: PhenotypeAnnotation
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
    owner: PhenotypeAnnotation
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
    owner: PhenotypeAnnotation
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
    owner: PhenotypeAnnotation
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>