# -*- coding: utf-8 -*-
from contextlib import closing
import requests
from flask import Flask, request, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')

@app.route("/path/<path:path>")
def before_request(path):

    method = request.method
    data = request.data or request.form or None
    headers = dict()
    for name, value in request.headers:
        if name == 'Host':
            continue
        headers[name] = value
    r = requests.request(method=method,url=path, headers=headers, data=data)
    return r.content


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=7777)