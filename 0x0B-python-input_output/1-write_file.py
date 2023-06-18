#!/usr/bin/python3
""" This module contains a function that writes to a text file
"""


def write_file(filename="", text=""):
    """ Function that writes to a text file

    params:
        filename: filename
        text: text to write

    raises
        Exception: when the file can't be opened

    writes text to file on success

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
