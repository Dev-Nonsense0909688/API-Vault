from database import StorageHandler
from core.crypto import encrypt
from middleware.validator import api_validation

from flask import request, jsonify,session

storage = StorageHandler()

def add_api_key():
    res = api_validation(session, request.headers)
    if res: return res

    data : dict = request.json

    try:
        raw_key = data["api_key"]
        key = encrypt(raw_key)

        storage.add_key(key=key, name=data["name"], website=data.get("website"))
        return jsonify({"success": True}), 200
    except:
        return jsonify({"success": False, "message": "Invalid parameters"}), 401
