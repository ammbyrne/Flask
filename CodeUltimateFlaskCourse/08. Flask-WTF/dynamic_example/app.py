from flask import Flask, render_template, request
from flask_wtf import FlaskForm 
from wtforms import SelectField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class MyForm(FlaskForm):
    language = SelectField(u'Programming Language', choices=[('rb', 'Ruby'), ('py', 'Python')])
    framework = SelectField('Framework', choices=[])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()

    form.framework.choices = query('rb') #init the dropdown with the first value

    if request.method == 'POST':
        #this is to enable Flask-WTFs verification
        #it uses the language value passed in to determine the value
        #framework choices
        form.framework.choices = query(form.language.data)

    if form.validate_on_submit():
        return '<h1>Language: {} Framework: {}</h1>'.format(form.language.data, form.framework.data)

    return render_template('index.html', form=form)

@app.route('/getframework/<lang>')
def getframework(lang):
    form = MyForm()
    form.framework.choices = query(lang)
    #return only the select html
    return str(form.framework)

def query(lang):
    if lang == 'rb':
        return [('sina', 'Sinatra'), ('rails', 'Rails')]
    if lang == 'py':
        return [('flask', 'Flask'), ('django', 'Django')]

if __name__ == '__main__':
    app.run(debug=True)