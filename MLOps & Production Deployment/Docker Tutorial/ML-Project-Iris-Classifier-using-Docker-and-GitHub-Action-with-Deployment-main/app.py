from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import joblib

app = Flask(__name__)

# load the model
model = joblib.load('models/iris_model.pkl')

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
    app.run(debug=True, host='0.0.0.0', port=5000)