# ExperimentalConditionDTO

Ingest class for describing the environmental context in which an experiment is carried out


```mermaid
 classDiagram
      AuditedObjectDTO <|-- ExperimentalConditionDTO
      
      ExperimentalConditionDTO : condition_anatomy_curie
      ExperimentalConditionDTO : condition_chemical_curie
      ExperimentalConditionDTO : condition_class_curie
      ExperimentalConditionDTO : condition_free_text
      ExperimentalConditionDTO : condition_gene_ontology_curie
      ExperimentalConditionDTO : condition_id_curie
      ExperimentalConditionDTO : condition_quantity
      ExperimentalConditionDTO : condition_taxon_curie
      ExperimentalConditionDTO : created_by_curie
      ExperimentalConditionDTO : date_created
      ExperimentalConditionDTO : date_updated
      ExperimentalConditionDTO : db_date_created
      ExperimentalConditionDTO : db_date_updated
      ExperimentalConditionDTO : internal
      ExperimentalConditionDTO : obsolete
      ExperimentalConditionDTO : updated_by_curie
      

```



URI: [alliance:ExperimentalConditionDTO](http://alliancegenome.org/ExperimentalConditionDTO)


## Parent Classes

* [AuditedObjectDTO](AuditedObjectDTO.md)
    * **ExperimentalConditionDTO**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [condition_anatomy_curie](condition_anatomy_curie.md) | Curie of AnatomicalTerm associated with condition |
| [condition_chemical_curie](condition_chemical_curie.md) | Curie of ChemicalTerm associated with condition |
| [condition_class_curie](condition_class_curie.md) | Curie of ZECOTerm describing condition class |
| [condition_free_text](condition_free_text.md) | Free-text description of the experimental condition |
| [condition_gene_ontology_curie](condition_gene_ontology_curie.md) | Curie of GOTerm associated with condition |
| [condition_id_curie](condition_id_curie.md) | Curie of ExperimentalConditionOntologyTerm describing condition |
| [condition_quantity](condition_quantity.md) | None |
| [condition_taxon_curie](condition_taxon_curie.md) | Curie of NCBITaxonTerm associated with condition |
| [created_by_curie](created_by_curie.md) | Curie of the Person object representing the individual that created the entity |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [updated_by_curie](updated_by_curie.md) | Curie of the Person object representing the individual that updated the entity |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:ExperimentalConditionDTO'] |
| native | ['alliance:ExperimentalConditionDTO'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExperimentalConditionDTO
description: Ingest class for describing the environmental context in which an experiment
  is carried out
from_schema: https://github.com/alliance-genome/agr_persistent_schema/phenotypeAndDiseaseAnnotation.yaml
is_a: AuditedObjectDTO
slots:
- condition_class_curie
- condition_id_curie
- condition_free_text
- condition_quantity
- condition_anatomy_curie
- condition_gene_ontology_curie
- condition_taxon_curie
- condition_chemical_curie

```
</details>

### Induced

<details>
```yaml
name: ExperimentalConditionDTO
description: Ingest class for describing the environmental context in which an experiment
  is carried out
from_schema: https://github.com/alliance-genome/agr_persistent_schema/phenotypeAndDiseaseAnnotation.yaml
is_a: AuditedObjectDTO
attributes:
  condition_class_curie:
    name: condition_class_curie
    description: Curie of ZECOTerm describing condition class
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/phenotypeAndDiseaseAnnotation.yaml
    domain: ExperimentalConditionDTO
    alias: condition_class_curie
    owner: ExperimentalConditionDTO
    domain_of:
    - ExperimentalConditionDTO
    range: string
    required: true
  condition_id_curie:
    name: condition_id_curie
    description: Curie of ExperimentalConditionOntologyTerm describing condition
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/phenotypeAndDiseaseAnnotation.yaml
    domain: ExperimentalConditionDTO
    alias: condition_id_curie
    owner: ExperimentalConditionDTO
    domain_of:
    - ExperimentalConditionDTO
    range: string
  condition_free_text:
    name: condition_free_text
    description: Free-text description of the experimental condition
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/phenotypeAndDiseaseAnnotation.yaml
    domain: ExperimentalCondition
    alias: condition_free_text
    owner: ExperimentalConditionDTO
    domain_of:
    - ExperimentalCondition
    - ExperimentalConditionDTO
    range: string
    required: false
  condition_quantity:
    name: condition_quantity
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/phenotypeAndDiseaseAnnotation.yaml
    domain: ExperimentalCondition
    alias: condition_quantity
    owner: ExperimentalConditionDTO
    domain_of:
    - ExperimentalCondition
    - ExperimentalConditionDTO
    range: string
  condition_anatomy_curie:
    name: condition_anatomy_curie
    description: Curie of AnatomicalTerm associated with condition
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/phenotypeAndDiseaseAnnotation.yaml
    domain: ExperimentalConditionDTO
    alias: condition_anatomy_curie
    owner: ExperimentalConditionDTO
    domain_of:
    - ExperimentalConditionDTO
    range: string
  condition_gene_ontology_curie:
    name: condition_gene_ontology_curie
    description: Curie of GOTerm associated with condition
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/phenotypeAndDiseaseAnnotation.yaml
    domain: ExperimentalConditionDTO
    alias: condition_gene_ontology_curie
    owner: ExperimentalConditionDTO
    domain_of:
    - ExperimentalConditionDTO
    range: string
  condition_taxon_curie:
    name: condition_taxon_curie
    description: Curie of NCBITaxonTerm associated with condition
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/phenotypeAndDiseaseAnnotation.yaml
    domain: ExperimentalConditionDTO
    alias: condition_taxon_curie
    owner: ExperimentalConditionDTO
    domain_of:
    - ExperimentalConditionDTO
    range: string
  condition_chemical_curie:
    name: condition_chemical_curie
    description: Curie of ChemicalTerm associated with condition
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/phenotypeAndDiseaseAnnotation.yaml
    domain: ExperimentalConditionDTO
    alias: condition_chemical_curie
    owner: ExperimentalConditionDTO
    domain_of:
    - ExperimentalConditionDTO
    range: string
  created_by_curie:
    name: created_by_curie
    description: Curie of the Person object representing the individual that created
      the entity
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObjectDTO
    alias: created_by_curie
    owner: ExperimentalConditionDTO
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
    owner: ExperimentalConditionDTO
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
    owner: ExperimentalConditionDTO
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
    owner: ExperimentalConditionDTO
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
    owner: ExperimentalConditionDTO
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
    owner: ExperimentalConditionDTO
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
    owner: ExperimentalConditionDTO
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
    owner: ExperimentalConditionDTO
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>