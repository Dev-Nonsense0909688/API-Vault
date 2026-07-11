# contains the example script for login into the api_vault.
# TODO: add example for adding, deleting, listing api keys.


import requests

token = ""

def login():
    global token
    
    res : dict = requests.post("http://127.0.0.1:5608/api/v1/sessions/login", json={"password":"nonsense"}).json() # request the server for login token.
    
    if res.get("success"): # if response from server successful it will send in json {"success": true}
        token = res.get("token") # then we get and save the token.

def add_api_key():

    res: dict = requests.get("http://127.0.0.1:5608/api/v1/list_keys", headers={"token": token}).json()
    
    print(res)
login()
print(token)
add_api_key()