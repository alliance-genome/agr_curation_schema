# GeneNomenclatureSet

WB specific. A gene class is a set of genes which share nomenclature, belonging to the same gene class.


```mermaid
 classDiagram
      AuditedObject <|-- GeneNomenclatureSet
      
      GeneNomenclatureSet : created_by
      GeneNomenclatureSet : curie
      GeneNomenclatureSet : date_created
      GeneNomenclatureSet : date_updated
      GeneNomenclatureSet : db_date_created
      GeneNomenclatureSet : db_date_updated
      GeneNomenclatureSet : designating_laboratory
      GeneNomenclatureSet : genes
      GeneNomenclatureSet : internal
      GeneNomenclatureSet : obsolete
      GeneNomenclatureSet : old_members
      GeneNomenclatureSet : related_note
      GeneNomenclatureSet : synonyms
      GeneNomenclatureSet : updated_by
      

```



URI: [alliance:GeneNomenclatureSet](http://alliancegenome.org/GeneNomenclatureSet)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * **GeneNomenclatureSet**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [created_by](created_by.md) | The individual that created the entity. |
| [curie](curie.md) | A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [designating_laboratory](designating_laboratory.md) | A laboratory which designated this gene class |
| [genes](genes.md) | None |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [old_members](old_members.md) | Gene which were formerly members of this GeneClass |
| [related_note](related_note.md) | Holds between an object and a Note object. |
| [synonyms](synonyms.md) | Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence). |
| [updated_by](updated_by.md) | The individual that last modified the entity. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:GeneNomenclatureSet'] |
| native | ['alliance:GeneNomenclatureSet'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneNomenclatureSet
description: WB specific. A gene class is a set of genes which share nomenclature,
  belonging to the same gene class.
from_schema: https://github.com/alliance-genome/agr_curation_schema/biologicalEntitySet.yaml
is_a: AuditedObject
slots:
- genes
- curie
- designating_laboratory
- old_members
- synonyms
- related_note

```
</details>

### Induced

<details>
```yaml
name: GeneNomenclatureSet
description: WB specific. A gene class is a set of genes which share nomenclature,
  belonging to the same gene class.
from_schema: https://github.com/alliance-genome/agr_curation_schema/biologicalEntitySet.yaml
is_a: AuditedObject
attributes:
  genes:
    name: genes
    from_schema: https://github.com/alliance-genome/agr_curation_schema/biologicalEntitySet.yaml
    multivalued: true
    alias: genes
    owner: GeneNomenclatureSet
    domain_of:
    - GeneCluster
    - GeneCollection
    - GeneNomenclatureSet
    - Operon
    - UniGeneSet
    - FunctionalGeneSet
    range: Gene
  curie:
    name: curie
    description: A unique identifier for a thing. Must be either a CURIE shorthand
      for a URI or a complete URI
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    identifier: true
    alias: curie
    owner: GeneNomenclatureSet
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
  designating_laboratory:
    name: designating_laboratory
    description: A laboratory which designated this gene class
    from_schema: https://github.com/alliance-genome/agr_curation_schema/biologicalEntitySet.yaml
    domain: Gene
    multivalued: false
    alias: designating_laboratory
    owner: GeneNomenclatureSet
    domain_of:
    - GeneNomenclatureSet
    range: Laboratory
    required: true
  old_members:
    name: old_members
    description: Gene which were formerly members of this GeneClass
    from_schema: https://github.com/alliance-genome/agr_curation_schema/biologicalEntitySet.yaml
    domain: GeneNomenclatureSet
    multivalued: true
    alias: old_members
    owner: GeneNomenclatureSet
    domain_of:
    - GeneNomenclatureSet
    range: Gene
    required: false
  synonyms:
    name: synonyms
    description: Placeholder? Some objects still use this slot. Not clear how it fits
      in with NameSlotAnnotation (which captures evidence).
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: true
    alias: synonyms
    owner: GeneNomenclatureSet
    domain_of:
    - OntologyTerm
    - ResourceDescriptor
    - Resource
    - GeneNomenclatureSet
    range: string
    required: false
  related_note:
    name: related_note
    description: Holds between an object and a Note object.
    notes:
    - Singular version of related_notes
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    alias: related_note
    owner: GeneNomenclatureSet
    domain_of:
    - AlleleNoteSlotAnnotation
    - AlleleGenomicEntityAssociation
    - GeneCluster
    - GeneCollection
    - GeneNomenclatureSet
    - Operon
    range: Note
  created_by:
    name: created_by
    description: The individual that created the entity.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObject
    multivalued: false
    alias: created_by
    owner: GeneNomenclatureSet
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
    owner: GeneNomenclatureSet
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
    owner: GeneNomenclatureSet
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
    owner: GeneNomenclatureSet
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
    owner: GeneNomenclatureSet
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
    owner: GeneNomenclatureSet
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
    owner: GeneNomenclatureSet
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
    owner: GeneNomenclatureSet
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>