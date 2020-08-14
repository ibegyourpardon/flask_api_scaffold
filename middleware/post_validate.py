from flask import request, jsonify
import json
from validator import Required, Not, Truthy, Blank, Range, Equals, In, validate
from collections import OrderedDict


def isstr(param):
    try:
        return isinstance(param, str)
    except:
        return False


def validate_json_type(f):
    # 如果前端未携带json格式的参数
    def wrapper(*args, **kw):
        try:
            json.loads(request.get_data())
        except:
            return jsonify({"errMsg": "payload must be a valid json"}), 500
        return f(*args, **kw)
    return wrapper


def validate_json_scheme(*args, **kwargs):
    # 传入必须传的参数
    lost_params = []
    for name in args:
        try:
            json.loads(request.get_data())[name]
            print(name)
            print("_______")
        except:
            lost_params.append(name)
            print(name + "不存在")
    if len(lost_params) == 0:
        return None
    else:
        return lost_params


