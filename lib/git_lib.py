#!/usr/bin/env python3.6
# -*- Coding: utf-8 -*-
import os
import subprocess

class Git(object):
    def __init__(self, base_path, repository):
        self._repository = repository
        self._path = os.path.join(base_path, repository)

    def fetch(self):
        command = "git fetch --progress origin"
        self.exec_git_command(command)

    def pull(self):
        command = "git pull"
        return self.exec_git_command(command)


    def push(self):
        pass


    def log(self, limit=0):
        arg_limit = ''
        if not limit:
            arg_limit = f'-{limit}'
        command = r'git --no-pager log --date=iso --pretty=format:"%H,%an,%ad,%s" ' + arg_limit

        return self.exec_git_command(command)


    def exec_git_command(self, command):
        return self._exec_command(self._create_command(command))

    def _create_command(self, command):
        if os.name == 'posix':
            delimiter = ';'
        elif os.name == 'nt':
            delimiter = '&'
        else:
            raise RuntimeError("Un supported Operating System")

        return f"cd {self._path}{delimiter}{command}"

    def _exec_command(self, command):
        result = subprocess.run(command, shell=True, timeout=30, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # print("---- STDOUT ----")
        # print(result.stdout)

        # print("---- STDERR ----")
        # print(result.stderr)

        # print("---- EOF ----")

        return result.stdout.splitlines()
