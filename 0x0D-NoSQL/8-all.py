# /bin/usr/python3
"""
List all documents in Python
"""


def list_all(mongo_collection):
    """
    function that lists all documents in a collection
    """
    if not mongo_collection:
        return []
    return mongo_collection.find()
