from flask import Flask, request, url_for, Response, session, redirect, render_template
app = Flask(__name__)

@app.route("/")
def student():
    return render_template(
        "profile.html",
        name="Prashant",
        is_Topper=True,
        subjects=["Math", "Science", "English"],
    )
if __name__ == "__main__":
    app.run(debug=True)