from .hashing import hash_key
from .utils import get_cpu_uuid

from cryptography.fernet import Fernet


f = Fernet(hash_key(get_cpu_uuid()))

def encrypt(data: str) -> bytes:
    return f.encrypt(data.encode())

def decrypt(data: bytes) -> str:
    return f.decrypt(data).decode()
