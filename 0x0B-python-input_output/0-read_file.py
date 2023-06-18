#!/usr/bin/python3
""" This module  contains a function that reads from a file """


def read_file(filename=""):
    """ Function that reads from a file

    params:
        filename: filename

    raises:
        Exception: when the file can be opened

    prints the read data on success

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
