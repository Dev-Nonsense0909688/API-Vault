from flask import Blueprint
from .add_api import add_api_key
from .delete_api import delete_api_key
from .list_api import list_api_key
from .sessions import login, logout

vault_api = Blueprint("vault_api", __name__)

vault_api.add_url_rule("/api/v1/add_key", view_func=add_api_key, methods=["POST"])
vault_api.add_url_rule("/api/v1/delete_key", view_func=delete_api_key, methods=["POST"])
vault_api.add_url_rule("/api/v1/list_keys", view_func=list_api_key, methods=["GET"])
vault_api.add_url_rule("/api/v1/sessions/login", view_func=login, methods=["POST"])
vault_api.add_url_rule("/api/v1/sessions/logout", view_func=logout, methods=["POST"])
