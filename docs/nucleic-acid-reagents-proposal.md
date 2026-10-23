# Nucleic-acid reagents: first working model

This proposal provides schema classes and submission examples for hands-on review.
It incorporates MOD database analysis and curator feedback received through
October 19, 2026, with the clone-origin design revised on October 23, 2026. It is a schema prototype, not approval of every mapping or a
working persistence/ingest implementation. Do not transfer source records merely
because a source class has a similar name.

Baseline: `main` at `8e491ab8e0772ff863fd5b471ab3a435b86f1d8b` (v2.19.0).
The expression DTO work from PR #325 is already on that baseline. This proposal
is intended to supersede the PCR-only proposal in [PR #321](https://github.com/alliance-genome/agr_curation_schema/pull/321),
reviewed at `14af569d`. PR #321 has been closed.

## Inheritance and biological boundaries

```text
AuditedObject
  CurieObject
    SubmittedObject
      Reagent
        NucleicAcidReagent (abstract; new)
          DNAClone (existing class moved here)
          PCRProduct (new)
          NucleicAcidProbePreparation (new)
        Antibody / Construct / Cassette / RNAClone (unchanged)
```

A DNAClone has an insert maintained in a cloning vector. All confirmed DNA clones
use this one class and DNACloneDTO. Origin is a property of the clone; it
does not require a subclass with no additional slots. The optional, single-valued `clone_insert_origin`
references a VocabularyTerm from the proposed Clone Insert Origin vocabulary:
`cDNA` means derived by reverse transcription of RNA; `genomic DNA` means derived
from genomic DNA. The DTO submits the term using `clone_insert_origin_name`.
For unknown or unspecified origin, omit the submission field or use null.
The persistence field can remain null; no artificial unknown term is required.

Origin is independent of `nucleic_acid_reagent_type` (DTO: `_name`), which retains
source-supported reagent subtypes such as EST. An EST designation alone does
not establish origin. cDNA/genomic sequence origin alone does not establish a
clone. The vocabulary must be seeded and term membership checked downstream;
the DTO's string field does not itself enforce these two proposed labels.

PCRProduct identifies a provider-recorded amplified material. A primer pair
can produce different products in different template backgrounds. This model
does not turn MGI primer records, RGD SSLPs or ZFIN primer-defined markers into
PCRProduct records automatically.

A NucleicAcidProbePreparation identifies a separate preparation when the source
records one. It may link to starting materials. An experiment can also use a
clone or PCR product directly; no synthetic preparation wrapper is required.
MGI preparations belong to an assay and are not assumed reusable across assays.
Antibody preparations are not nucleic-acid preparations.

```text
AuditedObjectDTO
  SubmittedObjectDTO
    ReagentDTO
      NucleicAcidReagentDTO (abstract; new)
        DNACloneDTO
        PCRProductDTO
        NucleicAcidProbePreparationDTO

AuditedObject                 AuditedObjectDTO
  NucleicAcidSource             NucleicAcidSourceDTO
  ReagentSequence               ReagentSequenceDTO

AuditedObject
  SlotAnnotation
    NameSlotAnnotation
      NucleicAcidReagentSynonymSlotAnnotation
        (submitted inline using the existing NameSlotAnnotationDTO)

AuditedObject
  Association
    EvidenceAssociation
      NucleicAcidReagentAssociation (abstract)
        NucleicAcidReagentGenomicEntityAssociation

AuditedObjectDTO
  EvidenceAssociationDTO
    NucleicAcidReagentGenomicEntityAssociationDTO
```

`NucleicAcidSource` and `ReagentSequence` are inline audited details, not new
SubmittedObject identities. Multiple library memberships and multiple sequence
pieces are preserved. Source-library vector/site facts remain library-scoped;
clone-specific fields must have clone-specific support. A sequence detail is
not a reagent, even when it has a stable accession.

The existing SequenceTargetingReagent hierarchy, Construct, Cassette and RNAClone
are deliberately not reparented in this iteration. Their biological overlap
with this branch needs a separate review before changing established inheritance.

## What can be submitted

| Ingest collection | DTO | Intended records |
| --- | --- | --- |
| `dna_clone_ingest_set` | DNACloneDTO | All confirmed DNA clones, with cDNA, genomic DNA or unspecified insert origin |
| `pcr_product_ingest_set` | PCRProductDTO | Provider-identified PCR material, including legacy records lacking primer or taxon details |
| `nucleic_acid_probe_preparation_ingest_set` | NucleicAcidProbePreparationDTO | Separately identified preparations, including assay-owned MGI records |
| `nucleic_acid_reagent_genomic_entity_association_ingest_set` | NucleicAcidReagentGenomicEntityAssociationDTO | Typed and evidenced material-to-gene/transcript/CDS/variant relationships |

The abstract parent has no generic ingest collection. Submit an object once in
the collection for its supported class. All DNA clones use the single
`dna_clone_ingest_set` collection, regardless of insert origin.

The common fields provide optional name, taxon, subtype, attributed synonyms,
references, cross-references, generating Agents, source-library details,
sequence details and source-reported availability. Every material DTO inherits
its data provider, public/internal source identity, notes and audit fields.
Taxon, name and primers are optional: unknown values must not be invented.
For an insert length, a positive integer means bases in the insert, not vector
length or an unknown-value sentinel.

`generated_by_identifiers` is multivalued, matching the existing entity slot
`generated_by`. The new slot does not change Antibody's existing singular
submission slot. Agent identifier resolution must be implemented downstream.
Synonyms reuse the model's attributed name annotation structure so evidence,
source name type and display text need not be flattened into strings.

Probe preparations have separate chemical type, strand orientation, labels,
visualization methods and polymerase fields. They are not universally required:
Connie's four-field MGI molecular-probe requirement describes MGI's workflow,
not every MOD. Antibody preparation requirements remain outside this branch.
`derived_from_reagent_identifiers` points to separately submitted materials.
`source_template_identifiers` preserves an original template ID when its source
material, such as a non-cloned MGI probe, has no agreed Alliance class yet. It
is provenance, not an instruction to mint a placeholder clone. Likewise,
`preparation_assay_identifier` retains the provider's assay identity without
claiming it already resolves to an Alliance experiment.

A PCR product can retain its source template identifiers and description,
including genetic background. These are intentionally limited provenance
fields. Structured template/strain/primer-pair/observed-product modeling is
still open; do not treat them as a completed PCR experiment model.

## Associations and computational evidence

The shared association replaces PR #321's PCR-only association. It uses
entity-prefixed subject/object fields and supports evidence and notes using
existing EvidenceAssociation conventions. An association submitted separately
must resolve both its reagent identifier and its genomic-entity identifier.

The proposed runtime vocabulary distinguishes encoding, hybridization,
amplification, feature overlap and computational sequence support. Vocabulary
notes are candidate definitions, not seeded or JSON-enforced term lists.
Source relation text remains separate from the harmonized relation name.
MGI's approved P/missing-to-H conversion should preserve the raw source value
and its missing-value encoding; it does not establish a rule for another MOD.

For computed links, retain method, recorded version, source release, supporting
sequence identifiers and intervening transcript identifiers where available.
Gil describes FlyBase AEVAST sequence-to-transcript support in production and
gene-clone derivation in the reporting build. Its method version was not
recorded: omit it rather than inventing one. Lists of supporting identifiers
preserve contributors to one association; they do not encode every edge in a
multi-step analysis graph. More detailed computational provenance remains open.

A FlyBase read-anchoring FBcl record is outside this material hierarchy. Its
stable FBcl ID, library, EST/GenBank links, computed gene links and library-based
references must be preserved in a future sequence/provenance representation.
Do not submit it as DNAClone with availability `not available`. Availability
is not a substitute for biological classification. A clone with no library
link is not automatically a material or a read-anchoring record.

## Source mapping and remaining decisions

| Source evidence or feedback | Implemented first-iteration choice | What still needs work |
| --- | --- | --- |
| WormBase WS298 includes PCR products without primers or species | Optional primers/taxon; PCR method, conditions, generating Agents and shared genomic-entity links | SMap coordinates, exact Variation relation meaning, Amplified integer, Oligo identity, and Method interpretation |
| MGI primer products depend on assay/template background (Connie Smith) | No automatic primer-to-PCRProduct mapping | PrimerPair/assay-product and non-cloned material classes; meaning/export context of `prb_probe.productsize` |
| MGI preparations have stable, non-reused keys and belong to assays (Joel Richardson) | Separate preparation DTO, internal source identity, source assay identity | Probe replacement, deletion versus omitted export, Alliance retention policy; historical multi-assay-key discrepancy |
| MGI distinguishes preparation type, orientation, label and visualization | Separate fields, optional across MODs | Vocabulary ownership and any provider-specific validation profile |
| MGI A/E/H meanings and P/missing-to-H permission (Connie/Joel) | Shared typed association, raw relation and evidence/provenance | Export encodings for none/NULL/empty string; handling historical erroneous S |
| FlyBase library and membership types distinguish reagent clones from read anchors (Gil dos Santos, October 19) | Only confirmed materials enter clone collections; multiple sequence details remain separate | A standalone read-anchoring record model and missing-library exceptions |
| FlyBase computed sequence support and reporting-build gene-clone links (Gil) | Association-level method/release and supporting sequence/transcript IDs | Exact reporting export, structured derivation graph, relationship CV; do not infer expression-detection use |
| Xenbase has fifteen clones with two libraries; vector/site facts can be library-scoped | Multiple source descriptions, with separate library/clone-scoped fields | Shared Library/Vector identity; distinct Xenbase probe definition/preparation/use lifecycle |
| ZFIN expression can reference clones directly; EST/genomic and unspecified exceptions exist | Direct clone detection references; EST subtype only when cDNA identity is supported | Review conflicting or unspecified source classifications; no universal EST dispatch |
| RGD SSLPs are marker records with PCR-definition fields | No automatic reagent or detection-use mapping | Marker and PCR-definition models; reduced-copy limitations still apply |
| SGD and other MODs have related records without a demonstrated universal reagent path | No inferred detection relationships or new mandatory fields | Additional representative submissions and source-specific classification evidence |

The following cross-MOD decisions also remain open:

1. Confirm the abstract parent, polymorphic persistence and final association
   structure with Chris Grove, Chris Tabone and persistence/ingest owners.
   Authorization to build this prototype is not implementation approval.
2. Assign runtime vocabulary ownership and approve values for reagent type,
   availability, clone insert origin, vector type, sequence role, preparation properties, PCR method
   and genomic-entity relations. Unspecified, not applicable and unknown must
   remain distinct where the source distinguishes them.
3. Confirm source identity rules, provider qualification of private identifiers,
   Agent resolution, updates and load/deletion order. The inherited DTO contract
   intends exactly one of primary_external_id and mod_internal_id; this PR
   does not add a new global identity rule. Existing JSON validation does not
   replace identifier uniqueness or resolution checks in the loader.
4. Decide whether inline library and sequence details should become independently
   reusable entities. This first iteration preserves multiple details without
   inventing public library/vector identities.
5. Add coordinate-bearing mapping and richer computational provenance only after
   agreeing the reference sequence, assembly, interval and evidence semantics.
6. Resolve unsupported material definitions before admitting non-cloned MGI probes,
   synthetic oligos or primer-pair records. Generic DNAClone is not a fallback
   class for all of them.

## Expression integration and downstream work

The existing `ExpressionExperiment.detection_reagents` continues to range over
Reagent, so it can reference a clone, PCR product or preparation as well as an
antibody or construct. This PR fixes that slot's stale domain declaration from
ExpressionAnnotation to ExpressionExperiment. It does not narrow its range.
The existing `GeneExpressionExperimentDTO.detection_reagent_identifiers` and
gene-expression ingest collection from PR #325 are reused unchanged.

A downstream implementation must add persistence entities/registration,
services, DTO validators, vocabulary terms, identifier lookup and loading.
Load materials first, then preparation template links and genomic-entity
associations, then experiments using them. The exact order within material
collections and the handling of unresolved source provenance need loader design.
Schema acceptance alone does not establish that a submitted reference resolves
or that a curator's biological classification is correct.

## Changes relative to PR #321

| PR #321 | This proposal |
| --- | --- |
| PCRProduct directly under Reagent | PCRProduct under the shared abstract NucleicAcidReagent |
| Required taxon and both primer sequences | Optional source-supported values on entity and DTO |
| PCR-specific genomic-entity association | Shared evidence-supported reagent association, with computational/source provenance |
| Singular generated_by_identifier | Plural generated_by_identifiers matching entity cardinality |
| PCR ingest collection and association collection | Three material/preparation collections and one shared association collection |
| PCR-focused examples | Clone, preparation, legacy PCR, sequence/library and expression integration examples |

PR #321's unrelated functional-gene-set fixture correction is not copied into
this proposal. Generated artifacts remain CI-owned and are not committed here.
PR #321 is closed and is superseded by this proposal.

## Try the model

[The submission fixture](../test/data/nucleic_acid_reagent_test.json) contains
illustrative, explicitly `EXAMPLE`-named identifiers. It is not a verified MOD
export or a database transfer. It exercises every new collection, multiple
library memberships and reads, known and unspecified clone origin, synonym
evidence, missing taxon/primers,
assay-owned preparations, a computed association with unknown method version,
and the existing expression detection-reference path.

Eight separately invalid fixtures test missing provider, primer value type,
negative insert length, insert-origin, Agent and label cardinality, missing association target
and preparation-only fields incorrectly submitted on PCRProduct. These are
registered in the Makefile. Runtime CV membership, source semantics, uniqueness
and cross-record identifier resolution require downstream tests.

For local experiments with the repository's uv environment:

```sh
uv run gen-json-schema --closed -t Ingest model/schema/allianceModel.yaml > /tmp/nucleic-acid-ingest.schema.json
uv run linkml-validate -C Ingest -s model/schema/allianceModel.yaml test/data/nucleic_acid_reagent_test.json
```

## Evidence and discussion

The [curator review](https://model-preview.alliancegenome.org/reviews/nucleic-acid-reagents/)
requires an Alliance login. Its [MGI](https://model-preview.alliancegenome.org/reviews/nucleic-acid-reagents/mgi.html),
[FlyBase](https://model-preview.alliancegenome.org/reviews/nucleic-acid-reagents/flybase.html),
[WormBase](https://model-preview.alliancegenome.org/reviews/nucleic-acid-reagents/wormbase.html),
[Xenbase](https://model-preview.alliancegenome.org/reviews/nucleic-acid-reagents/xenbase.html),
[ZFIN](https://model-preview.alliancegenome.org/reviews/nucleic-acid-reagents/zfin.html),
[RGD](https://model-preview.alliancegenome.org/reviews/nucleic-acid-reagents/rgd.html) and
[SGD](https://model-preview.alliancegenome.org/reviews/nucleic-acid-reagents/sgd.html)
pages preserve the source paths, snapshot limitations, named feedback and
outstanding questions. New feedback through October 19 is incorporated here;
older review passages describing PR #325 as unmerged are historical.

## Validation of this iteration

Using the available LinkML 1.9.2 environment, compared with PR head
`0428ebfb` before the October 23 clone-origin revision:

- Closed Ingest JSON Schema generation and LinkML validation of the new
  submission fixture pass.
- Each of the eight invalid fixtures fails independently for its intended
  constraint, not an unrelated schema error.
- All 37 existing valid-directory fixtures have exactly the same JSON Schema
  validation results as the baseline. The three legacy functional-gene-set
  ALP/ARP/WNT examples each retain two pre-existing errors; this proposal
  introduces no new failures and does not repair those unrelated fixtures.
- The clone-origin slots are optional and single-valued. Known, omitted and
  explicit JSON-null origins pass validation. The empty clone subclasses and
  their separate ingest collections have been removed.
- Gitleaks, TruffleHog and staged whitespace checks pass. No generated artifact
  is included in the patch.

These checks validate schema structure and illustrative data, not production
MOD exports, runtime vocabulary membership or downstream persistence behavior.
