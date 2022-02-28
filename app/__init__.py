# this houses the code to initialize our Flask application and to import our views.
# In this file, we import Flask, and also create and app object which is an instance of the Flask class.
from flask import Flask

# this is d app obj
app = Flask(__name__)


from app import views