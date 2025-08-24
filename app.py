import os
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('heart_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb')) if os.path.exists('scaler.pkl') else None
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form inputs (match the 13 features from the dataset)
    features = [float(request.form['age']), float(request.form['sex']), float(request.form['cp']),
                float(request.form['trestbps']), float(request.form['chol']), float(request.form['fbs']),
                float(request.form['restecg']), float(request.form['thalach']), float(request.form['exang']),
                float(request.form['oldpeak']), float(request.form['slope']), float(request.form['ca']),
                float(request.form['thal'])]
    features = np.array([features])
    if scaler:
        features = scaler.transform(features)
    prediction = model.predict(features)[0]
    result = "Heart Disease Likely" if prediction == 1 else "No Heart Disease"
    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)