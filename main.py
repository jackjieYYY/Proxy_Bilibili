# -*- coding: utf-8 -*-
from contextlib import closing
import requests
from flask import Flask, request, Response,abort
from urllib.parse import urlparse
app = Flask(__name__)


@app.before_request
def proxy():
    #if not filter(request):
    #    return abort(403)
    headers = {h[0]: h[1] for h in request.headers}
    url=request.url.replace(request.host+'/', '', 1)
    print(url)
    # 一些自己的逻辑...

    return requests.request(request.method,url, data=request.json, headers=headers).content


def filter(request):
    if( 'bilibili.com/bangumi/play/' in request.url):
        return True
    else:
        return False


app.run(
    host = '0.0.0.0',
    port = 7777,  
    debug = True 
    )