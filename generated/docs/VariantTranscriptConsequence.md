# VariantTranscriptConsequence

Class for transcript-level VEP results


```mermaid
 classDiagram
      VariantConsequence <|-- VariantTranscriptConsequence
      
      VariantTranscriptConsequence : amino_acid_reference
      VariantTranscriptConsequence : amino_acid_variant
      VariantTranscriptConsequence : cdna_end
      VariantTranscriptConsequence : cdna_start
      VariantTranscriptConsequence : cds_end
      VariantTranscriptConsequence : cds_start
      VariantTranscriptConsequence : codon_reference
      VariantTranscriptConsequence : codon_variant
      VariantTranscriptConsequence : created_by
      VariantTranscriptConsequence : date_created
      VariantTranscriptConsequence : date_updated
      VariantTranscriptConsequence : db_date_created
      VariantTranscriptConsequence : db_date_updated
      VariantTranscriptConsequence : hgvs_coding_nomenclature
      VariantTranscriptConsequence : hgvs_protein_nomenclature
      VariantTranscriptConsequence : internal
      VariantTranscriptConsequence : object
      VariantTranscriptConsequence : obsolete
      VariantTranscriptConsequence : polyphen_prediction
      VariantTranscriptConsequence : polyphen_score
      VariantTranscriptConsequence : protein_end
      VariantTranscriptConsequence : protein_start
      VariantTranscriptConsequence : sift_prediction
      VariantTranscriptConsequence : sift_score
      VariantTranscriptConsequence : subject
      VariantTranscriptConsequence : updated_by
      VariantTranscriptConsequence : vep_consequence
      VariantTranscriptConsequence : vep_impact
      

```



