#!/usr/bin/env python3.6
# -*- Coding: utf-8 -*-
from lib.api_base import ApiBase
from lib.git_lib import Git

class ApiLogController(ApiBase):
    def controller(self):
        limit = self.get_params('limit')
        repository = self.get_params('repository')

        git = Git(r"/git", repository)
        logs = git.log(limit)

        splited_first_log = logs[0].split(',')

        body = {
            "repository": repository
            , "logs": []
            , "hash": splited_first_log[0]
            , "author": splited_first_log[1]
            , "authored_date": splited_first_log[2]
            , "message": splited_first_log[3]
        }

        for log in logs:
            splited_log = log.split(',')
            body['logs'].append({
                "hash":           splited_log[0]
                , "author":         splited_log[1]
                , "authored_date":  splited_log[2]
                , "message":        splited_log[3]
            })

        self.send_response_json(body)