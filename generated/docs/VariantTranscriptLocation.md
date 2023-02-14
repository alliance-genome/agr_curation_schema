# VariantTranscriptLocation

Links a variant to a position on a specified transcript and the resulting consequence to the sequence and/or function of that transcript.


```mermaid
 classDiagram
      VariantLocation <|-- VariantTranscriptLocation
      
      VariantTranscriptLocation : consequence
      VariantTranscriptLocation : created_by
      VariantTranscriptLocation : date_created
      VariantTranscriptLocation : date_updated
      VariantTranscriptLocation : db_date_created
      VariantTranscriptLocation : db_date_updated
      VariantTranscriptLocation : end_position
      VariantTranscriptLocation : evidence_code
      VariantTranscriptLocation : internal
      VariantTranscriptLocation : obsolete
      VariantTranscriptLocation : reference_sequence
      VariantTranscriptLocation : single_reference
      VariantTranscriptLocation : start_position
      VariantTranscriptLocation : transcript
      VariantTranscriptLocation : updated_by
      VariantTranscriptLocation : variant_sequence
      

```



URI: [alliance:VariantTranscriptLocation](http://alliancegenome.org/VariantTranscriptLocation)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * [VariantLocation](VariantLocation.md)
        * **VariantTranscriptLocation**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [consequence](consequence.md) | SOTerm (child of SO:0001576 - transcript_variant) that describes the consequence of the variant, as stated in the source reference. In practice source consequence will be associated with locations at any or all of VariantGenomeLocation, VariantTranscriptLocation, and VariantPolypeptideLocation. |
| [created_by](created_by.md) | The individual that created the entity. |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [end_position](end_position.md) | End position of variant on genomic entity. |
| [evidence_code](evidence_code.md) | None |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [reference_sequence](reference_sequence.md) | Reference sequence of genome or genomic entity at position of aligned variant. |
| [single_reference](single_reference.md) | holds between an object and a single reference |
| [start_position](start_position.md) | Start position of variant on genomic entity. |
| [transcript](transcript.md) | Transcript associated with variant and for which a specific location and consequence of that variant is provided, as specified at source.  Multivalued=false for this slot because although a variant can have multiple VariantTranscriptLocation stanzas, each stanza will have one and only one source transcript ID. |
| [updated_by](updated_by.md) | The individual that last modified the entity. |
| [variant_sequence](variant_sequence.md) | Sequence that differs from the reference sequence of genome or genomic entity at position of variant, as specified by curator. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:VariantTranscriptLocation'] |
| native | ['alliance:VariantTranscriptLocation'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VariantTranscriptLocation
description: Links a variant to a position on a specified transcript and the resulting
  consequence to the sequence and/or function of that transcript.
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variation
is_a: VariantLocation
slots:
- transcript

```
</details>

### Induced

<details>
```yaml
name: VariantTranscriptLocation
description: Links a variant to a position on a specified transcript and the resulting
  consequence to the sequence and/or function of that transcript.
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variation
is_a: VariantLocation
attributes:
  transcript:
    name: transcript
    description: Transcript associated with variant and for which a specific location
      and consequence of that variant is provided, as specified at source.  Multivalued=false
      for this slot because although a variant can have multiple VariantTranscriptLocation
      stanzas, each stanza will have one and only one source transcript ID.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variation
    domain: VariantTranscriptLocation
    multivalued: false
    alias: transcript
    owner: VariantTranscriptLocation
    domain_of:
    - VariantTranscriptLocation
    range: Transcript
    required: false
  evidence_code:
    name: evidence_code
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    alias: evidence_code
    owner: VariantTranscriptLocation
    domain_of:
    - VariantLocation
    - AlleleGenomicEntityAssociation
    - GeneToGeneOrthologyCurated
    range: ECOTerm
    required: false
  single_reference:
    name: single_reference
    description: holds between an object and a single reference
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    alias: single_reference
    owner: VariantTranscriptLocation
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
  start_position:
    name: start_position
    description: Start position of variant on genomic entity.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variation
    domain: VariantLocation
    multivalued: false
    alias: start_position
    owner: VariantTranscriptLocation
    domain_of:
    - VariantLocation
    range: integer
    required: false
  end_position:
    name: end_position
    description: End position of variant on genomic entity.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variation
    domain: VariantLocation
    multivalued: false
    alias: end_position
    owner: VariantTranscriptLocation
    domain_of:
    - VariantLocation
    range: integer
    required: false
  reference_sequence:
    name: reference_sequence
    description: Reference sequence of genome or genomic entity at position of aligned
      variant.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variation
    domain: VariantLocation
    multivalued: false
    alias: reference_sequence
    owner: VariantTranscriptLocation
    domain_of:
    - VariantLocation
    range: biological_sequence
    required: false
  variant_sequence:
    name: variant_sequence
    description: Sequence that differs from the reference sequence of genome or genomic
      entity at position of variant, as specified by curator.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variation
    domain: VariantLocation
    multivalued: false
    alias: variant_sequence
    owner: VariantTranscriptLocation
    domain_of:
    - VariantLocation
    range: biological_sequence
    required: false
  consequence:
    name: consequence
    description: SOTerm (child of SO:0001576 - transcript_variant) that describes
      the consequence of the variant, as stated in the source reference. In practice
      source consequence will be associated with locations at any or all of VariantGenomeLocation,
      VariantTranscriptLocation, and VariantPolypeptideLocation.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variation
    domain: VariantLocation
    multivalued: false
    alias: consequence
    owner: VariantTranscriptLocation
    domain_of:
    - VariantLocation
    range: SOTerm
    required: false
  created_by:
    name: created_by
    description: The individual that created the entity.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    domain: AuditedObject
    multivalued: false
    alias: created_by
    owner: VariantTranscriptLocation
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
    owner: VariantTranscriptLocation
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
    owner: VariantTranscriptLocation
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
    owner: VariantTranscriptLocation
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
    owner: VariantTranscriptLocation
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
    owner: VariantTranscriptLocation
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
    owner: VariantTranscriptLocation
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
    owner: VariantTranscriptLocation
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>