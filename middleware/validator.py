from flask import redirect, jsonify
from core.token import token

# validating the dashboard (web broswer only)
def validation(session):
    try:
        if session["token"] == token():
            return None
    except KeyError:
        pass

    return redirect("/")

# including session and headers to ensure smooth running for both the web browser and normal REST API.
def api_validation(session,headers: dict):
    
    try:
        if headers.get("Token") == token():
            return None
        if session["token"] == token():
            return None
    except KeyError:
        pass

    return jsonify({"success": False, "message": "Token expired/unknown"})
