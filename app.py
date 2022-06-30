from flask import Flask, request, render_template
import pymongo
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def homepage():
    return render_template('index.html')

@app.route("/register",methods=['GET','POST'])
def register():
    return render_template('registration.html')

@app.route("/fillreg",methods=['POST'])
def fillregform():
    if(request.method=='POST'):
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        client = pymongo.MongoClient(
            "mongodb+srv://maideen:myislam@cluster0.e7blv.mongodb.net/?retryWrites=true&w=majority")
        db = client['Login']
        clus = db['cluster1']
        for i in clus.find():
            if i['email'] == email:
                return render_template('regsuccess.html',result="Email already registered!")
            else:
                clus.insert_one(
                    {
                        'Name': name,
                        'email': email,
                        'password': password
                    }
                )
        return render_template('regsuccess.html',result="Registered Successfully!")

@app.route("/login",methods = ['GET','POST'])
def log():
    return render_template("login.html")

@app.route("/log",methods=['POST'])
def log_in():
    if(request.method=='POST'):
        email = request.form['email']
        password = request.form['password']
        client = pymongo.MongoClient(
            "mongodb+srv://maideen:myislam@cluster0.e7blv.mongodb.net/?retryWrites=true&w=majority")
        db = client['Login']
        clus = db['cluster1']
        for i in clus.find():
            if i['email'] == email and i['password'] == password:
                result = ("Welcome", i['Name'], "!")
                return render_template('loginsuccess.html',result=result)
                break
            elif i['email'] == email and i['password'] != password:
                result = ("Incorrect Paaword")
                return render_template('loginsuccess.html', result=result)
                break
        else:
            result = ("User not registered!")
        return render_template('loginsuccess.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)