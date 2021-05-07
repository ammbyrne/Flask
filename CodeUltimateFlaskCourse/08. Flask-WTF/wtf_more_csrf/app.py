from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Length, AnyOf, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Mysecret!'
app.config['WTF_CSRF_ENABLED'] = True
app.config['WTF_CSRF_SECRET_KEY'] = 'ADifferentSecret!'
app.config['WTF_CSRF_TIME_LIMIT'] = 3600

class LoginForm(FlaskForm):
    username = StringField('Your Username', validators=[InputRequired('A username is required!'), Length(min=4, max=8, message='Must be between 4 and 8 characters')])
    password = PasswordField('password', validators=[InputRequired('Password is required!'), AnyOf(values=['secret', 'password'])])
    age = IntegerField('age', default=24)
    true = BooleanField('Click here')
    email = StringField('email', validators=[Email()])

class User:
    def __init__(self, username, age, email):
        self.username = username
        self.age = age
        self.email = email 

@app.route('/', methods=['GET', 'POST'])
def index():
    myuser = User('JohnDoe', 58, 'john@doe.com')

    form = LoginForm(obj=myuser)

    if form.validate_on_submit():
        return '<h1>Username: {} Password: {} Age: {} True: {} Email: {}</h1>'.format(form.username.data, form.password.data, form.age.data, form.true.data, form.email.data)

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)