from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app
from flask_admin import Admin

db = SQLAlchemy(app)
migrate = Migrate(app,db, compare_type=True)


admin  = Admin(app, name = 'BankRespublika', template_mode = 'bootstrap3')
