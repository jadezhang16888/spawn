#!/usr/bin/env python
#coding=utf-8

from flask import Flask

from .helper import helper_tools


app = Flask(__name__)
app.register_blueprint(helper_tools)