from flask import render_template,Blueprint

home=Blueprint('home',__name__)

@home.route('/',methods=["GET","POST"])
def index():
    return render_template('index.html')