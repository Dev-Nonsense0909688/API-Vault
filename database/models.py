CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS api_keys(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    website TEXT NOT NULL,
    key TEXT NOT NULL,
    is_dead BOOLEAN DEFAULT FALSE
    );"""
                
INSERT_INTO_TABLE = """
INSERT INTO api_keys (name, website, key, is_dead) 
    VALUES (?, ?, ?, ?);"""
    
DEL_FROM_TABLE = "DELETE FROM api_keys WHERE name=?"

GET_DATA = "SELECT * FROM api_keys WHERE name=?"

KEY_EXISTS = "SELECT EXISTS(SELECT 1 FROM api_keys WHERE name = ?)"

LIST_KEYS = "SELECT * FROM api_keys"