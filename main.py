import os
import re
import json
import sys

import logging

from flask import Flask
from flask import request
from flask import Response
import gunicorn

app = Flask(__name__)
logger = logging.getLogger("gunicorn.glogging.Logger")
logger.propagate = False
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(logging.Formatter("%(asctime)s: BAD REQUEST: %(message)s"))
logger.addHandler(handler)


@app.route('/', methods=['GET'])
def index():
    return "elo"

if __name__ == '__main__':
    app.run(debug=True, port=8000)