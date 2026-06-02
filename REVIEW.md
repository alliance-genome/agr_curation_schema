# REVIEW.md — Claude review guide for agr_curation_schema

This repo is the LinkML model for the Alliance curation / persistence data store.
Review changes against the repo conventions (README → "Alliance Model Development
Conventions") and the rubric below. Match the house style: terse, collegial,
specific. If a change looks correct, say so in one line. Do not pad with stylistic
nits and do not invent issues.

## Scope
- Review `model/schema/**` (the schema) and `test/data/**` (examples/tests).
- This is a read-only review. Do NOT run builds, `make`, the test suite, or any
  validation/regeneration commands — CI (GitHub Actions) does all of that. Review by
  reading the diff and the schema files only.
- IGNORE `generated/`. Those artifacts are auto-regenerated and committed by CI
  (`regenerate_artifacts.yaml`) and validated by `check-pull-request.yaml`. Never tell
  an author to "regenerate the artifacts" — CI does it. Only mention `generated/` if it
  appears hand-edited or out of sync with the source.
- Only flag issues the diff introduces; do not review pre-existing code.

## The core tension — read this first
Many fields are REQUIRED in the persistent database but MUST NOT be required at
ingest (Alliance-minted curies, generated IDs/HGVS, etc.). That is the entire reason
parallel `*DTO` (ingest) classes exist.
- Looser-than-the-database at ingest is usually CORRECT.
- Stricter-than-the-submission-source (FMS / DQM files) is usually a BUG.
- So: treat `required`/cardinality on DTO/ingest classes as a QUESTION for curators,
  not a defect.

## Assert these (mechanical, high-confidence — flag directly with file:line)
- DTO divergence (the #1 thing reviewers catch): a slot added to an entity class but
  missing the matching slot on its `*DTO` class, or using the wrong DTO suffix.
  Suffix rules: single ontology/curie ref -> `_curie`; multi -> `_curies`; reference
  to a SubmittedObject-derived entity -> `_identifier` / `_identifiers`; VocabularyTerm
  -> `_name` / `_names`; inlined DTO -> `_dto` / `_dtos`; plain string/boolean
  (e.g. `is_extinct`) -> same name.
- DTO description accuracy: a `_identifier` / `_name` slot whose `description:` still
  says "curie" (or otherwise contradicts its suffix/range).
- A new schema YAML file not added to `allianceModel.yaml` `imports:` (build-breaking).
- Redundant re-declaration of inherited slots — e.g. listing `curie`, `mod_entity_id`,
  `mod_internal_id`, `primary_external_id`, or `data_provider` on a child of
  `SubmittedObject`; or `subject`/`object`/`predicate` on a child of `Association`.
- Generic, unprefixed slot names (`status`, `url`, `name`, `group`, `type`) on a domain
  class -> suggest an entity-prefixed name (e.g. `bulkload_status`).
- `multivalued: true` with a singular name, or a plural name without `multivalued: true`.
- An Association using generic `subject`/`object` instead of entity-prefixed slot names
  (required by downstream Hibernate base-table constraints).
- A slot name identical to a class name (LinkML rejects it).
- A new class/slot with a missing or placeholder `description:` ("Dummy", empty).
- A new slot with no explicit `range:` (relying on `default_range: string`).
- Naming: classes CamelCase, slots snake_case.
- A new `date`-typed slot -> note the Java layer expects `OffsetDateTime`; confirm
  whether `datetime` is intended.
- A genuinely NEW entity/domain class with no `test/data/*.json` added in the PR
  (info-level only; do NOT raise this for ordinary slot additions). Also remind the
  author to register new test files in the Makefile (`SCHEMA_TEST_EXAMPLES` /
  `SCHEMA_TEST_EXAMPLES_INVALID`).

## Ask, do not assert (genuine judgment calls — pose as questions)
- Required vs optional AT INGEST — can DQMs actually supply this value at submission?
- Parent class / hierarchy placement — inheriting from `GenomicEntity` / `BiologicalEntity`
  forces a required curie/taxon; is that intended for this entity?
- New class vs. extending an existing one, or introducing a shared parent.
- Enum vs VocabularyTerm vs OntologyTerm — biological/curation values should usually be
  runtime-managed VocabularyTerms, not enums; ontology-backed slots should use the
  specific subclass (`SOTerm`) not generic `OntologyTerm`. Flag the pattern, ask the curator.
- A `domain:` constraint on a slot used (or likely to be used) by more than one class —
  it is documentation-only and tends to go stale; ask whether to drop it.
- Many-to-many modeling, load order, and association-vs-inlined choices — loader-dependent;
  defer to the curation/persistence team.
- "Does this match the persistent store / FMS / ABC database / the Java app?" — you cannot
  verify downstream repos; surface the question and ask the author to confirm alignment.

## Output
Post ONE top-level PR comment via `gh pr comment`. Structure it:
1. One-line summary of what the PR does.
2. Assertions (mechanical issues) with `file:line`.
3. Questions (judgment calls), clearly separated from assertions.
4. A brief overall note. Keep the whole thing tight.
