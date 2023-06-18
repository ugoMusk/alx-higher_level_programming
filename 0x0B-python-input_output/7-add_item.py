#!/usr/bin/python3
"""Add all cl arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = [] # set items to an empty array to avoid error that could break the program
        
    # extend items with all command line args 
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
