from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import joblib
import numpy as np

app = Flask(__name__)

# load the model
model = joblib.load('C:/Users/emon1/OneDrive/Desktop/AI Engineer/Production Deployment/Flask/Deploy Machine Learning Model Flask/iris_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    data = [
            float(request.form['sepal_length']),
            float(request.form['sepal_width']),
            float(request.form['petal_length']),
            float(request.form['petal_width'])
        ]
    prediction = model.predict([data])
    species    = ['setosa','versicolor','virginica']
    result     = species[prediction[0]]
    return render_template('index.html',prediction_text=f'Iris flower is predicted to be {result}')

if __name__ == '__main__':
    app.run(debug=True)
