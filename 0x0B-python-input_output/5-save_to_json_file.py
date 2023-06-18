#!/usr/bin/python3
"""This module contains  a function that converts and writes a python object to a file in JSON format"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
