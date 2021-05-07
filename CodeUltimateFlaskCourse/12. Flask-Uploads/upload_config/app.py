from flask import Flask 
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = '/pictures'

configure_uploads(app, photos)

if __name__ == '__main__':
    app.run(debug=True)