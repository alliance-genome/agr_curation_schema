# AlleleFunctionalImpactSlotAnnotationDTO

None


```mermaid
 classDiagram
      SlotAnnotationDTO <|-- AlleleFunctionalImpactSlotAnnotationDTO
      
      AlleleFunctionalImpactSlotAnnotationDTO : created_by_curie
      AlleleFunctionalImpactSlotAnnotationDTO : date_created
      AlleleFunctionalImpactSlotAnnotationDTO : date_updated
      AlleleFunctionalImpactSlotAnnotationDTO : db_date_created
      AlleleFunctionalImpactSlotAnnotationDTO : db_date_updated
      AlleleFunctionalImpactSlotAnnotationDTO : evidence_curies
      AlleleFunctionalImpactSlotAnnotationDTO : functional_impact_names
      AlleleFunctionalImpactSlotAnnotationDTO : internal
      AlleleFunctionalImpactSlotAnnotationDTO : obsolete
      AlleleFunctionalImpactSlotAnnotationDTO : phenotype_statement
      AlleleFunctionalImpactSlotAnnotationDTO : phenotype_term_curie
      AlleleFunctionalImpactSlotAnnotationDTO : updated_by_curie
      

```



URI: [alliance:AlleleFunctionalImpactSlotAnnotationDTO](http://alliancegenome.org/AlleleFunctionalImpactSlotAnnotationDTO)


## Parent Classes

* [AuditedObjectDTO](AuditedObjectDTO.md)
    * [SlotAnnotationDTO](SlotAnnotationDTO.md)
        * **AlleleFunctionalImpactSlotAnnotationDTO**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [created_by_curie](created_by_curie.md) | Curie of the Person object representing the individual that created the entity |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [evidence_curies](evidence_curies.md) | Curies of InformationContentEntity objects given as evidence |
| [functional_impact_names](functional_impact_names.md) | Name of the VocabularyTerm describing the experimentally assessed functional impact of the allele, e.g. knockout / amorphic |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [phenotype_statement](phenotype_statement.md) | For some MODs, the functional impact of an allele is reported specifically in the context of a particular phenotype. This slot is intended to capture the free-text phenotype statement. |
| [phenotype_term_curie](phenotype_term_curie.md) | The string representation of the phenotype ontology term (PhenotypeTerm) curie |
| [updated_by_curie](updated_by_curie.md) | Curie of the Person object representing the individual that updated the entity |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:AlleleFunctionalImpactSlotAnnotationDTO'] |
| native | ['alliance:AlleleFunctionalImpactSlotAnnotationDTO'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AlleleFunctionalImpactSlotAnnotationDTO
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/alleleDTO
is_a: SlotAnnotationDTO
slots:
- functional_impact_names
- phenotype_term_curie
- phenotype_statement
slot_usage:
  phenotype_term:
    name: phenotype_term
    description: For some MODs, the functional impact of an allele is reported specifically
      in the context of a particular phenotype. This slot is intended to capture the
      PhenotypeTerm.
    required: false
  phenotype_statement:
    name: phenotype_statement
    description: For some MODs, the functional impact of an allele is reported specifically
      in the context of a particular phenotype. This slot is intended to capture the
      free-text phenotype statement.
    domain_of:
    - AlleleFunctionalImpactSlotAnnotation
    - AlleleInheritanceModeSlotAnnotation
    - AlleleFunctionalImpactSlotAnnotationDTO
    - AlleleInheritanceModeSlotAnnotationDTO
    required: false

```
</details>

### Induced

<details>
```yaml
name: AlleleFunctionalImpactSlotAnnotationDTO
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/alleleDTO
is_a: SlotAnnotationDTO
slot_usage:
  phenotype_term:
    name: phenotype_term
    description: For some MODs, the functional impact of an allele is reported specifically
      in the context of a particular phenotype. This slot is intended to capture the
      PhenotypeTerm.
    required: false
  phenotype_statement:
    name: phenotype_statement
    description: For some MODs, the functional impact of an allele is reported specifically
      in the context of a particular phenotype. This slot is intended to capture the
      free-text phenotype statement.
    domain_of:
    - AlleleFunctionalImpactSlotAnnotation
    - AlleleInheritanceModeSlotAnnotation
    - AlleleFunctionalImpactSlotAnnotationDTO
    - AlleleInheritanceModeSlotAnnotationDTO
    required: false
attributes:
  functional_impact_names:
    name: functional_impact_names
    description: Name of the VocabularyTerm describing the experimentally assessed
      functional impact of the allele, e.g. knockout / amorphic
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/alleleDTO
    domain: AlleleFunctionalImpactSlotAnnotationDTO
    multivalued: true
    alias: functional_impact_names
    owner: AlleleFunctionalImpactSlotAnnotationDTO
    domain_of:
    - AlleleFunctionalImpactSlotAnnotationDTO
    range: string
    required: true
  phenotype_term_curie:
    name: phenotype_term_curie
    description: The string representation of the phenotype ontology term (PhenotypeTerm)
      curie
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/phenotypeAndDiseaseAnnotation.yaml
    multivalued: false
    alias: phenotype_term_curie
    owner: AlleleFunctionalImpactSlotAnnotationDTO
    domain_of:
    - AlleleFunctionalImpactSlotAnnotationDTO
    - AlleleInheritanceModeSlotAnnotationDTO
    range: string
  phenotype_statement:
    name: phenotype_statement
    description: For some MODs, the functional impact of an allele is reported specifically
      in the context of a particular phenotype. This slot is intended to capture the
      free-text phenotype statement.
    from_schema: https://github.com/alliance-genome/agr_persistent_schema/phenotypeAndDiseaseAnnotation.yaml
    alias: phenotype_statement
    owner: AlleleFunctionalImpactSlotAnnotationDTO
    domain_of:
    - AlleleFunctionalImpactSlotAnnotation
    - AlleleInheritanceModeSlotAnnotation
    - AlleleFunctionalImpactSlotAnnotationDTO
    - AlleleInheritanceModeSlotAnnotationDTO
    range: string
    required: false
  evidence_curies:
    name: evidence_curies
    description: Curies of InformationContentEntity objects given as evidence
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/reference
    multivalued: true
    alias: evidence_curies
    owner: AlleleFunctionalImpactSlotAnnotationDTO
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
  created_by_curie:
    name: created_by_curie
    description: Curie of the Person object representing the individual that created
      the entity
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObjectDTO
    alias: created_by_curie
    owner: AlleleFunctionalImpactSlotAnnotationDTO
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
    owner: AlleleFunctionalImpactSlotAnnotationDTO
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
    owner: AlleleFunctionalImpactSlotAnnotationDTO
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
    owner: AlleleFunctionalImpactSlotAnnotationDTO
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
    owner: AlleleFunctionalImpactSlotAnnotationDTO
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
    owner: AlleleFunctionalImpactSlotAnnotationDTO
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
    owner: AlleleFunctionalImpactSlotAnnotationDTO
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
    owner: AlleleFunctionalImpactSlotAnnotationDTO
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>