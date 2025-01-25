# Energy Consumption Predictor

## Description
This project predicts energy consumption based on input parameters such as temperature, humidity, and hour of the day. It utilizes a linear regression machine learning model trained on a dataset of energy usage patterns. The project includes:

- A Python backend powered by Flask for web-based user interaction.
- A machine learning model built using Scikit-learn, with evaluation metrics such as Mean Squared Error (MSE).
- Data visualization with Matplotlib to show actual vs. predicted energy consumption.
- Integration of a web interface (HTML/CSS) to input data and display predictions.

---

## Key Features
- **Machine Learning**: Linear regression model for energy consumption prediction.
- **Interactive Web Application**: Predict energy usage via a user-friendly interface.
- **Visualization**: Graphs to display the relationship between actual and predicted values.
- **Reusable Code**: Model saved with Pickle for easy reloading and prediction.

---

## Technologies Used
- **Frontend**: HTML, CSS
- **Backend**: Python (Flask)
- **Libraries**: Pandas, NumPy, Matplotlib, Scikit-learn
- **Model Persistence**: Pickle

---

## How to Run
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open the app in your browser:
   ```
   http://127.0.0.1:5000
   ```

---

