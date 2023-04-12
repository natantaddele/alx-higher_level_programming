def class_to_json(obj):
    """
    Returns a dictionary description of the object with simple data structure for JSON serialization.

    Args:
        obj (object): The object to be serialized to a JSON-compatible dictionary.

    Returns:
        dict: A dictionary representation of the object.
    """
    if not isinstance(obj, object):
        raise TypeError("obj must be an instance of a class")

    return obj.__dict__
