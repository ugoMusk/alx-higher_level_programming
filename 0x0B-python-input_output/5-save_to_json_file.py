#!/usr/bin/python3
""" This modules contains a function that writes an Object to a text file in JSON format
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes a python object to a text file using JSON format
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
