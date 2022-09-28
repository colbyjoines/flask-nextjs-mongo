from src.instance.app import app
from src.routes.index import index
from src.routes.test import test
from src.routes.visit import visit


if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
