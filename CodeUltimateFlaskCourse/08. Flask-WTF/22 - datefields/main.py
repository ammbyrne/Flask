from flask import Flask, render_template
from flask_wtf import FlaskForm 
#from wtforms import DateField
from wtforms.fields.html5 import DateField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone'

class LoginForm(FlaskForm):
	entrydate = DateField('entrydate', format='%Y-%m-%d')

@app.route('/', methods=['GET', 'POST'])
def index():
	form = LoginForm()
	if form.validate():
		return 'Date: {}'.format(form.entrydate.data)
	return render_template('index.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)