# Ingest

None


```mermaid
 classDiagram
    class Ingest
      Ingest : agm_ingest_set
      Ingest : allele_cell_line_association_ingest_set
      Ingest : allele_construct_association_ingest_set
      Ingest : allele_gene_association_ingest_set
      Ingest : allele_generation_method_association_ingest_set
      Ingest : allele_genomic_location_association_ingest_set
      Ingest : allele_image_association_ingest_set
      Ingest : allele_ingest_set
      Ingest : allele_origin_association_ingest_set
      Ingest : allele_protein_association_ingest_set
      Ingest : allele_transcript_association_ingest_set
      Ingest : allele_variant_association_ingest_set
      Ingest : disease_agm_ingest_set
      Ingest : disease_allele_ingest_set
      Ingest : disease_gene_ingest_set
      Ingest : gene_ingest_set
      Ingest : linkml_version
      Ingest : ontology_closure_ingest_set
      Ingest : sqtr_ingest_set
      Ingest : variant_ingest_set
      




URI: [alliance:Ingest](http://alliancegenome.org/Ingest)


## Parent Classes




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [agm_ingest_set](agm_ingest_set.md) |  |
| [allele_cell_line_association_ingest_set](allele_cell_line_association_ingest_set.md) |  |
| [allele_construct_association_ingest_set](allele_construct_association_ingest_set.md) |  |
| [allele_gene_association_ingest_set](allele_gene_association_ingest_set.md) |  |
| [allele_generation_method_association_ingest_set](allele_generation_method_association_ingest_set.md) |  |
| [allele_genomic_location_association_ingest_set](allele_genomic_location_association_ingest_set.md) | An ingest set of genomic locations DTOs that are associated with an allele |
| [allele_image_association_ingest_set](allele_image_association_ingest_set.md) |  |
| [allele_ingest_set](allele_ingest_set.md) |  |
| [allele_origin_association_ingest_set](allele_origin_association_ingest_set.md) |  |
| [allele_protein_association_ingest_set](allele_protein_association_ingest_set.md) |  |
| [allele_transcript_association_ingest_set](allele_transcript_association_ingest_set.md) |  |
| [allele_variant_association_ingest_set](allele_variant_association_ingest_set.md) |  |
| [disease_agm_ingest_set](disease_agm_ingest_set.md) |  |
| [disease_allele_ingest_set](disease_allele_ingest_set.md) |  |
| [disease_gene_ingest_set](disease_gene_ingest_set.md) |  |
| [gene_ingest_set](gene_ingest_set.md) |  |
| [linkml_version](linkml_version.md) | Version of LinkML schema used for submitted file in the format n.n.n (e.g. 1.2.4 or 2.0.0) |
| [ontology_closure_ingest_set](ontology_closure_ingest_set.md) |  |
| [sqtr_ingest_set](sqtr_ingest_set.md) |  |
| [variant_ingest_set](variant_ingest_set.md) |  |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:Ingest'] |
| native | ['alliance:Ingest'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Ingest
from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
slots:
- linkml_version
- allele_ingest_set
- disease_allele_ingest_set
- disease_agm_ingest_set
- disease_gene_ingest_set
- gene_ingest_set
- variant_ingest_set
- allele_variant_association_ingest_set
- allele_gene_association_ingest_set
- allele_transcript_association_ingest_set
- allele_protein_association_ingest_set
- allele_construct_association_ingest_set
- allele_cell_line_association_ingest_set
- allele_origin_association_ingest_set
- allele_image_association_ingest_set
- allele_generation_method_association_ingest_set
- allele_genomic_location_association_ingest_set
- agm_ingest_set
- sqtr_ingest_set
- ontology_closure_ingest_set
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: Ingest
from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
attributes:
  linkml_version:
    name: linkml_version
    description: Version of LinkML schema used for submitted file in the format n.n.n
      (e.g. 1.2.4 or 2.0.0)
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    domain: Ingest
    alias: linkml_version
    owner: Ingest
    domain_of:
    - Ingest
    range: string
    required: true
  allele_ingest_set:
    name: allele_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: allele_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: AlleleDTO
    inlined_as_list: true
  disease_allele_ingest_set:
    name: disease_allele_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: disease_allele_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: AlleleDiseaseAnnotationDTO
    inlined_as_list: true
  disease_agm_ingest_set:
    name: disease_agm_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: disease_agm_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: AGMDiseaseAnnotationDTO
    inlined_as_list: true
  disease_gene_ingest_set:
    name: disease_gene_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: disease_gene_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: GeneDiseaseAnnotationDTO
    inlined_as_list: true
  gene_ingest_set:
    name: gene_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: gene_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: GeneDTO
    inlined_as_list: true
  variant_ingest_set:
    name: variant_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: variant_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: Variant
    inlined_as_list: true
  allele_variant_association_ingest_set:
    name: allele_variant_association_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: allele_variant_association_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: AlleleVariantAssociationDTO
    inlined_as_list: true
  allele_gene_association_ingest_set:
    name: allele_gene_association_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: allele_gene_association_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: AlleleGeneAssociationDTO
    inlined_as_list: true
  allele_transcript_association_ingest_set:
    name: allele_transcript_association_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: allele_transcript_association_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: AlleleTranscriptAssociationDTO
    inlined_as_list: true
  allele_protein_association_ingest_set:
    name: allele_protein_association_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: allele_protein_association_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: AlleleProteinAssociationDTO
    inlined_as_list: true
  allele_construct_association_ingest_set:
    name: allele_construct_association_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: allele_construct_association_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: AlleleConstructAssociationDTO
    inlined_as_list: true
  allele_cell_line_association_ingest_set:
    name: allele_cell_line_association_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: allele_cell_line_association_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: AlleleCellLineAssociationDTO
    inlined_as_list: true
  allele_origin_association_ingest_set:
    name: allele_origin_association_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: allele_origin_association_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: AlleleOriginAssociationDTO
    inlined_as_list: true
  allele_image_association_ingest_set:
    name: allele_image_association_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: allele_image_association_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: AlleleImageAssociationDTO
    inlined_as_list: true
  allele_generation_method_association_ingest_set:
    name: allele_generation_method_association_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: allele_generation_method_association_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: AlleleGenerationMethodAssociationDTO
    inlined_as_list: true
  allele_genomic_location_association_ingest_set:
    name: allele_genomic_location_association_ingest_set
    description: An ingest set of genomic locations DTOs that are associated with
      an allele
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: allele_genomic_location_association_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: GenomicLocationAssociationDTO
    inlined_as_list: true
  agm_ingest_set:
    name: agm_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: agm_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: AffectedGenomicModelDTO
    inlined_as_list: true
  sqtr_ingest_set:
    name: sqtr_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: sqtr_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: SequenceTargetingReagentDTO
    inlined_as_list: true
  ontology_closure_ingest_set:
    name: ontology_closure_ingest_set
    description: ''
    from_schema: https://github.com/alliance-genome/agr_curation_schema/model/schema/ingest
    mixins:
    - object_set
    domain: Ingest
    multivalued: true
    alias: ontology_closure_ingest_set
    owner: Ingest
    domain_of:
    - Ingest
    range: OntologyTermClosure
    inlined_as_list: true
tree_root: true

```
</details>