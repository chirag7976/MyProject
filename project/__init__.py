import warnings
from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)

app.secret_key = 'y2JgkQeO9OWyWUpIOXBHnDOvU6YYO6qR'

app.config['TESTING'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_ECHO'] = True

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

app.config['SQLALCHEMY_RECORD_QUERIES'] = True

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hello:hellohello@192.168.43.109:3306/pythondb'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rootroot@rdspython.cmiy6lo9qske.us-east-1.rds.amazonaws.com:3306/pythondb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/newdatabase'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://codejxxz_FYUSER:IVD2hsaM-3wn@103.195.185.77:3306/codejxxz_FYProject'


app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

db = SQLAlchemy(app)

import project.com.controller
