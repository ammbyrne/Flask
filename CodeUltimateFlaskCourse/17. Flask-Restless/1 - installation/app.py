from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_restless import APIManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/Users/antho/Documents/restless/api.db'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)