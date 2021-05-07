from flask import Flask, render_template
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, ValidationError
from wtforms.validators import InputRequired, Email, Length, AnyOf
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone'
bootstrap = Bootstrap(app)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Email(message='I don\'t like your name.')])
    password = PasswordField('password', validators=[InputRequired(), Length(min=5, max=10), AnyOf(['secret', 'password'])])

    def validate_username(form, field):
        if field.data != 'anthony@prettyprinted.com':
            raise ValidationError('You do not have the right username')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    user = User(username='Anthony', password='password')
    print(user.username)
    print(user.password)
    if form.validate_on_submit():
        form.populate_obj(user)
        print(user.username)
        print(user.password)
        return 'Form Successfully Submitted!'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)