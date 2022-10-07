#!/usr/bin/env python3

import jsonschema
import json
from typing import Dict
import click


def get_agr_jsonschema_dict() -> Dict:
    """Parses the agr.schema.json file into a dict.

    Returns
    -------
    dict
        The dict of the keys and value in the agr.schema.json file.
    """
    json_schema_file = open('jsonschema/allianceModel.schema.json')
    return json.load(json_schema_file)


def is_valid_json(json_file: str) -> bool:
    """
    Determines if the data in json_file conforms to the agr json schema.

    Parameters
    ----------
    json_file : str
        Path to the file containing json formatted data.
    Returns
    -------
    bool
        True if data conforms to the agr json schema; False otherwise.
    """
    with open(json_file, "r") as fh:
        json_data = json.load(fh)

    try:
        jsonschema.validate(instance=json_data, schema=get_agr_jsonschema_dict())
    except jsonschema.exceptions.ValidationError as err:
        print(err.message)
        return False

    return True


# CLI interface
@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option(
    "--input",
    "-i",
    help="the path the file containing json formatted data.",
)
def cli(input: str):
    if is_valid_json(input):
        click.echo("%s: The JSON data is VALID for agr schema." % input)
    else:
        click.echo("%s: The JSON data is ** NOT ** valid for agr schema." % input)
        raise SystemExit("Error in validation.")


if __name__ == "__main__":
    cli()  # CLI interface
