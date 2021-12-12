from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#----------------APP------------------#
app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
#-------------------------------------#

#---------------DATABASE--------------#
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)
#-------------------------------------#


#------------BLUEPRINTS-------------#
from web_app.home.views import home
app.register_blueprint(home)

from web_app.lab.views import lab
app.register_blueprint(lab)

from web_app.logs.views import logs
app.register_blueprint(logs)

from web_app.error_pages.handler import error_pages
app.register_blueprint(error_pages)
#-----------------------------------#