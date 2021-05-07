from flask import Flask, render_template, request
from flask_babel import Babel, get_locale

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def localeselector():
    #return 'en_US'
    return request.accept_languages.best_match(['en', 'es', 'de'])

@app.route('/')
def index():
    return '<h1>Locale: {}</h1>'.format(get_locale())

if __name__ == '__main__':
    app.run(debug=True)