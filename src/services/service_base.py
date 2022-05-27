from json import detect_encoding
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

class ServiceBase():
    def __init__(self):
        self.db = TinyDB(storage=MemoryStorage)

    def get(self):
        return self.db.all()

    def insert(self, bodyRequest):
        self.db.insert(bodyRequest)

    def update(self, bodyRequest, query: Query):
        self.db.update(bodyRequest, query)

    def remove(self, query: Query):
        self.db.remove(query)
