import datetime
import os

from bson import ObjectId
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.results import InsertOneResult

# Set the documents to expire after a set amount of time
TTL_SECONDS = 6 * 60 * 60

# Fields used in the database
CREATED_AT_FIELD = "createdAt"
TEXT_FIELD = "text"
ID_FIELD = "_id"


class ApplicationDao:
    def __init__(self, database: Database = None):
        # If no database provided, connect to one
        if database is None:
            username = os.environ.get("MONGO_USER")
            password = os.environ.get("MONGO_PASSWORD")
            host = os.environ.get("MONGO_HOST")
            self.client = MongoClient(f"mongodb+srv://{username}:{password}@{host}/test?retryWrites=true&w=majority")

            database: Database = self.client.test

        # Set up database and collection variables
        self.database = database
        self.test_collection: Collection = database.test_collection

        # Set a TTL on the test collection
        self.test_collection.create_index(CREATED_AT_FIELD, expireAfterSeconds=TTL_SECONDS)

        print(f"Database collections: {self.database.list_collection_names()}")

    def insert_document(self, text: str) -> InsertOneResult:
        return self.test_collection.insert_one({CREATED_AT_FIELD: datetime.datetime.utcnow(), TEXT_FIELD: text})

    def get_documents(self):
        return self.test_collection.find()

    def get_document(self, document_id) -> dict:
        return self.test_collection.find_one({ID_FIELD: ObjectId(document_id)})

    def delete_document(self, document_id):
        return self.test_collection.delete_one({ID_FIELD: ObjectId(document_id)})

    def delete_documents(self):
        return self.test_collection.delete_many({})
