#!/usr/bin/python3
""" This modules contains a function that writes an Object to a text file in JSON format
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an object to a text file by a JSON representation

    params:
        my_obj: object
        filename: textfile name

    raise:
    Exception: incase file can not be opened
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
