#!/usr/bin/env python3
"""
Change school topics
"""


def schools_by_topic(mongo_collection, topic):
    '''
    Prototype: def schools_by_topic(mongo_collection, topic):
    mongo_collection will be the pymongo collection object
    topic (string) will be topic searched
    '''
    return [collection for collection in mongo_collection.find(
        {"topics": topic}
        )]