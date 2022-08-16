from flask import Flask, request,render_template
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Gun1234@127.0.0.1:3306/my_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "my_project"

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

from extensions import *
from model import *
from controllers import *




if __name__ == "__main__":
    
    app.run(port=5000,debug=True)
