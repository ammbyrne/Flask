from flask import Flask 
from flask_sqlalchemy SQLAlchemy 

app = Flask(__name__)

app.config['SECRET_KEY'] = 'randomstring'
app.config['SQLALCHEMY_DATABASE_URI'] = '/mnt/c/Users/antho/Documents/user/mydb.db'
app.config['CSRF_ENABLED'] = True 
app.config['USER_ENABLE_EMAIL'] = False 

if __name__ ==  '__main__':
    app.run(debug=True)