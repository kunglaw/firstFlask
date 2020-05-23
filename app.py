from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from flask import jsonify

from controllers.HomeController import HomeController
from controllers.SquareController import SquareController
from controllers.MahasiswaController import MahasiswaController

application = Flask(__name__)

application.config["MYSQL_USER"] = "root"
application.config["MYSQL_PASSWORD"] = ""
application.config["MYSQL_HOST"] = "localhost"
application.config["MYSQL_DB"] = "demo"
application.config["MYSQL_CURSORRCLASS"] = "DictCursor" 

mysql = MySQL(application)

@application.route("/")
def index():
    return HomeController.index()

@application.route("/mahasiswa")
def mahasiswa():
   return jsonify(MahasiswaController.listMahasiswa(mysql))
   pass
    

@application.route("/hello/<n>/<int:age>")
def hello(n, age):
    return "<h1> Hello {0}, your age is {1}</h1><hr>".format(n,age)

@application.route("/about/<name>")
def about(name=""):
    return render_template("about.html",name=name)

@application.route("/lingkaran/<int:radius>")
def lingkaran(radius=0):

    return HomeController.Lingkaran(radius)


@application.route("/square",methods=["POST","GET"])
def square():
    if(request.method == "GET"):
       
        return SquareController.index()
    else:

        s = int(request.form["side"])
        return SquareController.index(s)

    pass

if __name__ == '__main__':
    application.run(debug=True)