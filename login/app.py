from flask import Flask,render_template,request,session,flash
import mlab
from user import User

app = Flask(__name__)
app.config["SECRET_KEY"] = "abcd1234"
mlab.connect()

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method =="GET":
        return render_template("login.html")
    elif request.method=="POST":
        form = request.form
        u=form["username"]
        p=form["password"]
        users=User.objects(username=u).first()
        if users != None:

            if users.password == p :
                return "hello"
            else :
                flash("invalid password")
                return render_template("login.html")
        else :
            flash("username not found")
            return render_template("login.html")

if __name__ == '__main__':
  app.run(debug=True)