#!/usr/bin/python3

def save_to_json_file(my_obj, filename, json=None):
    """
    Writes an object to a text file, using a JSON representation.

    Args:
        my_obj (object): Object to be serialized to JSON.
        filename (str): Name of the file to save the JSON representation.

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
