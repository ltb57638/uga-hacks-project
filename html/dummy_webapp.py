import os
from flask import Flask, request, redirect, url_for, render_template
from  werkzeug.utils import secure_filename
app = Flask(__name__)
from keras.models import load_model
from keras.backend import set_session
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

print("Loading Model")
global sess
sess = tf.Session()
set_session(sess)
global model
model = load_model('MY_CIFAR10_MODEL.H5')
global graph
graph = tf.get_default_graph()

@app.route('/', methods=['GET', 'POST'])
def main_page():
	if request.method == 'POST':
		text  = request.form['words']
		return redirect(url_for('prediction', text=text))
#		FILE = REQUEST.FILES['FILE']
#		FILENAME = SECURE_FILENAME(FILE.FILENAME)
#		FILE.SAVE(OS.PATH.JOIN('UPLOADS', FILENAME))
#		RETURN REDIRECT(URL_FOR('PREDICTION', FILENAME=FILENAME))
	return render_template('index.html')
@app.route('/prediction/<text>')
def prediction(text):
	#MY_IMAGE = PLT.IMREAD(OS.PATH.JOIN('UPLOADS', FILENAME))
	#MY_IMAGE_RE = RESIZE(MY_IMAGE, (32,32,3))
	with graph.as_default():
		set_session(sess)
		probabilities = model.predict(np.array([text]))
		print(probabilities)
		number_to_class = ['yes','no']
		index = np.argsort(probabilities)
		#preditions here i think this would be yes or no
		return render_template('predict.html', predictions=predictions)

app.run(host='0.0.0.0', port=80)
