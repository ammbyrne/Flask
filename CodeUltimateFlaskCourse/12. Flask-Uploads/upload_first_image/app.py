from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'pictures'

configure_uploads(app, photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'thefile' in request.files:
        image_filename = photos.save(request.files['thefile'])
        #return '<h1>'+photos.path(image_filename)+'</h1>'
        return '<h1>'+photos.url(image_filename)+'</h1>'
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)