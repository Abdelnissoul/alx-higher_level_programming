#!/usr/bin/python3
"""a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return string representation of a JSON."""
    return json.loads(my_str)
