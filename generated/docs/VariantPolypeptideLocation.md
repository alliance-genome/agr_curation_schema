# VariantPolypeptideLocation

Links a variant to a position on a specified polypeptide and the resulting consequence to the sequence and/or function of that polypeptide.


```mermaid
 classDiagram
      VariantLocation <|-- VariantPolypeptideLocation
      
      VariantPolypeptideLocation : associated_transcripts
      VariantPolypeptideLocation : consequence
      VariantPolypeptideLocation : created_by
      VariantPolypeptideLocation : date_created
      VariantPolypeptideLocation : date_updated
      VariantPolypeptideLocation : db_date_created
      VariantPolypeptideLocation : db_date_updated
      VariantPolypeptideLocation : end_position
      VariantPolypeptideLocation : evidence_code
      VariantPolypeptideLocation : internal
      VariantPolypeptideLocation : obsolete
      VariantPolypeptideLocation : polypeptide
      VariantPolypeptideLocation : reference_sequence
      VariantPolypeptideLocation : single_reference
      VariantPolypeptideLocation : start_position
      VariantPolypeptideLocation : updated_by
      VariantPolypeptideLocation : variant_sequence
      

```



URI: [alliance:VariantPolypeptideLocation](http://alliancegenome.org/VariantPolypeptideLocation)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * [VariantLocation](VariantLocation.md)
        * **VariantPolypeptideLocation**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [associated_transcripts](associated_transcripts.md) | Transcript(s) associated with polypeptide to which variant is aligned. |
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
| [polypeptide](polypeptide.md) | Transcript associated with variant and for which a specific location and consequence of that variant is provided, as specified by curator. Multivalued=false for this slot because although a variant can have multiple VariantTranscriptLocation stanzas, each stanza will have one and only one curated transcript ID. |
| [reference_sequence](reference_sequence.md) | Reference sequence of genome or genomic entity at position of aligned variant. |
| [single_reference](single_reference.md) | holds between an object and a single reference |
| [start_position](start_position.md) | Start position of variant on genomic entity. |
| [updated_by](updated_by.md) | The individual that last modified the entity. |
| [variant_sequence](variant_sequence.md) | Sequence that differs from the reference sequence of genome or genomic entity at position of variant, as specified by curator. |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:VariantPolypeptideLocation'] |
| native | ['alliance:VariantPolypeptideLocation'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VariantPolypeptideLocation
description: Links a variant to a position on a specified polypeptide and the resulting
  consequence to the sequence and/or function of that polypeptide.
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variation
is_a: VariantLocation
slots:
- polypeptide
- associated_transcripts

```
</details>

### Induced

<details>
```yaml
name: VariantPolypeptideLocation
description: Links a variant to a position on a specified polypeptide and the resulting
  consequence to the sequence and/or function of that polypeptide.
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variation
is_a: VariantLocation
attributes:
  polypeptide:
    name: polypeptide
    description: Transcript associated with variant and for which a specific location
      and consequence of that variant is provided, as specified by curator. Multivalued=false
      for this slot because although a variant can have multiple VariantTranscriptLocation
      stanzas, each stanza will have one and only one curated transcript ID.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variation
    domain: VariantTranscriptLocation
    multivalued: false
    alias: polypeptide
    owner: VariantPolypeptideLocation
    domain_of:
    - VariantPolypeptideLocation
    range: Transcript
    required: true
  associated_transcripts:
    name: associated_transcripts
    description: Transcript(s) associated with polypeptide to which variant is aligned.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variation
    domain: VariantPolypeptideLocation
    multivalued: true
    alias: associated_transcripts
    owner: VariantPolypeptideLocation
    domain_of:
    - VariantPolypeptideLocation
    range: Transcript
    required: false
  evidence_code:
    name: evidence_code
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    alias: evidence_code
    owner: VariantPolypeptideLocation
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
    owner: VariantPolypeptideLocation
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
    owner: VariantPolypeptideLocation
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
    owner: VariantPolypeptideLocation
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
    owner: VariantPolypeptideLocation
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
    owner: VariantPolypeptideLocation
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
    owner: VariantPolypeptideLocation
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
    owner: VariantPolypeptideLocation
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
    owner: VariantPolypeptideLocation
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
    owner: VariantPolypeptideLocation
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
    owner: VariantPolypeptideLocation
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
    owner: VariantPolypeptideLocation
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
    owner: VariantPolypeptideLocation
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
    owner: VariantPolypeptideLocation
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
    owner: VariantPolypeptideLocation
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>