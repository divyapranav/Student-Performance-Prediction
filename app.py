from flask import Flask, render_template, request
import pickle
import numpy as np

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['Hours Studied']),
            float(request.form['Previous Scores']),
            int(request.form['Extracurricular Activities']),
            float(request.form['Sleep Hours']),
            float(request.form['Sample Question Papers Practiced'])
        ]

        final_features = np.array([features])
        prediction = model.predict(final_features)[0]
        prediction = round(prediction, 2)

        return render_template('index.html', prediction=prediction)

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
