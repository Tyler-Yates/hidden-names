from bson import ObjectId
from flask import json
from flask.json import JSONEncoder


class CustomJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)
