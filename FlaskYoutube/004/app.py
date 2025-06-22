from flask import Flask, request, url_for, Response, session, redirect, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/form")
def f():
    return render_template("form.html")

@app.route("/submit", methods=["POST"]) #here action name of the form is submit
def submit():
    # 1-Name 2-POST 3-make sure action match
    name = request.form.get("name")
    email = request.form.get("email")
    if request.method == "POST":
        if name and email:
            return render_template("success.html", name=name, email=email)
        else:
            return Response("Please fill out all fields.", mimetype="text/plain")
        
if __name__ == "__main__":
    app.run(debug=True)