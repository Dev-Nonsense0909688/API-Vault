from database import StorageHandler
from middleware.validator import api_validation

from flask import jsonify,session

storage = StorageHandler()

def list_api_key():
    res = api_validation(session)
    if res: return res
    
    return jsonify(storage.list_keys())