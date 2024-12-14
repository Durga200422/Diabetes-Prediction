from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = pickle.load(open('diabetics_prediction_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect input data from the form
    int_features = [float(x) for x in request.form.values()]
    final_features = np.array(int_features).reshape(1, -1)
    scaled_features = scaler.transform(final_features)

    # Make prediction
    prediction = model.predict(scaled_features)
    result = "Diabetic" if prediction[0] == 1 else "Non-Diabetic"

    return render_template('index.html', prediction_text=f'Prediction: {result}')

if __name__ == '__main__':
    app.run(debug=True)