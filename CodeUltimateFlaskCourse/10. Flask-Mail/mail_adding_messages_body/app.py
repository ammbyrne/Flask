from flask import Flask 
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.yourserver.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
#app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'anthony@prettyprinted.com'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_DEFAULT_SENDER'] = 'anthony@prettyprinted.com'
app.config['MAIL_MAX_EMAILS'] = None
#app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

#mail = Mail()
#mail.init_app(app)

@app.route('/')
def index():
    msg = Message('Hey There', recipients=['patoxediwo@bestvpn.top'])
    #msg.body = 'Here is the body!'
    msg.html = '<b>This is a test email sent from Anthony\'s app. You don\'t have to reply.</b>'
    mail.send(msg)

    return 'Message has been sent!'

if __name__ == '__main__':
    app.run()