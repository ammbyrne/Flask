from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_security import Security, SQLAlchemyUserDataStore

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'

db = SQLAlchemy(app)

user_datastore = SQLAlchemyUserDataStore(db)
security = Security(app, user_datastore)

if __name__ == '__main__':
    app.run(debug=True)