#-*- encoding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import random
import threading
import argparse

app = Flask(__name__)
CORS(app, supports_credentials=True)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
