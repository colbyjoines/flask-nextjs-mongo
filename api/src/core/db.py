from pymongo import MongoClient
from flask import Flask

class DbConnection:
    mongo_params = {
        "url": "MONGO_DB_URL",
        "db_name": "MONGO_DB_NAME"
    }
    def __init__(self, app: Flask) -> None:
        self.client = MongoClient(app.config[self.mongo_params["url"]])
        self.db = self.client[app.config[self.mongo_params["db_name"]]]
        
    def get_connection(self):
        return self.db