import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  
from sklearn.metrics import mean_squared_error
import pickle

#  ------------load dataset-------------
data = pd.read_csv('data.csv')

# --------features and target variable----------
X = data[['temperature', 'humidity', 'hour']]
y = data['energy_consumption']

# ---------split data----------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------train model------------
model = LinearRegression()  
model.fit(X_train, y_train)

# ----------Evaluate model------------
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print(f'Mean Squared Error: {mse:.2f}')

# ----------for save model------------
with open('energy_model.pkl', 'wb') as file:
    pickle.dump(model, file)

# -----------Graph actual vs predicted-------------
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.xlabel('Actual Energy Consumption')
plt.ylabel('Predicted Energy Consumption')
plt.title('Actual vs Predicted Energy Consumption')
plt.grid(True)
plt.show()
