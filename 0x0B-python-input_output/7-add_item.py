#!/usr/bin/python3
import sys
from os import path
from typing import List
from json import load, dump
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_item(args: List[str], filename: str):
    if path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []
    items.extend(args[1:])
    save_to_json_file(items, filename)


if __name__ == '__main__':
    add_item(sys.argv, 'add_item.json')
