from api import vault_api
from middleware.validator import validation
from core.config import SECRET_KEY

from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.register_blueprint(vault_api)

@app.route("/dashboard")
def dashboard():
    res = validation(session) # validate user session token
    if res: return res
    
    return render_template("index.html")
    
@app.route("/")
def root():
    return render_template("login.html")

if __name__ == "__main__":
    app.run("0.0.0.0", 5608, debug=True)