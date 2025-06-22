from flask import Flask,request
app=Flask(__name__) 

@app.route("/")
def home():
    return "Hello user! This is my first flask app"

@app.route("/about")
def about():
    return "This is about us page"

@app.route("/contact") # By default method is GET.
def contact():
    return "This is contact us page"

@app.route("/submit",methods=["GET","POST"]) #GET for getting data ,POST for sending data.
def submit():
    if request.method=="POST":
        return "You are sending data"
    return "You are getting data"
#request is it keeps track of what user sended to server
#response it sends back something to user
#redirect sends user to some other page
#session remember user info across page

if __name__=="__main__":
    app.run(debug=True)