URI: [alliance:VariantTranscriptConsequence](http://alliancegenome.org/VariantTranscriptConsequence)


## Parent Classes

* [AuditedObject](AuditedObject.md)
    * [VariantConsequence](VariantConsequence.md)
        * **VariantTranscriptConsequence**




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [amino_acid_reference](amino_acid_reference.md) | Amino acid sequence encoded by codon(s) in reference genome sequence altered by the variant |
| [amino_acid_variant](amino_acid_variant.md) | Amino acid sequence encoded by codon(s) in variant sequence |
| [cdna_end](cdna_end.md) | End position of variant in cDNA coordinates |
| [cdna_start](cdna_start.md) | Start position of variant in cDNA coordinates |
| [cds_end](cds_end.md) | End position of variant in CDS coordinates |
| [cds_start](cds_start.md) | Start position of variant in CDS coordinates |
| [codon_reference](codon_reference.md) | Reference genome sequence of codon(s) altered by the variant.  Bases affected by the variant are given in upper case, bases flanking the variation are given in lower case |
| [codon_variant](codon_variant.md) | Sequence of codon(s) in variant sequence altered by the variant. Bases affected by the variant are given in upper case, bases flanking the variation are given in lower case |
| [created_by](created_by.md) | The individual that created the entity. |
| [date_created](date_created.md) | The date on which an entity was created. This can be applied to nodes or edges. |
| [date_updated](date_updated.md) | Date on which an entity was last modified. |
| [db_date_created](db_date_created.md) | The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data). |
| [db_date_updated](db_date_updated.md) | Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database. |
| [hgvs_coding_nomenclature](hgvs_coding_nomenclature.md) | HGVS coding sequence (HGVSc) name |
| [hgvs_protein_nomenclature](hgvs_protein_nomenclature.md) | HGVS protein sequence (HGVSp) name |
| [internal](internal.md) | Classifies the entity as private (for internal use) or not (for public use). |
| [object](object.md) | connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object. |
| [obsolete](obsolete.md) | Entity is no longer current. |
| [polyphen_prediction](polyphen_prediction.md) | PolyPhen-2 prediction |
| [polyphen_score](polyphen_score.md) | PolyPhen-2 score between 0 and 1 |
| [protein_end](protein_end.md) | End position of variant in amino acid sequence |
| [protein_start](protein_start.md) | Start position of variant in amino acid sequence |
| [sift_prediction](sift_prediction.md) | SIFT prediction |
| [sift_score](sift_score.md) | SIFT score between 0 and 1 |
| [subject](subject.md) | connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object. |
| [updated_by](updated_by.md) | The individual that last modified the entity. |
| [vep_consequence](vep_consequence.md) | VEP consequence |
| [vep_impact](vep_impact.md) | VEP predicted impact of variation on molecule |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:VariantTranscriptConsequence'] |
| native | ['alliance:VariantTranscriptConsequence'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VariantTranscriptConsequence
description: Class for transcript-level VEP results
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
aliases:
- TranscriptLevelConsequence
is_a: VariantConsequence
slots:
- amino_acid_reference
- amino_acid_variant
- codon_reference
- codon_variant
- cdna_start
- cdna_end
- cds_start
- cds_end
- protein_start
- protein_end
- hgvs_protein_nomenclature
- hgvs_coding_nomenclature
slot_usage:
  object:
    name: object
    domain_of:
    - Association
    - VariantConsequence
    range: Transcript
  subject:
    name: subject
    domain_of:
    - Association
    - VariantConsequence
    range: VariantTranscriptLocation
  amino_acid_reference:
    name: amino_acid_reference
    description: Amino acid sequence encoded by codon(s) in reference genome sequence
      altered by the variant
    domain_of:
    - VariantTranscriptConsequence
  amino_acid_variant:
    name: amino_acid_variant
    description: Amino acid sequence encoded by codon(s) in variant sequence
    domain_of:
    - VariantTranscriptConsequence
  codon_reference:
    name: codon_reference
    description: Reference genome sequence of codon(s) altered by the variant.  Bases
      affected by the variant are given in upper case, bases flanking the variation
      are given in lower case
    domain_of:
    - VariantTranscriptConsequence
  codon_variant:
    name: codon_variant
    description: Sequence of codon(s) in variant sequence altered by the variant.
      Bases affected by the variant are given in upper case, bases flanking the variation
      are given in lower case
    domain_of:
    - VariantTranscriptConsequence
  cdna_start:
    name: cdna_start
    description: Start position of variant in cDNA coordinates
    domain_of:
    - VariantTranscriptConsequence
  cdna_end:
    name: cdna_end
    description: End position of variant in cDNA coordinates
    domain_of:
    - VariantTranscriptConsequence
  cds_start:
    name: cds_start
    description: Start position of variant in CDS coordinates
    domain_of:
    - VariantTranscriptConsequence
  cds_end:
    name: cds_end
    description: End position of variant in CDS coordinates
    domain_of:
    - VariantTranscriptConsequence
  protein_start:
    name: protein_start
    description: Start position of variant in amino acid sequence
    domain_of:
    - VariantTranscriptConsequence
  protein_end:
    name: protein_end
    description: End position of variant in amino acid sequence
    domain_of:
    - VariantTranscriptConsequence
  hgvs_protein_nomenclature:
    name: hgvs_protein_nomenclature
    description: HGVS protein sequence (HGVSp) name
    domain_of:
    - VariantTranscriptConsequence
  hgvs_coding_nomenclature:
    name: hgvs_coding_nomenclature
    description: HGVS coding sequence (HGVSc) name
    domain_of:
    - VariantTranscriptConsequence

```
</details>

### Induced

<details>
```yaml
name: VariantTranscriptConsequence
description: Class for transcript-level VEP results
from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
aliases:
- TranscriptLevelConsequence
is_a: VariantConsequence
slot_usage:
  object:
    name: object
    domain_of:
    - Association
    - VariantConsequence
    range: Transcript
  subject:
    name: subject
    domain_of:
    - Association
    - VariantConsequence
    range: VariantTranscriptLocation
  amino_acid_reference:
    name: amino_acid_reference
    description: Amino acid sequence encoded by codon(s) in reference genome sequence
      altered by the variant
    domain_of:
    - VariantTranscriptConsequence
  amino_acid_variant:
    name: amino_acid_variant
    description: Amino acid sequence encoded by codon(s) in variant sequence
    domain_of:
    - VariantTranscriptConsequence
  codon_reference:
    name: codon_reference
    description: Reference genome sequence of codon(s) altered by the variant.  Bases
      affected by the variant are given in upper case, bases flanking the variation
      are given in lower case
    domain_of:
    - VariantTranscriptConsequence
  codon_variant:
    name: codon_variant
    description: Sequence of codon(s) in variant sequence altered by the variant.
      Bases affected by the variant are given in upper case, bases flanking the variation
      are given in lower case
    domain_of:
    - VariantTranscriptConsequence
  cdna_start:
    name: cdna_start
    description: Start position of variant in cDNA coordinates
    domain_of:
    - VariantTranscriptConsequence
  cdna_end:
    name: cdna_end
    description: End position of variant in cDNA coordinates
    domain_of:
    - VariantTranscriptConsequence
  cds_start:
    name: cds_start
    description: Start position of variant in CDS coordinates
    domain_of:
    - VariantTranscriptConsequence
  cds_end:
    name: cds_end
    description: End position of variant in CDS coordinates
    domain_of:
    - VariantTranscriptConsequence
  protein_start:
    name: protein_start
    description: Start position of variant in amino acid sequence
    domain_of:
    - VariantTranscriptConsequence
  protein_end:
    name: protein_end
    description: End position of variant in amino acid sequence
    domain_of:
    - VariantTranscriptConsequence
  hgvs_protein_nomenclature:
    name: hgvs_protein_nomenclature
    description: HGVS protein sequence (HGVSp) name
    domain_of:
    - VariantTranscriptConsequence
  hgvs_coding_nomenclature:
    name: hgvs_coding_nomenclature
    description: HGVS coding sequence (HGVSc) name
    domain_of:
    - VariantTranscriptConsequence
attributes:
  amino_acid_reference:
    name: amino_acid_reference
    description: Amino acid sequence encoded by codon(s) in reference genome sequence
      altered by the variant
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    domain: VariantTranscriptConsequence
    alias: amino_acid_reference
    owner: VariantTranscriptConsequence
    domain_of:
    - VariantTranscriptConsequence
    range: string
  amino_acid_variant:
    name: amino_acid_variant
    description: Amino acid sequence encoded by codon(s) in variant sequence
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    domain: VariantTranscriptConsequence
    alias: amino_acid_variant
    owner: VariantTranscriptConsequence
    domain_of:
    - VariantTranscriptConsequence
    range: string
  codon_reference:
    name: codon_reference
    description: Reference genome sequence of codon(s) altered by the variant.  Bases
      affected by the variant are given in upper case, bases flanking the variation
      are given in lower case
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    domain: VariantTranscriptConsequence
    alias: codon_reference
    owner: VariantTranscriptConsequence
    domain_of:
    - VariantTranscriptConsequence
    range: string
  codon_variant:
    name: codon_variant
    description: Sequence of codon(s) in variant sequence altered by the variant.
      Bases affected by the variant are given in upper case, bases flanking the variation
      are given in lower case
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    domain: VariantTranscriptConsequence
    alias: codon_variant
    owner: VariantTranscriptConsequence
    domain_of:
    - VariantTranscriptConsequence
    range: string
  cdna_start:
    name: cdna_start
    description: Start position of variant in cDNA coordinates
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    domain: VariantTranscriptConsequence
    alias: cdna_start
    owner: VariantTranscriptConsequence
    domain_of:
    - VariantTranscriptConsequence
    range: integer
  cdna_end:
    name: cdna_end
    description: End position of variant in cDNA coordinates
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    domain: VariantTranscriptConsequence
    alias: cdna_end
    owner: VariantTranscriptConsequence
    domain_of:
    - VariantTranscriptConsequence
    range: integer
  cds_start:
    name: cds_start
    description: Start position of variant in CDS coordinates
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    domain: VariantTranscriptConsequence
    alias: cds_start
    owner: VariantTranscriptConsequence
    domain_of:
    - VariantTranscriptConsequence
    range: integer
  cds_end:
    name: cds_end
    description: End position of variant in CDS coordinates
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    domain: VariantTranscriptConsequence
    alias: cds_end
    owner: VariantTranscriptConsequence
    domain_of:
    - VariantTranscriptConsequence
    range: integer
  protein_start:
    name: protein_start
    description: Start position of variant in amino acid sequence
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    domain: VariantTranscriptConsequence
    alias: protein_start
    owner: VariantTranscriptConsequence
    domain_of:
    - VariantTranscriptConsequence
    range: integer
  protein_end:
    name: protein_end
    description: End position of variant in amino acid sequence
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    domain: VariantTranscriptConsequence
    alias: protein_end
    owner: VariantTranscriptConsequence
    domain_of:
    - VariantTranscriptConsequence
    range: integer
  hgvs_protein_nomenclature:
    name: hgvs_protein_nomenclature
    description: HGVS protein sequence (HGVSp) name
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    domain: VariantTranscriptConsequence
    alias: hgvs_protein_nomenclature
    owner: VariantTranscriptConsequence
    domain_of:
    - VariantTranscriptConsequence
    range: string
  hgvs_coding_nomenclature:
    name: hgvs_coding_nomenclature
    description: HGVS coding sequence (HGVSc) name
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    domain: VariantTranscriptConsequence
    alias: hgvs_coding_nomenclature
    owner: VariantTranscriptConsequence
    domain_of:
    - VariantTranscriptConsequence
    range: string
  subject:
    name: subject
    description: connects an association to the subject of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    is_a: association_slot
    alias: subject
    owner: VariantTranscriptConsequence
    domain_of:
    - Association
    - VariantConsequence
    range: VariantTranscriptLocation
    required: true
  object:
    name: object
    description: connects an association to the object of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    is_a: association_slot
    alias: object
    owner: VariantTranscriptConsequence
    domain_of:
    - Association
    - VariantConsequence
    range: Transcript
    required: true
  vep_consequence:
    name: vep_consequence
    description: VEP consequence
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    alias: vep_consequence
    owner: VariantTranscriptConsequence
    domain_of:
    - VariantConsequence
    range: vep_consequence_levels
  vep_impact:
    name: vep_impact
    description: VEP predicted impact of variation on molecule
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    alias: vep_impact
    owner: VariantTranscriptConsequence
    domain_of:
    - VariantConsequence
    range: string
  polyphen_score:
    name: polyphen_score
    description: PolyPhen-2 score between 0 and 1
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    domain: VariantGeneConsequence
    alias: polyphen_score
    owner: VariantTranscriptConsequence
    domain_of:
    - VariantConsequence
    range: float
  polyphen_prediction:
    name: polyphen_prediction
    description: PolyPhen-2 prediction
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    alias: polyphen_prediction
    owner: VariantTranscriptConsequence
    domain_of:
    - VariantConsequence
    range: polyphen_prediction_levels
  sift_score:
    name: sift_score
    description: SIFT score between 0 and 1
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    domain: VariantGeneConsequence
    alias: sift_score
    owner: VariantTranscriptConsequence
    domain_of:
    - VariantConsequence
    range: float
  sift_prediction:
    name: sift_prediction
    description: SIFT prediction
    from_schema: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
    alias: sift_prediction
    owner: VariantTranscriptConsequence
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
    owner: VariantTranscriptConsequence
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
    owner: VariantTranscriptConsequence
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
    owner: VariantTranscriptConsequence
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
    owner: VariantTranscriptConsequence
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
    owner: VariantTranscriptConsequence
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
    owner: VariantTranscriptConsequence
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
    owner: VariantTranscriptConsequence
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
    owner: VariantTranscriptConsequence
    domain_of:
    - AuditedObject
    - AuditedObjectDTO
    range: boolean

```
</details>