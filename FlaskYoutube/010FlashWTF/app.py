from flask import Flask, request, url_for, Response, session, redirect, render_template,flash
from form import RegistrationForm
app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/",methods=["GET", "POST"])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        flash(f"Thanks {name}, Your registration has been submitted successfully!", "success")
        return redirect(url_for("success"))
    return render_template("register.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)