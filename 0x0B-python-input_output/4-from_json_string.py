#!/usr/bin/python3

""" This module contains a Json_to_object function
"""
import json


def from_json_string(my_str):
    """ returns an object representation of a JSON string
    """
    return json.loads(my_str)
