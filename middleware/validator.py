from flask import redirect
from core.token import token

def validation(session):
    try:
        if session["token"] == token():
            return None
    except KeyError:
        pass
    
    return redirect("/")

def api_validation(session):
    try:
        if session["token"] == token():
            return None
    except KeyError:
        pass
    
    return {"success": True}