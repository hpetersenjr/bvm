from flask import Flask , render_template
#from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os , sqlite3

app = Flask(__name__)

@app.route("/") #/home

def home():
    return render_template("index.html")
    #return "pyResponse"

if __name__ == "__main__":
    app.run(debug="true",host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))