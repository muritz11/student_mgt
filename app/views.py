# The views file contains the routes to webpages and might also house logic for your web app.
from app import app


@app.route("/")
def index():
    return "Hello World"
