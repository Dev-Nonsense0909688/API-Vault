from .hashing import hash_key

from cryptography.fernet import Fernet
import socket

f =  Fernet(hash_key(socket.gethostname()))

def encrypt(data: str) -> bytes:
    return f.encrypt(data.encode())

def decrypt(data: bytes) -> str:
    return f.decrypt(data).decode()