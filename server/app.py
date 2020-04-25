from flask import Flask, render_template, request
import random
import socket
import database	
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=80)