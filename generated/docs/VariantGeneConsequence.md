# VariantGeneConsequence

Class for gene-level VEP results


```mermaid
 classDiagram
      VariantConsequence <|-- VariantGeneConsequence
      
      VariantGeneConsequence : created_by
      VariantGeneConsequence : date_created
      VariantGeneConsequence : date_updated
      VariantGeneConsequence : db_date_created
      VariantGeneConsequence : db_date_updated
      VariantGeneConsequence : internal
      VariantGeneConsequence : object
      VariantGeneConsequence : obsolete
      VariantGeneConsequence : polyphen_prediction
      VariantGeneConsequence : polyphen_score
      VariantGeneConsequence : sift_prediction
      VariantGeneConsequence : sift_score
      VariantGeneConsequence : subject
      VariantGeneConsequence : updated_by
      VariantGeneConsequence : vep_consequence
      VariantGeneConsequence : vep_impact
      

```



URI: [alliance:VariantGeneConsequence](http://alliancegenome.org/VariantGeneConsequence)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * [VariantConsequence](VariantConsequence.md)
        * **VariantGeneConsequence**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [created_by](created_by.md) | The individual that created the entity. |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [object](object.md) | connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object. |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [polyphen_prediction](polyphen_prediction.md) | PolyPhen-2 prediction |
| [polyphen_score](polyphen_score.md) | PolyPhen-2 score between 0 and 1 |
| [sift_prediction](sift_prediction.md) | SIFT prediction |
| [sift_score](sift_score.md) | SIFT score between 0 and 1 |
| [subject](subject.md) | connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object. |
| [updated_by](updated_by.md) | The individual that last modified the entity. |
| [vep_consequence](vep_consequence.md) | VEP consequence |
| [vep_impact](vep_impact.md) | VEP predicted impact of variation on molecule |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:VariantGeneConsequence'] |
| native | ['alliance:VariantGeneConsequence'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VariantGeneConsequence
description: Class for gene-level VEP results
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
aliases:
- GeneLevelConsequence
is_a: VariantConsequence
slot_usage:
  object:
    name: object
    domain_of:
    - Association
    - VariantConsequence
    range: Gene
  subject:
    name: subject
    domain_of:
    - Association
    - VariantConsequence
    range: VariantGenomeLocation

```
</details>

### Induced

<details>
```yaml
name: VariantGeneConsequence
description: Class for gene-level VEP results
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
aliases:
- GeneLevelConsequence
is_a: VariantConsequence
slot_usage:
  object:
    name: object
    domain_of:
    - Association
    - VariantConsequence
    range: Gene
  subject:
    name: subject
    domain_of:
    - Association
    - VariantConsequence
    range: VariantGenomeLocation
attributes:
  subject:
    name: subject
    description: connects an association to the subject of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    is_a: association_slot
    alias: subject
    owner: VariantGeneConsequence
    domain_of:
    - Association
    - VariantConsequence
    range: VariantGenomeLocation
    required: true
  object:
    name: object
    description: connects an association to the object of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    is_a: association_slot
    alias: object
    owner: VariantGeneConsequence
    domain_of:
    - Association
    - VariantConsequence
    range: Gene
    required: true
  vep_consequence:
    name: vep_consequence
    description: VEP consequence
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    alias: vep_consequence
    owner: VariantGeneConsequence
    domain_of:
    - VariantConsequence
    range: vep_consequence_levels
  vep_impact:
    name: vep_impact
    description: VEP predicted impact of variation on molecule
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    alias: vep_impact
    owner: VariantGeneConsequence
    domain_of:
    - VariantConsequence
    range: string
  polyphen_score:
    name: polyphen_score
    description: PolyPhen-2 score between 0 and 1
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    domain: VariantGeneConsequence
    alias: polyphen_score
    owner: VariantGeneConsequence
    domain_of:
    - VariantConsequence
    range: float
  polyphen_prediction:
    name: polyphen_prediction
    description: PolyPhen-2 prediction
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    alias: polyphen_prediction
    owner: VariantGeneConsequence
    domain_of:
    - VariantConsequence
    range: polyphen_prediction_levels
  sift_score:
    name: sift_score
    description: SIFT score between 0 and 1
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    domain: VariantGeneConsequence
    alias: sift_score
    owner: VariantGeneConsequence
    domain_of:
    - VariantConsequence
    range: float
  sift_prediction:
    name: sift_prediction
    description: SIFT prediction
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    alias: sift_prediction
    owner: VariantGeneConsequence
    domain_of:
    - VariantConsequence
    range: sift_prediction_levels
  created_by:
    name: created_by
    description: The individual that created the entity.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObject
    multivalued: false
    alias: created_by
    owner: VariantGeneConsequence
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
    owner: VariantGeneConsequence
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
    owner: VariantGeneConsequence
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
    owner: VariantGeneConsequence
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
    owner: VariantGeneConsequence
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
    owner: VariantGeneConsequence
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
    owner: VariantGeneConsequence
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
    owner: VariantGeneConsequence
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>