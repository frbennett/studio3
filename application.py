import os
from flask import Flask, request, redirect, url_for,send_from_directory
from werkzeug.utils import secure_filename
'''
A simple file uploading example 
'''
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['uploads'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['uploads'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
 <!doctype html>
 <title>Upload new File</title>
 <h1>Upload new File</h1>
 <form action="" method=post enctype=multipart/form-data>
 <p><input type=file name=file>
 <input type=submit value=Upload>
 </form>
 '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['uploads'],
                               filename)


if __name__ == '__main__':
    app.run(debug=True)
