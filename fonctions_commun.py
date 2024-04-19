#!/bin/python
# -*- coding: utf-8 -*-

import json

class JsonUtils:

    def json2Dict(j:str) -> dict:
        d = json.load(j)
        return d

    def json2Dict(d:dict) -> str:
        j = json.dumps(d)
        return j
