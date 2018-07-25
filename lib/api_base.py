#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from flask import request, Response
import traceback
import json

class ApiException(Exception):
    def __init__(self, response):
        self._response = response

    def get_response(self):
        return self._response

class ApiBase(object):
    def __init__(self, **params):
        self._params = params

    def main(self):
        try:
            self.controller()
        except ApiException as e:
            resp = e.get_response()
        # except Exception:
        #     return Response(response="<h1>Internal Server Error</h1><hr><p>Git Notification</p>", mimetype="text/html", status=500)

        return resp

    def get_params(self, key):
        return self._params[key]

    def get_request_header(self, key):
        return request.headers.get(key)

    def send_redirect(self, url):
        return redirect(url)

    def send_response(self, body, mimetype='application/json;charset=utf-8', status_cd=200):
        raise ApiException(Response(response=body, mimetype=mimetype, status=status_cd))

    def send_response_json(self, json_obj):
        body = json.dumps(json_obj, ensure_ascii=False, indent=4, separators=(',', ': '))
        self.send_response(body)
