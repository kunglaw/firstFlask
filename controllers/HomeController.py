from models.Lingkaran import Lingkaran
from flask import render_template

class HomeController: 

    def __init__(self):
        pass
    
    @staticmethod
    def index():

        content = "<h3>Suka suka gua bgsd</h3>"

        return render_template("index.html",dt={"name":"Aries Dimas Yudhistira","content":content}) 

    @staticmethod
    def Lingkaran(radius):

        dt = Lingkaran(radius)

        content = render_template("lingkaran.html",dt=dt)
        # return content
        
        return render_template("index.html",dt={"name":"Aries Dimas","content":content}) # object literal harus ada kutip key nya 