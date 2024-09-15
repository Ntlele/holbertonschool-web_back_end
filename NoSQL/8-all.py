#!/usr/bin/env python3
"""Function lists all documents of collection
"""
import pymongo


def list_all(mongo_collection):
    """Function lists all documents of collection

    Args:
        mongo_collection (_type_): datbase collection

    Returns:
        _type_: list
    """
    return list(mongo_collection.find())