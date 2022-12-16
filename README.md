# LinkML Model to describe the Alliance curation/persistence data store
Model to describe the Alliance curation/persistence data store

## [Model Components and Visualizations](https://alliance-genome.github.io/agr_curation_schema/)

## Developing the AGR Curation Schema 

The Alliance schema is stored in a series of interconnected YAML files in the `model/schema` directory written using
[LinkML syntax](https://linkml.io/linkml/intro/tutorial.html). LinkML is an object-oriented modeling language, tutorial 
[here](https://linkml.io/linkml/intro/tutorial.html) with tooling that can convert simple, easy to author YAML into 
validatable artifacts such as: JSON schemas, SQL DDL, python and java classes, markdown documentation and others.
  
Some of these artifact types and generated and stored in this repository as well including JSON schemas that are used
to submit data.  The main modeling components of any LinkML model are: classes, slots, enumerations and types.  

### Classes 

Classes are a set or category of things having some property or attribute in common and differentiated from others by 
kind, type, or quality.

### Slots

Slots (synonym: attributes) are properties or attributes of classes and can be specified once and reused in many 
classes in the model. 

### Types

Types can be "string" or "integer" per many language specifications, but if custom types can also be defined.  Alliance model reuses a custom LinkML type (URIorCurie) which restricts a slot value to a URI or CURIE data type. 

### Enums

Enumerations are objects that are used to restrict the values of a particular slot to those declared in the 
enumeration.

### Alliance Model Development Conventions

In addition to LinkML conventions, this repository follows a series of local conventions.    

- classes should be written in CamelCase
- slots should be written in snake_case

The Schema is divided into several YAML files roughly by biological domain.  There are two special YAML files that
behave differently from the rest:

`model/schema/allianceModel.yaml`

allianceModel.yaml is the grouping schema file for all the other split out schemas (YAML files).  In its "imports"
section, all the other YAML files are listed by name.  This helps the automated regeneration of artifacts (like 
JSONSchema, python, java files) to find and combine all the sub schemas together.  When adding a new YAML file (a new
biological domain, or new schema component file) be sure to add your schema file as an import to allianceModel.yaml
   
`model/schema/core.yaml` 

The core.yaml file holds classes and
attributes that should or can be reused in several of the biological domains (e.g. AuditedObject, a class that holds
all relevant data tracking information is a parent class of all other biological objects that need to be audited.  
AuditedObject lives in core.yaml)

##### Tests

Any time a new domain is developed, a test should be written to exercise the resulting JSON schema artifact.  This helps
provide example data for people seeking to produce data to our standard, and helps test the model for model developers.
Test data belongs in `test/data` and `test/invalid/data`.  Test files should be named following these conventions:

valid test data files: `"test_name"_test.json`

invalid test data files: `"test_name"_invalid.json`

And test file should be added (for the moment, we can turn this into a configuration file in another iteration) in the
Makefile collections:
SCHEMA_TEST_EXAMPLES,
SCHEMA_TEST_EXAMPLES_INVALID

`test/data/allele_test.json` and `test/data/invalid/allele_invalid.json` are good examples of how to do this.

An easy way to write a test is to pull out the 'required' fields of a domain object from `jsonschema/allianceModel.schema.json`
and write test data according to those required fields.  Alternatively, a few submission objects from an existing submission
will be a better exercise of the schema when not many fields are required.  

## Building the Artifacts of the AGR Curation Schema

Artifacts of the AGR Curation Schema are defined as all the schema transformations that are automatically conducted 
via the Makefile in this repository.   These artifact are generated using LinkML software added as a dependency in this
repository.

In the `Makefile` here, all the different kinds of generated artifact targets are prefixed with 'gen-' to indicate that
those targets create a specific kind of file.  For example, the `gen-jsonschema` target generates the allianceModel.schema.json
file are executed when `make` or `make all` is run from the command line.  The github actions in this repository also
use these Makefile targets to generate the artifacts for a pull request or for a release of the repository.

To regenerate python, java, jsonschema, etc. locally, run `make` from the command line.
Two other important targets exist in the Makefile for this repository: stage and test.  Stage moves all the assembled 
artifacts that are generated in a non-checked-in directory (`target` directory) into the top of the repository for 
easier finding and for easier packaging of these artifacts.  `stage` is executed as part of the build targets in the Makefile
via github actions (GA) and so developers can ignore these targets in favor of automated builds via GA.

To make a schema change and test your changes:

1. checkout a new branch for development
   ```bash
   git checkout -b new_branch_name
   ```
2. change the appropriate YAML file in `model/schema`
3. rebuild all your artifacts (this in itself is a test of the validity of your schema change):
    ```bash
    make
    ```
4. add or modify an existing test in `test/data` and `test/data/invald`
5. add your new test, or verify the test you changed is available in the Makefile for execution.
6. run the tests to confirm that your test data is validated against the generated JSONschema artifact that you made in 
step 2 above.
    ```bash
    git add test/data/[new_]test.json # optional step if you added a new test
    make clean
    make test 
    ```
7. commit your change and open pull request.
    ```bash
   git commit -a -m "message indicating what you changed." 
   ```

## Examples of valid ingest files and tests

The Makefile in this repository runs a series of json schema validation tests using test data stored in this repository.
Test data are located in the `test/data` directory which is split into example data that are valid JSON according
to the Alliance JSON schema, and data that are invalid.

The invalid tests will report how they are invalid, and expect to be invalid so that a passing 'invalid' test will 
report how its invalid but not break the build.  This is a convenient way to exercise the schema and make subtle errors
more clearly stated.

To run the tests in this repository:
```bash
make clean
make test
```

This will run both the valid and invalid tests. 

Note there is a convention in this repository to make a 'set' slot for each ingest as a convenient convention for 
being able to validate objects in a JSON list.  In the example below, an "allele ingest set" is defined in the 
model as being a multivalued slot that contains Allele objects.  In this way, the JSON validator and automated
tests can validate that the submission is a list of Allele objects (as opposed to a list of Gene objects, or a 
list of GOTerm objects).  A simple example (using only the required fields of the Allele object), would look like this:

```json
{
  "allele_ingest_set": [
    {
      "curie": "ZFIN:ZDB-ALT-123456-1",
      "taxon": "NCBITaxon:7955",
      "created_by": "ZFIN",
      "modified_by": "ZFIN"
    },
    {
      "curie": "ZFIN:ZDB-ALT-123456-2",
      "taxon": "NCBITaxon:7955",
      "created_by": "ZFIN",
      "modified_by": "ZFIN"
    }
  ]
}
```

## Generating MOD JSON files and validating them

The Alliance JSON schema is generated from the Alliance model YAML in `model/schema` in this repository.  Also provided in 
this repository is a simple JSON schema validator (`util/validate_agr_schema.py`) that has a command line interface.

For users wishing to run a validator locally before submitting their files to the Alliance, this can be done by:

1. cloning the agr_curation_schema locally: 
```bash
git clone https://github.com/alliance-genome/agr_curation_schema
```

2. validating a local JSON file against the schema:
make sure you have linkml installed (see above for instructions on how to install the agr_curation_schema dependencies into your 
python environment).  Then run the validator:
```bash
poetry run linkml-validate -C Ingest -s model/schema/allianceModel.yaml -s model/schema/allianceModel.yaml [path/to/your/submission/file.json]
```

example command using test data (replace test/allele_ingest_test.json with the path to your submission.json):
```bash
poetry run linkml-validate -C Ingest -s model/schema/allianceModel.yaml -s model/schema/allianceModel.yaml test/allele_ingest_test.json
```

note: it's good practice to use a python virtual environment when running commands as the installed version of python
(for example, on most Mac operating systems is version 2 vs. version 3).  
Here is a guide for working with python and poetry virtual environments: https://berkeleybop.github.io/best_practice/python_environments
Note, the guide above has been tested with a wide variety of biomedical python projects and is a great learning guide
for working with python and virtual environments.

The basic steps for setting up a system with multiple versions of python and virtual environments are:
1) Install pyenv, homebrew is a good method for installing pyenv:
```bash
brew update
brew install pyenv
```
once installed, you can add many versions of python to your system using pyenv:
```bash
pyenv install 3.8.15
pyenv global 3.8.15
```

2) Install poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -
poetry config virtualenvs.in-project true
poetry config virtualenvs.prefer-active-python true
```

3) Creating a virtual environment with poetry
```bash
git clone https://github.com/alliance-genome/agr_curation_schema
git checkout -b my_new_branch
cd agr_curation_schema
poetry install  
```

5) Run the tests
```bash
make test
```

## Alternate development environment - Using Docker

1) install docker
2) build the docker image
```bash
docker build -t agr_curation_schema .
```
3) run the docker image
```bash
docker run -t -d --name agr_curation_schema agr_curation_schema
```
4) invade the running container
```bash
docker exec -it agr_curation_schema /bin/bash
```
5) clone the repo
```bash
git clone https://github.com/alliance-genome/agr_curation_schema
cd agr_curation_schema
git checkout my_branch_to_run_tests
```
6) install the project
```bash
poetry install
```
7) run the tests
```bash
make test
```

## Alternate alternate test environment - just use pipx on MacOS
1) install pipx
```bash
brew install pipx --user
```
2) run tests in an isolated pipx environment
```bash
pipx run --spec linkml linkml-validate -C Ingest -s model/schema/allianceModel.yaml -s model/schema/allianceModel.yaml test/data/allele_test.json
```

If you need to make changes based on test results, you may wish to configure git 
according to https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls
in order to avoid having to enter your github credentials every time you push a change.


## GitHub Actions

There are three GitHub action files that are triggered based on actions that occur on this repository.

1. ```check-pull-request.yaml```

On each pull request, the artifacts (JSONSchema, doc, python, java etc) are run in order to generate fresh models
in those languages based on the changed schema YAML files.  

Once the artifacts are built, the action also runs the test suite against the new schema to insure the tests data still
passes the schema.  One should change the tests when changing the schema in order to have PRs pass this check.

2. ```build-deploy-documentation.yaml```

On each merge into main, the docs are regerated (regenerated with a [linkml generator](https://linkml.io/linkml/generators/markdown.html)) using the model/schema/\*.yaml files, generates markdown documentation and UML diagrams and pushes them into the gh-pages branch of this repository.  
Note: the documentation is only stored in the gh-pages branch only, not in the main repository.

This process is controlled in part by the mkdocs.yaml file in this repo which declares the source and site documentation repos and the location of the navigation index.html.

3. ```pypi-publish.yaml```

On release, this action is run to assembly and push this repository to PYPI automatically.  This is currently disabled for
Alliance Schema.  

