# agr_curation_schema — project context

LinkML model describing the Alliance of Genome Resources curation / persistence data
store. 27 schema files in `model/schema/`, aggregated via `allianceModel.yaml` imports.
Parallel `*DTO` (ingest) classes mirror the entity classes to separate *submission*
requirements from *database* requirements.

- Build, validation, and artifact generation are fully automated in CI (GitHub Actions).
  You do not need to build, run `make`, or run tests — CI handles all of it.
- `generated/` is build output — auto-regenerated and committed by CI; never hand-edit it.
- Downstream consumers: the `agr_curation` Java/Quarkus + Hibernate app, the data-ingest
  pipeline, and MOD data submitters (DQMs). Schema changes ripple into all of them.
- Conventions live in README → "Alliance Model Development Conventions".
- For PR-review specifics, see REVIEW.md.
