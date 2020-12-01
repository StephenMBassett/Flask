from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY']='thisisfirstflaskapp'
from stephen_flask import routes