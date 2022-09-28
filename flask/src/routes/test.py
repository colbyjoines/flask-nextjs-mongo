from ..instance.app import app

@app.route('/api/v0/')
def test():
    return {}