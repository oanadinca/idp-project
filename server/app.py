from flask import Flask, render_template, request
import random
import socket
import database	
from flask_cors import CORS, cross_origin
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.3')


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=80)