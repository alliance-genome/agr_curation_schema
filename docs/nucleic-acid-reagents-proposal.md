# Nucleic-acid reagents: working model

This proposal incorporates MOD analysis and curator feedback through October 27,
2026, including Gil dos Santos’s expanded FlyBase requests, Gillian Millburn’s
ontology recommendations, Ceri Van Slyke’s primer/protocol corrections, and the
MGI source-background and age requests. It defines schema and submission formats;
persistence, vocabulary loading and identifier resolution still need implementation.

The branch began on `main` at `8e491ab8` (v2.19.0), which already includes the
expression DTO work from PR #325. It supersedes the closed PCR-only
[PR #321](https://github.com/alliance-genome/agr_curation_schema/pull/321).
The expanded proposal is [PR #343](https://github.com/alliance-genome/agr_curation_schema/pull/343).

## Classes and biological boundaries

```text
SubmittedObject
  Reagent
    NucleicAcidReagent (abstract)
      DNAClone
      PCRProduct
      NucleicAcidProbePreparation
      Oligo
    Construct (existing parent; new sequence and progenitor-clone properties)
    Antibody / Cassette / SequenceTargetingReagent (existing hierarchy)
  NucleicAcidSequenceRecord
  PrimerPair
  NucleicAcidLibrary

AuditedObject
  NucleicAcidSource (inline biological-source or library-membership details)
  ReagentSequence (inline sequence evidence)
```

Each concrete class has a DTO with the corresponding parent and an ingest
collection. `RNAClone` was removed; this proposal does not restore it.
`CDNAClone` and `GenomicClone` remain folded into `DNAClone`. They would not add
properties beyond the parent. Insert origin is an optional, single-valued
`clone_insert_origin: VocabularyTerm`; its DTO field is `clone_insert_origin_name`.
Omit it, or submit null, for unknown origin. An EST label alone establishes neither
cloning nor insert origin.

**DNAClone means an insert that was cloned into a vector**, including clones
that were subsequently discarded. A confirmed discarded clone can have
availability `not available`. A record that was never cloned belongs in
`NucleicAcidSequenceRecord`, retaining its FBcl or other provider identity,
library, sequences, references and genomic-entity associations.

FlyBase’s assay-library classification is not sufficient to choose between
these classes. Gil reports that all 3,445 RM_cDNA records and approximately 506
RP_cDNA ABI3730 records were cloned but not kept, whereas AM, MODENCODE,
TTT_DIG, TTT_NEB and RP_cDNA 454 reads were never cloned. These are curator-reported
facts, not new database counts measured for this revision. Classification must
use the source-supported record or library/platform distinctions.

`Oligo` represents a separately identified physical oligonucleotide. It adds
sequence, chemistry, modifications and sequence-context properties. A primer
is a use of an oligo; no empty Primer subclass is introduced. `PrimerPair` is a
separately identified definition of two primers used together. It can reference
Oligo objects or retain forward/reverse sequence text where separate identities
are unavailable. It is not a physical product. `PCRProduct` can reference its
PrimerPair and retain its own template context. Identical primers do not establish
identical products across backgrounds.

`NucleicAcidSequenceRecord`, `PrimerPair` and `NucleicAcidLibrary` are outside
Reagent. Consequently they are not valid expression detection materials. The
existing expression detection range stays Reagent and can still point directly
to clones, PCR products, oligos, preparations, constructs or antibodies.

## Sources, libraries and vectors

A reusable `NucleicAcidLibrary` carries identity, provider, name, taxon, references,
source tissue/stage/age/background, and library-scoped vector information.
`NucleicAcidSource` remains an inline detail for biological source or membership.
Its `source_library` points to the library; the DTO uses `source_library_identifier`.
Membership relation stays on that detail. Existing exporters that send a library
identifier must supply or resolve the corresponding library, rather than treating
that field as an unchecked provenance string. If there is no independently
identified library, retain inline source fields without inventing an ID.

Library fields are shared assertions; membership-specific assertions stay inline.
If both are supplied, conflicting values must be reviewed by the loader, not
silently overwritten. A biological source need not be a library: MGI source
records can describe tissue, age and strain. For this reason `source_tissue`,
`source_stage`, `source_age` and `source_genetic_background` retain the biological
source prefix rather than the narrower suggested `source_library_*` prefix.

| Entity field | Entity range | DTO field | Mapping and limits |
| --- | --- | --- | --- |
| `source_tissue` | AnatomicalTerm | `source_tissue_curie` | FlyBase FBbt through the existing DAOTerm subclass; other supported anatomy ontologies through their existing subclasses |
| `source_stage` | StageTerm | `source_stage_curie` | FlyBase FBdv through FBDVTerm; other existing stage-term subclasses as appropriate |
| `source_genetic_background` | AffectedGenomicModel | `source_genetic_background_identifier` | Biological source strain/genotype/background, not the cloning or propagation host |
| `source_age` | string | `source_age` | MGI `mgd.prb_source.age`, separate from stage; preserve original wording |
| `source_tissue_free_text` / `source_stage_free_text` | string | same names | Preserve unmapped source wording; never insert a tissue label into a CURIE field |
| `source_library_type` | VocabularyTerm | `source_library_type_name` | Source classification, such as reagent collection or assay dataset; not proof of material identity |
| `source_library_membership_relation` | VocabularyTerm | `source_library_membership_relation_name` | Membership type, separate from library classification |
| `clone_vector` / `source_vector` | Construct | `clone_vector_identifier` / `source_vector_identifier` | Clone-specific or library-scoped vector identity respectively |

MGI’s `prb_probe._source_key → prb_source._source_key` selects source information.
`prb_source._strain_key` must be resolved to the corresponding AGM identifier;
it is not itself a public AGM identifier. Sentinel or unidentified strains must
not generate fictitious AGMs. The source-age string does not yet model `agemin`
and `agemax` as structured intervals. Mapping MGI tissue text to anatomy terms
requires review; the free-text fallback preserves it in the meantime.

Vector name strings remain available when identity is unknown. FlyBase FBmc
vectors use Construct. `Construct.construct_sequences` / DTO
`construct_sequence_dtos` accept the vector’s own sequence, including complete
backbone sequence. DNAClone sequence details describe its insert or insert reads,
not a concatenated vector-plus-insert sequence inferred by the exporter.

## Clone lineage, quality and preparation instructions

`derived_from_reagents` and `derived_from_reagent_identifiers` now live on the
NucleicAcidReagent parents. Both clone-to-clone lineage and preparation starting
materials can be submitted. FlyBase’s DPiM clone points to its progenitor clone.
These properties state derivation; they do not encode each intervening laboratory
step or per-edge evidence. A richer typed/evidenced lineage association remains
an extension if curators need that detail.

`Construct.construct_progenitor_clones` and its DTO identifier list link an FBtp
construct to the DNAClone used to generate it. This is distinct from
`DNAClone.clone_vector`, which identifies the vector used for cloning.
`replaces_clones` expresses succession, not derivation: the new clone points to
the superseded clone. The corresponding DTO uses `replaces_clone_identifiers`.

DNAClone also has collection-status terms (`BDGP`, `DGC gold` are candidates),
multiple free-text known problems, and a free-text curator assessment. Collection
membership/status is separate from availability and is not automatically an
assertion that a clone has passed every quality check.

ZFIN preparation instructions can be retained in `reagent_preparation_protocol`
on the clone, with `reagent_primer_pairs` linking identified primer-pair definitions.
Instructions alone do not establish a separate probe-preparation object. Ceri
reports that some primers are vector-derived or combine vector and insert sequence;
`oligo_sequence_context` can retain vector, insert or mixed context when supported.
Do not infer an insert’s genomic identity from a primer’s source label.

## Controlled vocabularies and ontology reuse

Ontology references use the existing ontology classes. Hybrid lists use
**VocabularyTerm**, including ontology-backed entries alongside local entries.
DTOs send ontology CURIEs in `_curie` fields and vocabulary names in `_name` or
`_names` fields. Those DTO fields remain strings because they are references,
not because the entity fields remain unstructured text.

VocabularyTerm and OntologyTerm are separate existing model hierarchies.
An SO or ChEBI object is not automatically a VocabularyTerm. Vocabulary owners
must approve and register entries and retain reviewed ontology mappings in the
vocabulary configuration. This PR does not seed terms, add a global mapping
mechanism, or make a CURIE valid in a name-based field. Runtime validators must
check vocabulary membership and ontology class resolution.

| Proposed vocabulary / fields | Candidates for review | Mapping caveat |
| --- | --- | --- |
| Clone Insert Origin | cDNA → SO:0000756; genomic DNA → SO:0000991 | Qualified origin mappings: derived from that material. SO:0000913 and SO:0000914 describe cloned insert classes instead. Unknown origin remains null. |
| Clone Vector Type (`clone_vector_type`, `source_vector_type`) | plasmid → SO:0000755; BAC → SO:0000153; PAC → SO:0000154; YAC → SO:0000152; cosmid → SO:0000156; phagemid → SO:0000157; fosmid → SO:0000158 | Retain local not specified and not applicable distinctly; SO:0000754 is lambda vector, not every phage vector. |
| Reagent Sequence Role | EST → SO:0000345; 5-prime EST → SO:0001208; 3-prime EST → SO:0001209; clone end → SO:0001793 | Full insert → SO:0000753 is qualified: the term does not assert completeness. Complete vector remains a local role pending review. |
| Probe Nucleic Acid Type (`probe_nucleic_acid_type`, `oligo_chemical_type`) | DNA → SO:0000352; RNA → SO:0000356 | These describe sequence composition; apply to material chemistry with that qualification. Modified or mixed chemistry needs explicit review. |
| Probe Label / Oligo Modification | digoxigenin → CHEBI:42098; biotin → CHEBI:15956; P32 → CHEBI:37972; P33 → CHEBI:37973; S35 → CHEBI:37983; tritium → CHEBI:29238 | Distinguish free chemical, attached moiety and labeled nucleotide. Positional oligo modifications are not modeled yet. |
| Clone Collection Status | BDGP; DGC gold | Provider-supported designations; not chemical or availability terms. |
| Library Type / Library Membership Relation | reagent collection; assay dataset / member_of_reagent_collection; member_of_assay | Distinct lists; curators must approve normalization of original source values. |
| Reagent Association Method | AEVAST with BLAST; source-supported manual or other computational methods | Method absence is not manual curation; retain version separately. |
| Sequence Record Type / Oligo Sequence Context | read anchor; sequence record / insert; vector; mixed; unspecified | Record classification and primer sequence context are different vocabularies. |
| Reagent Availability | available; not available; unknown | Unavailable physical clones remain clones; never-cloned records remain sequence records. |
| Other existing proposal vocabularies | Reagent Type, PCR Assay Method, Probe Strand Orientation, Probe Visualization Method, Nucleic Acid Polymerase | Keep source distinctions and approve runtime membership before loading. |

The [vocabulary review](https://model-preview.alliancegenome.org/reviews/nucleic-acid-reagents/vocabularies.html)
contains the broader SO and ChEBI candidate tables and unresolved chemical-label
questions. Candidate SO terms were checked against the official ontology at
[commit 4340c143](https://github.com/The-Sequence-Ontology/SO-Ontologies/blob/4340c143bac3578bba0c013d02e8c5f0e51ad14a/Ontology_Files/so.obo);
ChEBI candidates were checked through EBI OLS on October 27. DNP, generic rhodamine,
EvaGreen and other unresolved labels are not assigned guessed identifiers.
An unresolved mapping does not establish that the ontology lacks the concept.

## Genomic-entity associations

The existing proposal association now explicitly permits three subject ranges:
NucleicAcidReagent, PrimerPair and NucleicAcidSequenceRecord. Its historical class,
slot and DTO collection names are retained. The subject slot has range
SubmittedObject narrowed with `any_of` to those three classes. The DTO's
`nucleic_acid_reagent_identifier` must resolve to one of them, not an arbitrary
SubmittedObject. GenomicEntity remains the target, permitting genes, transcripts,
CDS, variants or qualifying sequence features. Mapping FBsf records to the right
GenomicEntity class and ensuring those target records are loaded remains a
separate ingest requirement.

The relation vocabulary retains encodes, hybridizes_to, amplifies, feature-overlap
relations and sequence_supports, and adds:

- `contains_gene`: the gene lies entirely within the clone insert.
- `partially_overlaps_gene`: the gene extends beyond an insert end.

These gene-overlap relations should be restricted downstream to appropriate
clone/gene endpoints. They are not expression-detection assertions. Gil reports
309,491 BAC-to-gene links, including 72,941 partial overlaps, in the FlyBase evidence
behind this request; these counts were not remeasured for this commit.

`reagent_association_source_relation` retains exact original text separately from
the normalized relation. `reagent_association_method` is now VocabularyTerm,
submitted through `reagent_association_method_name`. Method version, source
release, supporting sequence identifiers and intervening transcript identifiers
remain available. FlyBase did not record an AEVAST version; omit it.

MGI’s approved P/missing-to-H conversion must preserve raw values and distinguish
none, SQL NULL and empty string. It is not a conversion rule for another MOD.
Pair-to-target assertions must describe the definition’s supported target; they
do not prove that a particular PCR product was observed.

## Submission collections and examples

| Collection | DTO |
| --- | --- |
| `dna_clone_ingest_set` | DNACloneDTO |
| `pcr_product_ingest_set` | PCRProductDTO |
| `nucleic_acid_probe_preparation_ingest_set` | NucleicAcidProbePreparationDTO |
| `oligo_ingest_set` | OligoDTO |
| `primer_pair_ingest_set` | PrimerPairDTO |
| `nucleic_acid_sequence_record_ingest_set` | NucleicAcidSequenceRecordDTO |
| `nucleic_acid_library_ingest_set` | NucleicAcidLibraryDTO |
| `nucleic_acid_reagent_genomic_entity_association_ingest_set` | NucleicAcidReagentGenomicEntityAssociationDTO |

Construct uses its existing ingest collection. Submit each source identity in the
appropriate collection once. Do not duplicate a read anchor as an unavailable
clone or convert a marker with PCR-definition fields into physical material.

The [illustrative fixture](../test/data/nucleic_acid_reagent_test.json) uses
conspicuous EXAMPLE identities to exercise all new collections and relationships.
Its ontology references and background identifier illustrate syntax; they are not
assertions about actual source materials. It is not a resolvable production dataset.

The [FlyBase feedback fixture](../test/data/nucleic_acid_flybase_feedback_test.json)
uses real facts supplied by Gil on October 27: LD10016 (FBcl0158098), its DPiM
progeny FBcl0741583, GH03509 (FBcl0122173), CH322-53M21 (FBcl0784728), two identified
vectors, and LD10016’s CG2004 relationship. Sequence accessions are preserved;
residues, library identifiers, publications and unknown vector sequences are not
invented. BAC gene names and the PBac construct name supplied without identifiers
are documented as follow-up examples rather than used as identifiers. The fixture
is curator-supplied evidence, not a new database extraction or complete MOD export.

Earlier downloaded MOD samples and the published mapping tables describe the
previous branch schema. They require regeneration or migration for these renamed
DTO fields and new library-resolution rules. This commit does not silently certify
those older files against the expanded proposal.

## Feedback coverage and remaining implementation questions

All twelve requests in Gil’s October 27 comment are addressed: ontology source
fields and reusable library; discarded-clone boundary; sequence-record class;
vector objects and vector sequences; parent-level derivation; construct progenitor;
gene containment/partial overlap; clone quality and succession; Oligo/PrimerPair;
RNAClone documentation; domain-prefixed PCR/association slots; and real examples.
The proposed stronger library prefix was narrowed to preserve non-library biological
sources, as explained above. More detailed lineage evidence remains an extension.

The following questions affect loading and later refinements:

1. Which runtime vocabularies, normalized names and ontology mappings will owners
   approve? How will mapping provenance be stored and maintained?
2. What provider-qualified identities will represent libraries, primer pairs and
   physical oligos? Do sequence-only records need attributed synonyms as well?
3. How will the loader reconcile shared library assertions with inline source
   details, resolve AGM backgrounds, and reject references of the wrong class?
4. Which FlyBase read records can be classified automatically using platform and
   library metadata, and which need curator review? Library type alone is insufficient.
5. Do clone lineage/replacement and collection-quality statements need per-edge
   evidence, dates or structured assessments in a later iteration?
6. Which FBsf target classes and MGI primer definitions are ready for submission?
   What does MGI `prb_probe.productsize` describe in each template/assay context?
7. What is the MGI preparation replacement/deletion policy? Stable internal keys
   do not make preparations reusable across assays. Do not derive new preparation
   identities from instructions or create antibody preparations in this hierarchy.
8. Coordinate-bearing sequence mappings, modification positions and complete
   computational derivation graphs need additional agreed semantics.

Load or resolve vectors, libraries, AGMs and oligos before their references;
resolve clone lineage and construct progenitors after allocating their identities.
A staged loader is needed for dependencies in both directions between constructs
and clones. Load associations and expression references after their endpoints.
Schema validation cannot enforce those database-resolution and lifecycle rules.

For JSON Schema validation of full entity objects with polymorphic ranges, generate
with `--include-range-class-descendants`. Default generation checks the named base
class only. DTO identifier strings still require class-aware loader resolution;
JSON structure alone cannot establish the referenced object’s biological class.

## Validation

Run against this branch using the repository’s locked uv environment:

```sh
uv run --frozen linkml-validate -C Ingest -s model/schema/allianceModel.yaml test/data/nucleic_acid_reagent_test.json
uv run --frozen linkml-validate -C Ingest -s model/schema/allianceModel.yaml test/data/nucleic_acid_flybase_feedback_test.json
```

The fixtures use baseline version `2.19.0` with this unmerged PR’s schema; they
are not compatible with unmodified v2.19.0. Generated artifacts remain CI-owned.
Validation results for this revision are recorded in the PR description.

Source evidence and discussion remain in the
[curator review](https://model-preview.alliancegenome.org/reviews/nucleic-acid-reagents/).
The website is a separately published snapshot; this PR update does not rebuild it.
