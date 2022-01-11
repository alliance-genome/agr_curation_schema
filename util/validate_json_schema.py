#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provides CLI to validate json files against the agr_curation jsonschema."""

import click
import json
import jsonschema


def is_valid_json(json_file: str, database_set: str = "") -> bool:
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

        database_set = database_set.strip()
        if len(database_set) > 0:
            if type(json_data) == type([]):
                json_data = {f"{database_set}": json_data}
            else:
                json_data = {f"{database_set}": [json_data]}
    try:
        jsonschema.validate(instance=json_data, schema=get_nmdc_dict())
    except jsonschema.exceptions.ValidationError as err:
        print(err.message)
        return False

    return True


##### CLI interface #####
@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option(
    "--input",
    "-i",
    help="the path the file containing json formatted data.",
)
@click.option(
    "--database-set",
    "-set",
    default="",
    help="An optional top level database set (e.g, study_set, biosample_set) that contains the data.",
)
def cli(input: str, database_set: str):
    if is_valid_json(input, database_set):
        click.echo("%s: The JSON data is VALID for NMDC schema." % input)
    else:
        click.echo("%s: The JSON data is ** NOT ** valid for NMDC schema." % input)


if __name__ == "__main__":
    cli()  # CLI interface