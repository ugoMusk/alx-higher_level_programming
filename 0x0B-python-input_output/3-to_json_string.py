#!/usr/bin/python3

""" This module contains a function that returns the JSON representation of an object
"""

import json


def to_json_string(my_obj):
    """ Function that returns the JSON representation of an object

    param(s):
        my_obj: object

    raises:
        Exception: when the object can't be encoded
   returns a json format of the python object 

    """
    return json.dumps(my_obj)
