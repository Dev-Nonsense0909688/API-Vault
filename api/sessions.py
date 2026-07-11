from database import StorageHandler
from core.config import PASSWORD
from core.token import token

from flask import request, jsonify, session

storage = StorageHandler()

def login():
    data = request.json
    try:
        password = data["password"]
        if password == PASSWORD:
            session["token"] = token()
            
            return jsonify({"success": True, "token": token()}), 200
        return jsonify({"success": False, "message": "Invalid parameters"}), 401
    except:
        return jsonify({"success": False, "message": "Invalid parameters"}), 401
    
def logout():
    session.clear()
    return jsonify({"success": True})