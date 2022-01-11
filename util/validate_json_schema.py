#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provides CLI to validate json files against the NMDC jsonschema."""

import click
import json
from pprint import pprint
import jsonschema


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
    with open(json_file, "r") as fh:
        json_data = json.load(fh)
    with open(schema_file) as json_file:
        schema_dict = json.load(json_file)
    try:
        jsonschema.validate(instance=json_data, schema=schema_dict)
    except jsonschema.exceptions.ValidationError as err:
        print(err.message)
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
    "-schema",
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