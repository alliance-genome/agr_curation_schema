# LinkML Model to describe the Alliance curation/persistence data store
Model to describe the Alliance curation/persistence data store

## [Documentation](https://alliance-genome.github.io/agr_curation_schema/)

## Developing the AGR Curation Schema 


## Building a new release of AGR Curation Schema

## Examples of valid ingest files and tests

The Makefile in this repository runs a series of json schema validation tests using test data stored in this repository.
Test data are located in the 'test/data' directory which is split into example data that are valid JSON according
to the Alliance JSON schema, and data that are invalid accordingly.

To run the tests in this repository:
```bash
make test
```


## Generating MOD JSON files and validating them

The Alliance JSON schema is generated from the Alliance model yaml in src/schema in this repository.  Also provided in 
this repository is a simple JSON schema validator (util/validate_agr_schema.py) that has a command line interface.

For users wishing to run a validator locally before submitting their files to the Alliance, this can be done by:

1. clone the agr_curation_schema locally 
```bash
git clone https://github.com/alliance-genome/agr_curation_schema
```

2. validate a local JSON file against the schema
```bash
python util/validate_agr_schema.py -i path_to_the_json_data_to_validate
```

example command using test data:
```bash
python util/validate_agr_schema.py -i test/allele_ingest_test.json
```

note: it's good practice to use a python virtual environment when running commands as the installed version of python
on most Mac operating systems is version 2 vs. version 3.  The simplest way to do that is like this:
```bash
pyvenv venv
source venv/bin/activate
export PYTHONPATH=.:$PYTHONPATH
pip install -r requirements.txt
```

## GitHub Actions

