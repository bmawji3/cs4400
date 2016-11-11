from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config.update(
    WTF_CSRF_ENABLED = True,
    DEBUG=True,
    SECRET_KEY='c11a678785091b7f1334c24a4123ee75'
)
app.config['MYSQL_DATABASE_USER'] = 'cs4400_Team_75'
app.config['MYSQL_DATABASE_PASSWORD'] = 'vJQAUUNg'
app.config['MYSQL_DATABASE_DB'] = 'cs4400_Team_75'
app.config['MYSQL_DATABASE_HOST'] = 'academic-mysql.cc.gatech.edu'
mysql.init_app(app)

from app.general import views
