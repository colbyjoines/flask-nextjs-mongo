from ..instance.app import app

@app.route('/')
def index():
    return "<h1>Index</h1>"