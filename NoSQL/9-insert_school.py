#!/usr/bin/env python3
"""Script contains function that that inserts docs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """Function inserts docs in collection

    Args:
        mongo_collection (_type_): collection insert into

    Returns:
        _type_: id
    """
    obj = mongo_collection.insert_one(kwargs)
    return obj.inserted_id