from flask import Flask 
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/Users/antho/Documents/login_example/login.db'

login_manager = LoginManager(app)
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login')
def login():
    user = User.query.filter_by(username='Anthony').first()
    login_user(user)
    return '<h1>Logged in!</h1>'

@app.route('/home')
@login_required
def home():
    return '<h1>You are in the protected area, {}!</h1>'.format(current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return '<h1>You are now logged out!</h1>'

if __name__ == '__main__':
    app.run(debug=True)