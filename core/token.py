from .hashing import hash_token
import time
import socket

def token():
    hostname = socket.gethostname()
    full_token = hostname + "(:)" +time.strftime("%Y-%m-%d")
    return hash_token(full_token)
