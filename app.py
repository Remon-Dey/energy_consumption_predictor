from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('energy_model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user input
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        hour = int(request.form['hour'])
        
        # Prepare data for prediction
        data = np.array([[temperature, humidity, hour]])
        prediction = model.predict(data)[0]
        
        return render_template('index.html', 
                            prediction=f'Predicted Energy Consumption: {prediction:.2f} kWh')

if __name__ == '__main__':
    app.run(debug=True)
