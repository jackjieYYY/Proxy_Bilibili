# -*- coding: utf-8 -*-
from contextlib import closing
import requests
from flask import Flask, request, Response,redirect
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
    headers["Host"]="www.bilibili.com"
    r = requests.request(method=method,url=path, headers=headers, data=data)
    return redirect(path,Response=r)
    return r.content


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=7777)