# contains the example script for login into the api_vault.
# TODO: add example for adding, deleting, listing api keys. # DONE


import requests

token = ""

def login():
    global token
    
    res : dict = requests.post("http://127.0.0.1:5608/api/v1/sessions/login", json={"password":"nonsense"}).json() # request the server for login token.
    
    if res.get("success"): # if response from server successful it will send in json {"success": true}
        token = res.get("token") # then we get and save the token.

def add_api_key():
    res: dict = requests.post(
        "http://127.0.0.1:5608/api/v1/add_key", headers={"token": token},
        json={
            'api_key': '......',
            'name': 'OpenAI-key'
        }
    ).json()
    
    print(res)

def delete_api_key():
    res: dict = requests.post(
                "http://127.0.0.1:5608/api/v1/delete_key", headers={"token": token},
        json={
            'name': 'OpenAI-key'
        }
    ).json()

    print(res)


def list_api_keys():

    res: dict = requests.get("http://127.0.0.1:5608/api/v1/list_keys", headers={"token": token}).json()
    
    print(res)

login() # getting access token and saving it in var `token`
print(token) # printing access token

add_api_key() # adding api-key called `OpenAI-key`
list_api_keys() # the key we added should show up.
delete_api_key() # deleting the key added.
list_api_keys() # again listing keys we have.