import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): Name of the file containing JSON data.

    Returns:
        Object: Python object representing the JSON data.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
