SRC_DIR = model
SCHEMA_DIR = $(SRC_DIR)/schema
SOURCE_FILES := $(shell find $(SCHEMA_DIR) -name '*.yaml')
SCHEMA_NAMES = $(patsubst $(SCHEMA_DIR)/%.yaml, %, $(SOURCE_FILES))

SCHEMA_NAME = allianceModel
SCHEMA_SRC = $(SCHEMA_DIR)/$(SCHEMA_NAME).yaml
#TGTS = graphql jsonschema docs shex owl csv  python
TGTS = jsonschema jsonld-context python docs
JAVA_GEN_OPTS = --output_directory org/alliancegenome/curation/model --package org.alliancegenome.curation.model
DDL_GEN_OPTS = --sqla-file target/sqla-files/

#GEN_OPTS = --no-mergeimports
GEN_OPTS =

all: gen stage
gen: $(patsubst %,gen-%,$(TGTS))
.PHONY: all gen stage clean clean-artifacts clean-docs t echo test install docserve gh-deploy .FORCE

clean: clean-artifacts clean-docs

clean-artifacts:
	rm -rf target/

clean-docs:
	ls docs/*.md | egrep -v 'README.md|README.markdown' | xargs rm -f # keep readme files
	rm -f docs/images/*
	rm -f docs/types/*

t:
	echo $(SCHEMA_NAMES)

echo:
	echo $(patsubst %,gen-%,$(TGTS))

test: all test-jsonschema test-jsonschema_invalid

install:
#	. environment.sh
	pipenv install -r requirements.txt

tdir-%:
	mkdir -p target/$*

docs:
	mkdir -p $@
	mkdir -p $@/images

stage: $(patsubst %,stage-%,$(TGTS))
stage-%: gen-%
	cp -pr target/$* .


###  -- MARKDOWN DOCS AND SLIDES --
# Generate documentation ready for mkdocs
# TODO: modularize imports
gen-docs: target/docs/index.md copy-src-docs
.PHONY: gen-docs
copy-src-docs:
	mkdir -p target/docs/images
	cp $(SRC_DIR)/docs/*.md target/docs/
	cp $(SRC_DIR)/docs/images/* target/docs/images/
PHONY: copy-src-docs
target/docs/%.md: $(SCHEMA_SRC) tdir-docs
	pipenv run gen-markdown $(GEN_OPTS) --dir target/docs $<
stage-docs: gen-docs
	cp -pr target/docs .

###  -- PYTHON --
gen-python: $(patsubst %, target/python/%.py, $(SCHEMA_NAMES))
.PHONY: gen-python
target/python/%.py: $(SCHEMA_DIR)/%.yaml  tdir-python
# --no-mergeimports was causing an import error
#	gen-py-classes --no-mergeimports $(GEN_OPTS) $< > $@
	pipenv run gen-py-classes --mergeimports $(GEN_OPTS) $< > $@

###  -- GRAPHQL --
gen-graphql:target/graphql/$(SCHEMA_NAME).graphql
.PHONY: gen-graphql
target/graphql/%.graphql: $(SCHEMA_DIR)/%.yaml tdir-graphql
	pipenv run gen-graphql $(GEN_OPTS) $< > $@

###  -- JSON SCHEMA --
gen-jsonschema: target/jsonschema/$(SCHEMA_NAME).schema.json
.PHONY: gen-jsonschema
target/jsonschema/%.schema.json: $(SCHEMA_DIR)/%.yaml tdir-jsonschema
	pipenv run gen-json-schema $(GEN_OPTS) --closed -t ingest $< > $@

###  -- JSONLD Context --
gen-jsonld-context: target/jsonld-context/$(SCHEMA_NAME).context.jsonld
.PHONY: gen-jsonld-context
target/jsonld-context/%.context.jsonld: $(SCHEMA_DIR)/%.yaml tdir-jsonld-context
	pipenv run gen-jsonld-context $(GEN_OPTS) $< > $@

###  -- SHEX --
# one file per module
gen-shex: $(patsubst %, target/shex/%.shex, $(SCHEMA_NAMES))
.PHONY: gen-shex
target/shex/%.shex: $(SCHEMA_DIR)/%.yaml tdir-shex
	pipenv run gen-shex --no-mergeimports $(GEN_OPTS) $< > $@

###  -- CSV --
# one file per module
gen-csv: $(patsubst %, target/csv/%.csv, $(SCHEMA_NAMES))
.PHONY: gen-csv
target/csv/%.csv: $(SCHEMA_DIR)/%.yaml tdir-csv
	pipenv run gen-csv $(GEN_OPTS) $< > $@

###  -- OWL --
# TODO: modularize imports. For now imports are merged.
gen-owl: target/owl/$(SCHEMA_NAME).owl.ttl
.PHONY: gen-owl
target/owl/%.owl.ttl: $(SCHEMA_DIR)/%.yaml tdir-owl
	pipenv run gen-owl $(GEN_OPTS) $< > $@

###  -- RDF (direct mapping) --
# TODO: modularize imports. For now imports are merged.
gen-rdf: target/rdf/$(SCHEMA_NAME).ttl
.PHONY: gen-rdf
target/rdf/%.ttl: $(SCHEMA_DIR)/%.yaml tdir-rdf
	pipenv run gen-rdf $(GEN_OPTS) $< > $@

###  -- LINKML --
# linkml (copy)
# one file per module
gen-linkml: target/linkml/$(SCHEMA_NAME).yaml
.PHONY: gen-linkml
target/linkml/%.yaml: $(SCHEMA_DIR)/%.yaml tdir-limkml
	cp $< > $@

# test docs locally.
docserve:
	pipenv run mkdocs serve

gh-deploy:
# deploy documentation (note: requires documentation is in docs dir)
	pipenv run mkdocs gh-deploy --remote-branch gh-pages --force --theme readthedocs

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
	cp python/*.py agr_schema/ # copy python files
	cp jsonschema/allianceModel.schema.json agr_schema/ # copy allianceModel json schema
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
	disease_test \

SCHEMA_TEST_EXAMPLES_INVALID := \
	allele_invalid \
	disease_allele_invalid \

.PHONY: test-jsonschema
test-jsonschema: $(foreach example, $(SCHEMA_TEST_EXAMPLES), validate-$(example))

.PHONY: test-jsonschema_invalid
test-jsonschema_invalid: $(foreach example, $(SCHEMA_TEST_EXAMPLES_INVALID), validate-invalid-$(example))

validate-%: test/data/%.json jsonschema/allianceModel.schema.json
# util/validate_allianceModel_json.py -i $< # example of validating data using the cli
	pipenv run jsonschema -i $< $(word 2, $^)

validate-invalid-%: test/data/invalid/%.json jsonschema/allianceModel.schema.json
	! pipenv run jsonschema -i $< $(word 2, $^)

# ---------------------------------------
# Java
# ---------------------------------------
gen-java: $(patsubst %, target/java/%.java, $(SCHEMA_NAMES))
.PHONY: gen-java

target/java/%.java: $(SCHEMA_DIR)/%.yaml tdir-java
	pipenv run gen-java $(JAVA_GEN_OPTS)  $< > $@
