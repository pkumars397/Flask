from flask import Flask, request, url_for, Response, session, redirect, render_template
app = Flask(__name__)
app.secret_key="supersecret"

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login",methods=["POST"]) #here action name of the form is submit
def submit():
    username = request.form.get("username")
    password = request.form.get("password")
    
    # if username == "prashant" and password == "123":
    #     session["user"] = username
    #     return render_template("welcome.html", user=username)   
    # else:
    #     return Response("Invalid credentials. Try again", mimetype="text/plain")
    
    #for multiple users
    users = {
        "prashant": "123",
        "john": "456",
        "alice": "789"
    }
    if username in users and users[username] == password:
        session["user"] = username
        print(str(session))
        return render_template("welcome.html", user=username)
    else:
        return Response("Invalid credentials. Try again", mimetype="text/plain")
    
if __name__ == "__main__":
    app.run(debug=True)