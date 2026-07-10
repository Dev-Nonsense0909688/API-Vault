import sqlite3
from .models import *
from core.crypto import decrypt
from core.config import DB_NAME

def connection():
    return sqlite3.connect(DB_NAME)

class StorageHandler:
    def __init__(self):
        with connection() as conn:
            conn.execute(CREATE_TABLE)
          
    def add_key(self, name: str, website: str, key: bytes, is_dead: bool = False):
        if not self.key_exists(name):
            with connection() as conn:
                conn.execute(INSERT_INTO_TABLE, (name, website, key.decode(), is_dead,))
            
            return True
        else:
            return False
            
    def delete_key(self, name: str):
        try:
            with connection() as conn:
                conn.execute(DEL_FROM_TABLE, (name,))
        except:
            pass
        
    def get_key(self, name: str):
        try:
            with connection() as conn:
                cur = conn.execute(GET_DATA, (name,))
                data = cur.fetchone()
                return {"api_key":data[3], "is_dead": bool(data[4])} 
        except:
            return None
    
    def key_exists(self, name: str):
        with connection() as conn:
            cur = conn.execute(KEY_EXISTS,(name,))
            return bool(cur.fetchone()[0])
        
    def list_keys(self):
        try:
            with connection() as conn:
                cur = conn.execute(LIST_KEYS)
                return [{"api_key": decrypt(r[3].encode()), "is_dead": r[4], "website": r[2], "name": r[1], "id": r[0]} for r in cur.fetchall()]   
        except:
            []