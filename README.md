# LinkML Model to describe the Alliance curation/persistence data store
Model to describe the Alliance curation/persistence data store

## [Documentation](https://alliance-genome.github.io/agr_curation_schema/)

## Developing the AGR Curation Schema 

The Alliance schema is stored in a series of interconnected YAML files in the `model/schema` directory written using
[LinkML syntax](https://linkml.io/linkml/intro/tutorial.html). LinkML is an object-oriented modeling language, tutorial 
[here](https://linkml.io/linkml/intro/tutorial.html) with tooling that can convert simple, easy to author YAML into 
validatable artifacts such as: JSON schemas, SQL DDL, python and java classes, markdown documentation and others.  
Some of these artifact types and generated and stored in this repository as well including JSON schemas that are used
to submit data.  

The main modeling components of any LinkML model are: classes, slots, enumerations and types.  

### Classes 

Classes are a set or category of things having some property or attribute in common and differentiated from others by 
kind, type, or quality.

### Slots

Slots (synonym: attributes) are properties or attributes of classes and can be specified once and reused in many 
classes in the model. 

### Types

Types 

### Alliance Development Conventions

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




## Building a new release of AGR Curation Schema

## Examples of valid ingest files and tests

The Makefile in this repository runs a series of json schema validation tests using test data stored in this repository.
Test data are located in the 'test/data' directory which is split into example data that are valid JSON according
to the Alliance JSON schema, and data that are invalid.  

To run the tests in this repository:
```bash
make test
```

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

The Alliance JSON schema is generated from the Alliance model yaml in model/schema in this repository.  Also provided in 
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

