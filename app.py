from flask import Flask, render_template, request
import random
import socket
import database	

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "index.html",
        home = True, history = False, products = False, add = False, dataFound = False
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)