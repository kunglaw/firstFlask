from flask import render_template, render_template_string
from models.Square import Square

class SquareController: 

   @staticmethod  
   def index(s=0):

       squareObj = Square(s)
       rangeSquare = squareObj.getRange()

       content = render_template("squareform.html",dt={"rangeSquare":rangeSquare})

       return render_template("index.html",dt={ "content":content, "name":"DIMAS" })

       pass  