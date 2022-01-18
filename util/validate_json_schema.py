#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provides CLI to validate json files against the NMDC jsonschema."""

import click
import json
from pprint import pprint
import jsonschema
import os


def is_valid_json(json_file: str, schema_file: str) -> bool:
    """
    Determines if the data in json_file conforms to the NMDC json schema.
    Parameters
    ----------
    json_file : str
        Path to the file containing json formatted data.
    database_set : str, default=""
        An optional top level database set (e.g, study_set, biosample_set) that contains the data.
    Returns
    -------
    bool
        True if data conforms to the NMDC json schema; False otherwise.
    """

    with open(json_file) as data_file:
        data = json.load(data_file)

    schema_file_name = schema_file
    with open(schema_file_name) as schema_file:
        schema = json.load(schema_file)

    # Defining a resolver for relative paths and schema issues, see https://github.com/Julian/jsonschema/issues/313
    # and https://github.com/Julian/jsonschema/issues/274
    schema_dir = os.path.dirname(os.path.abspath(schema_file_name))
    resolver = jsonschema.RefResolver(base_uri='file://' + schema_dir + '/', referrer=schema)

    try:
        jsonschema.validate(data, schema, format_checker=jsonschema.FormatChecker(), resolver=resolver)
        print("'%s' successfully validated against '%s'" % (json_file, schema_file_name))
    except jsonschema.ValidationError as e:
        print(e.message)
        print(e)
        return False
    except jsonschema.SchemaError as e:
        print(e.message)
        print(e)
        return False
    return True


##### CLI interface #####
@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option(
    "--input",
    "-i",
    help="the path to the file containing json data to validate.",
)
@click.option(
    "--schema_file",
    "-s",
    default="",
    help="the path to the file containing the json schema to validate against.",
)
def cli(input: str, schema_file: str):
    if is_valid_json(input, schema_file):
        click.echo("%s: Valid JSON data." % input)
    else:
        click.echo("%s: The JSON data is ** NOT ** valid." % input)


if __name__ == "__main__":
    cli()