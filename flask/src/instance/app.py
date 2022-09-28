from ..core.db import DbConnection
from .config import config

from datetime import datetime
import json

from flask import Flask
from bson import json_util

app = Flask(__name__)
mongo_password = config["mongodb_key"]
app.config["MONGO_DB_URL"] = f"mongodb+srv://mongdb:{mongo_password}@cluster0.7a9ym7j.mongodb.net/?retryWrites=true&w=majority"
app.config["MONGO_DB_NAME"] = "automation-webapp"
app.db = DbConnection(app).get_connection()
db = app.db


@app.route('/')
def index():
    return {}

@app.route('/api/v0/')
def get_current_time():
    return {'test': "test"}

@app.route('/api/v0/add')
def add_entry():
    visits_collection = db["site-visits"]
    visits_collection.insert_one({"visit": True})
    return {"every_visit": json.loads(json_util.dumps(list(visits_collection.find({}))))}