from flask import Flask, request, url_for, Response, session, redirect, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("feedback.html")

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("username") #will return None if not found ,request.form["username"] will throw error if not found
        message = request.form.get("message")
        
        return render_template("thankyou.html", name=name, message=message)
        
if __name__ == "__main__":
    app.run(debug=True)