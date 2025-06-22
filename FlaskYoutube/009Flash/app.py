from flask import Flask, request, url_for, Response, session, redirect, render_template,flash
app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/",methods=["GET", "POST"])
def form():
  if request.method == "POST":
      name=request.form.get("name")
      email=request.form.get("email")
      if not name:
          flash("Name is required!", "error")
      flash(f"Thanks {name},Your feedback has been submitted successfully!", "success")
      return redirect(url_for("thankyou")) #using redirect to avoid form resubmission on refresh,route is thankyou
      #redirect("/thankyou") #this will also work but not recommended.
  return render_template("form.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")
if __name__ == "__main__":
    app.run(debug=True)