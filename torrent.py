from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import os
import libtorrent as lt
import time
import sys

app = Flask(__name__, template_folder = 'templates/')
app.config['UPLOAD_FOLDER'] = '/home/arvind/bot/'
app.config['ALLOWED_EXTENSIONS'] = set(['torrent'])


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
	return render_template('single.html')

@app.route('/upload', methods = ['POST'])
def upload():
	print request.form['down']
	

	if request.form['down'] == 'Upload':
		file = request.files['file']
		print file.filename
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			global path
			path = os.path.join(app.config['UPLOAD_FOLDER'],filename)

			return redirect('/')

	elif request.form['down'] == 'Download':
		return redirect(url_for('download', paths = path))



@app.route('/downloads', methods = ['GET'])
def download(path):
    paths = request.args.get('paths')
    os.system("python /home/arvind/extra.py %s"%paths)
    return "hello"
	

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port= 5000,
        debug=True
    )
