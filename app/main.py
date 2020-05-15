from flask import Flask , render_template , request , json
import os , pymongo

app = Flask(__name__)

@app.route('/login/' , methods = ['POST'])

def login():
    
    appUser =  request.form['username'];
    appPassword = request.form['password'];
    
    with open('ip.txt', 'r') as file:
        hostIPAddress = file.read().replace('\n', '')

    client = pymongo.MongoClient("mongodb://" + hostIPAddress + "/")
    db = client.testDB
    loginQuery = { 'username': appUser , 'password': appPassword }
    
    if db.authTable.count_documents( loginQuery ) != 0:
        return json.dumps([{'status':'Authentication_Success'}])
    else:
        return json.dumps([{'status':'Authentication_Failed'}])

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug="true",host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))