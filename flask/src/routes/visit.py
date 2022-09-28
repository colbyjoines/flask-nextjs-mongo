from ..instance.app import app, db

import json
from bson import json_util

@app.route('/api/v0/visit')
def visit():
    visits_collection = db["site-visits"]
    visits_collection.insert_one({"visit": True})
    return {"every_visit": json.loads(json_util.dumps(list(visits_collection.find({}))))}