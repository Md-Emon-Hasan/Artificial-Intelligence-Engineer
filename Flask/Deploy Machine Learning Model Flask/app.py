import numpy as np
from flask  import Flask
from flask import request
from flask import jsonify
from flask import render_template
import pickle

# create flask app
flask_app = Flask(__name__)

model = pickle.load(open('C:/Users/emon1/OneDrive/Desktop/AI Engineer/Flask/Deploy Machine Learning Model Flask/model.pkl','rb'))

@flask_app.route('/')
def home():
    return render_template('index.html')

@flask_app.route('/predict',methods=['post'])
def predict():
    flaot_features = [float(x) for x in request.form.values()]
    features = [np.array(flaot_features)]
    prediction = model.predict(features)
    return render_template('index.html',prediction_text = 'The flower species is {}'.format(prediction))

if __name__=='__main__':
    flask_app.run(debug=True)
