#!/usr/bin/env python3.6
# -*- Coding: utf-8 -*-

from flask import Flask
from flask import Response, request
import json

from controller.log import ApiLogController

app = Flask(__name__)

@app.route('/')
def static_index():
    with open("./static/index.htm") as fh:
        body = fh.read()

    return Response(response=body, mimetype="text/html;charset=utf-8")

@app.route('/js/main.js')
def static_js_main_js():
    with open("./static/js/main.js") as fh:
        body = fh.read()

    return Response(response=body, mimetype="application/javascript;charset=utf-8")

@app.route('/css/style.css')
def static_css_style_css():
    with open("./static/css/style.css") as fh:
        body = fh.read()

    return Response(response=body, mimetype="text/css;charset=utf-8")

@app.route('/api/log/<limit>/<repository>')
def api_log(limit, repository):
    c = ApiLogController(limit=limit, repository=repository)
    return c.main()


def _exec_command(command):
    result = subprocess.run(command, shell=True, timeout=30, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    return result.stdout.splitlines()


if __name__ == '__main__':
    app.run(debug=True)