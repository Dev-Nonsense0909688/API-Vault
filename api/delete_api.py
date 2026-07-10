from database import StorageHandler
from middleware.validator import api_validation

from flask import request, jsonify, session

storage = StorageHandler()

def delete_api_key():
    res = api_validation(session)
    if res: return res

    data: dict = request.json
    
    try:
        name = data["name"]
    except:
        return jsonify({"succes": False, "message": "Invalid parameters"}), 400
    
    data = storage.delete_key(name)
    
    return jsonify({"success": True}), 200