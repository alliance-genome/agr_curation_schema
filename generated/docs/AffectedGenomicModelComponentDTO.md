# AffectedGenomicModelComponentDTO

None


```mermaid
 classDiagram
      AuditedObjectDTO <|-- AffectedGenomicModelComponentDTO
      
      AffectedGenomicModelComponentDTO : allele_curie
      AffectedGenomicModelComponentDTO : created_by_curie
      AffectedGenomicModelComponentDTO : date_created
      AffectedGenomicModelComponentDTO : date_updated
      AffectedGenomicModelComponentDTO : db_date_created
      AffectedGenomicModelComponentDTO : db_date_updated
      AffectedGenomicModelComponentDTO : internal
      AffectedGenomicModelComponentDTO : obsolete
      AffectedGenomicModelComponentDTO : updated_by_curie
      AffectedGenomicModelComponentDTO : zygosity_curie
      

```



URI: [alliance:AffectedGenomicModelComponentDTO](http://alliancegenome.org/AffectedGenomicModelComponentDTO)


## Parent Classes

* [AuditedObjectDTO](AuditedObjectDTO.md)
    * **AffectedGenomicModelComponentDTO**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [allele_curie](allele_curie.md) | None |
| [created_by_curie](created_by_curie.md) | Curie of the Person object representing the individual that created the entity |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [updated_by_curie](updated_by_curie.md) | Curie of the Person object representing the individual that updated the entity |
| [zygosity_curie](zygosity_curie.md) | Curie of GENO ontology ID for allele zygosity - permissible_values: GENO:0000602 / GENO:0000603 / GENO:0000604 / GENO:0000605 / GENO:0000606 / GENO:0000135 / GENO:0000136 / GENO:0000137 / GENO:0000134 |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:AffectedGenomicModelComponentDTO'] |
| native | ['alliance:AffectedGenomicModelComponentDTO'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AffectedGenomicModelComponentDTO
from_schema: https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel
is_a: AuditedObjectDTO
slots:
- allele_curie
- zygosity_curie

```
</details>

### Induced

<details>
```yaml
name: AffectedGenomicModelComponentDTO
from_schema: https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel
is_a: AuditedObjectDTO
attributes:
  allele_curie:
    name: allele_curie
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/alleleDTO
    alias: allele_curie
    owner: AffectedGenomicModelComponentDTO
    domain_of:
    - AlleleDiseaseAnnotationDTO
    - AlleleCellLineAssociationDTO
    - AlleleGenerationMethodAssociationDTO
    - AlleleGenomicEntityAssociationDTO
    - AlleleImageAssociationDTO
    - AlleleOriginAssociationDTO
    - AffectedGenomicModelComponentDTO
    range: string
    required: true
  zygosity_curie:
    name: zygosity_curie
    description: 'Curie of GENO ontology ID for allele zygosity - permissible_values:
      GENO:0000602 / GENO:0000603 / GENO:0000604 / GENO:0000605 / GENO:0000606 / GENO:0000135
      / GENO:0000136 / GENO:0000137 / GENO:0000134'
    from_schema: https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel
    domain: AffectedGenomicModelComponentDTO
    alias: zygosity_curie
    owner: AffectedGenomicModelComponentDTO
    domain_of:
    - AffectedGenomicModelComponentDTO
    range: string
  created_by_curie:
    name: created_by_curie
    description: Curie of the Person object representing the individual that created
      the entity
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObjectDTO
    alias: created_by_curie
    owner: AffectedGenomicModelComponentDTO
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
    owner: AffectedGenomicModelComponentDTO
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
    owner: AffectedGenomicModelComponentDTO
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
    owner: AffectedGenomicModelComponentDTO
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
    owner: AffectedGenomicModelComponentDTO
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
    owner: AffectedGenomicModelComponentDTO
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
    owner: AffectedGenomicModelComponentDTO
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
    owner: AffectedGenomicModelComponentDTO
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>