#!/usr/bin/python3

def class_to_json(obj):
    """Converts a class instance to a JSON serializable dictionary"""
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (int, str, bool)):
            json_dict[key] = value
        elif isinstance(value, list):
            json_dict[key] = value
        elif isinstance(value, dict):
            json_dict[key] = value
    return json_dict
