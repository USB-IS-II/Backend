from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask("api")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello, World!</p>"
