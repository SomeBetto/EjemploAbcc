from flask import Flask

# Routes
from src.v1.routers import util

app = Flask(__name__)


def page_not_found(error):
    return "NOT FOUND PAGE ",404


# Blueprints
app.register_blueprint(util.util,url_prefix='/v1/util/')

# Error Heandlers
app.register_error_handler(404,page_not_found)

if __name__ == "__main__":
    app.run()