SRC_DIR = model
SCHEMA_DIR = $(SRC_DIR)/schema
SOURCE_FILES := $(shell find $(SCHEMA_DIR) -name '*.yaml')
SCHEMA_NAMES = $(patsubst $(SCHEMA_DIR)/%.yaml, %, $(SOURCE_FILES))

SCHEMA_NAME = allianceModel
SCHEMA_SRC = $(SCHEMA_DIR)/$(SCHEMA_NAME).yaml

ARTIFACTS_DIR=generated
TARGET_DIR=$(ARTIFACTS_DIR)/target
#TGTS = graphql jsonschema docs shex owl csv  python
TGTS = jsonschema
# ARTIFACT_TGTS = python jsonschema jsonld-context sqlddl owl shex java docs
ARTIFACT_TGTS = jsonschema
JAVA_GEN_OPTS = --output-directory $(ARTIFACTS_DIR)/java/org/alliancegenome/curation/model --package org.alliancegenome.curation.model
DDL_GEN_OPTS = --sqla-file $(TARGET_DIR)/sqla-files/

all: clean gen stage
artifacts: clean-artifacts gen-artifacts stage-artifacts
gen: $(patsubst %,gen-%,$(TGTS))
.PHONY: all gen clean t echo test install gh-deploy-docs clean-artifacts clean-doc clean-artifacts gen-artifacts clean-docs .FORCE

gen-artifacts: $(patsubst %,gen-%,$(ARTIFACT_TGTS)) $(patsubst %,stage-%,$(ARTIFACT_TGTS))

clean: clean-jsonschema

