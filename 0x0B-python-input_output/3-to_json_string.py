#!/usr/bin/python3
"""A string to-JSON_string function."""
import json


def to_json_string(my_obj):
    """Returns the JSON representative of a str object."""
    return json.dumps(my_obj)