clean-jsonschema:
	rm -rf $(TARGET_DIR)/*
	rm -rf $(ARTIFACTS_DIR)/jsonschema/*

clean-artifacts:
	rm -rf $(TARGET_DIR)/*
	rm -rf $(ARTIFACTS_DIR)/*

clean-docs:
	rm -rf $(ARTIFACTS_DIR)/docs/images/*
	rm -rf $(ARTIFACTS_DIR)/docs/types/*
	rm -rf $(ARTIFACTS_DIR)/docs/

t:
	echo $(SCHEMA_NAMES)

echo:
	echo $(patsubst %,gen-%,$(TGTS))

test: all test-jsonschema

install:
	poetry install

tdir-%:
	mkdir -p $(TARGET_DIR)/$*

docs:
	mkdir -p $ARTIFACTS_DIR/$@
	mkdir -p $ARTIFACTS_DIR/$@/images

stage: $(patsubst %,stage-%,$(TGTS))

stage-artifacts: $(patsubst %,stage-%,$(ARTIFACT_TGTS))

stage-%: gen-%
	cp -pr $(TARGET_DIR)/$* $(ARTIFACTS_DIR)/

gen-docs:
	poetry run gen-doc model/schema/allianceModel.yaml --directory $(TARGET_DIR)/docs --template-directory doc_templates

stage-docs: gen-docs
	cp -pr $(TARGET_DIR)/docs $(ARTIFACTS_DIR)/
	cp css/extra_css.css $(ARTIFACTS_DIR)/docs/
	cp README.md $(ARTIFACTS_DIR)/docs/developing-the-model.md

serve-docs: stage-docs
	poetry run mkdocs serve

$(ARTIFACTS_DIR)/guidelines/%.md: $(ARTIFACTS_DIR)/docs/index.md
	cp -R $(ARTIFACTS_DIR)/guidelines/* $(dir $@)

# add more logging?
# some docs pages not being created
# usage of mkdocs.yml attributes like analytics?

###  -- PYTHON --
gen-python: $(patsubst %, $(TARGET_DIR)/python/%.py, $(SCHEMA_NAMES))
.PHONY: gen-python
$(TARGET_DIR)/python/%.py: $(SCHEMA_DIR)/%.yaml  tdir-python
# --no-mergeimports was causing an import error
#	gen-py-classes --no-mergeimports $(GEN_OPTS) $< > $@
	poetry run gen-py-classes --mergeimports $(GEN_OPTS) $< > $@

###  -- GRAPHQL --
gen-graphql:$(TARGET_DIR)/graphql/$(SCHEMA_NAME).graphql
.PHONY: gen-graphql
$(TARGET_DIR)/graphql/%.graphql: $(SCHEMA_DIR)/%.yaml tdir-graphql
	poetry run gen-graphql $(GEN_OPTS) $< > $@

###  -- JSON SCHEMA --
gen-jsonschema: $(TARGET_DIR)/jsonschema/$(SCHEMA_NAME).schema.json
.PHONY: gen-jsonschema
$(TARGET_DIR)/jsonschema/%.schema.json: $(SCHEMA_DIR)/%.yaml tdir-jsonschema
	poetry run gen-json-schema $(GEN_OPTS) --indent 4 --closed -t ingest $< > $@


###  -- SQL --
gen-sqlddl: $(TARGET_DIR)/sqlddl/$(SCHEMA_NAME).sql
.PHONY: gen-sqlddl
$(TARGET_DIR)/sqlddl/%.sql: $(SCHEMA_DIR)/%.yaml tdir-sqlddl
	poetry run gen-sqlddl $(GEN_OPTS) $< > $@

###  -- JSONLD Context --
gen-jsonld-context: $(TARGET_DIR)/jsonld-context/$(SCHEMA_NAME).context.jsonld
.PHONY: gen-jsonld-context
$(TARGET_DIR)/jsonld-context/%.context.jsonld: $(SCHEMA_DIR)/%.yaml tdir-jsonld-context
	poetry run gen-jsonld-context $(GEN_OPTS) $< > $@

###  -- SHEX --
# one file per module
gen-shex: $(patsubst %, $(TARGET_DIR)/shex/%.shex, $(SCHEMA_NAMES))
.PHONY: gen-shex
$(TARGET_DIR)/shex/%.shex: $(SCHEMA_DIR)/%.yaml tdir-shex
	poetry run gen-shex --no-mergeimports $(GEN_OPTS) $< > $@

###  -- CSV --
# one file per module
gen-csv: $(patsubst %, $(TARGET_DIR)/csv/%.csv, $(SCHEMA_NAMES))
.PHONY: gen-csv
$(TARGET_DIR)/csv/%.csv: $(SCHEMA_DIR)/%.yaml tdir-csv
	poetry run gen-csv $(GEN_OPTS) $< > $@

###  -- OWL --
# TODO: modularize imports. For now imports are merged.
gen-owl: $(TARGET_DIR)/owl/$(SCHEMA_NAME).owl.ttl
.PHONY: gen-owl
$(TARGET_DIR)/owl/%.owl.ttl: $(SCHEMA_DIR)/%.yaml tdir-owl
	poetry run gen-owl $(GEN_OPTS) $< > $@

###  -- RDF (direct mapping) --
# TODO: modularize imports. For now imports are merged.
gen-rdf: $(TARGET_DIR)/rdf/$(SCHEMA_NAME).ttl
.PHONY: gen-rdf
$(TARGET_DIR)/rdf/%.ttl: $(SCHEMA_DIR)/%.yaml tdir-rdf
	poetry run gen-rdf $(GEN_OPTS) $< > $@

###  -- LINKML --
# linkml (copy)
# one file per module
gen-linkml: $(TARGET_DIR)/linkml/$(SCHEMA_NAME).yaml
.PHONY: gen-linkml
$(TARGET_DIR)/linkml/%.yaml: $(SCHEMA_DIR)/%.yaml tdir-limkml
	cp $< > $@

gh-deploy-docs: stage-docs
# deploy documentation (note: requires documentation is in docs dir)
	poetry run mkdocs gh-deploy --remote-branch gh-pages --force

###  -- PYPI TARGETS
# Use the build-package target to build a PYPI package locally
# This is usefule for testing
.PHONY: clean-package build-package deploy-pypi
clean-package:
	rm -rf dist && echo 'dist removed'
	rm -rf agr_schema.egg-info && echo 'egg-info removed'
	rm -f agr_schema/*.py
	rm -f agr_schema/*.json
	rm -f agr_schema/*.tsv

build-package: clean-package
	cp model/schema/allianceModel.yaml agr_schema/ # copy allianceModel yaml file
	cp $(ARTIFACTS_DIR)/python/*.py agr_schema/ # copy python files
	cp $(ARTIFACTS_DIR)/jsonschema/allianceModel.schema.json agr_schema/ # copy allianceModel json schema
	cp util/validate_agr_json.py agr_schema/ # copy command-line validation tool
	python setup.py bdist_wheel sdist

deploy-pypi:
# deploys package to pypi
# note: you need to have a pypi account
# properly configured .pypirc file
	twine upload dist/* --verbose

deploy-testpypi:
# deploys package to testpypi
# note: you need to have a testpypi account
# or properly configured .pypirc file
	twine upload -r testpypi dist/* --verbose

##  -- TEST/VALIDATE JSONSCHEMA

# datasets used test/validate the schema
SCHEMA_TEST_EXAMPLES := \
	allele_test \
	disease_allele_test \
	disease_agm_test \
	disease_gene_test \
	gene_test \
	wb_disease_test \
	variant_test \
	agm_test \
	sqtr_test \
	ontology_closure_test \
	allele_association_ingest_test \
 	variant_allele_association_test \
 	sgd_disease_test \
 	fb_disease_test \
 	allele_slot_annotation_ingest_test \


SCHEMA_TEST_EXAMPLES_INVALID := \
	allele_invalid \
	disease_allele_invalid \
	variant_invalid \

.PHONY: test-jsonschema
test-jsonschema: $(foreach example, $(SCHEMA_TEST_EXAMPLES), validate-$(example))

.PHONY: test-jsonschema_invalid
test-jsonschema_invalid: $(foreach example, $(SCHEMA_TEST_EXAMPLES_INVALID), validate-invalid-$(example))

validate-%: test/data/%.json $(ARTIFACTS_DIR)/jsonschema/allianceModel.schema.json
# util/validate_allianceModel_json.py -i $< # example of validating data using the cli
	# poetry run jsonschema -i $< $(word 2, $^)
	poetry run linkml-validate -C Ingest -s model/schema/allianceModel.yaml -s model/schema/allianceModel.yaml $<
validate-invalid-%: test/data/invalid/%.json $(ARTIFACTS_DIR)/jsonschema/allianceModel.schema.json
	! poetry run jsonschema -i $< $(word 2, $^)


# ---------------------------------------
# Java
# ---------------------------------------
gen-java: $(patsubst %, $(TARGET_DIR)/java/%.java, $(SCHEMA_NAMES))
.PHONY: gen-java

$(TARGET_DIR)/java/%.java: $(SCHEMA_DIR)/%.yaml tdir-java
	poetry run gen-java $(JAVA_GEN_OPTS)  $<

run-tests: 
	docker build -t agr_curation_schema .
	docker run -i -t --name agr_curation_schema agr_curation_schema

remove-container:
	docker stop agr_curation_schema
	docker rm agr_curation_schema

