import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import pickle

X = np.array([
    [10, 0], [10, 1], [10, 2],
    [20, 0], [20, 1], [20, 2],
    [30, 0], [30, 1], [30, 2]
])

y = np.array([300, 800, 1200, 600, 1500, 2200, 900, 2100, 3000])

model = LinearRegression()
model.fit(X, y)

pred = model.predict(X)
error = mean_absolute_error(y, pred)

print("Linear Regression Error:", error)

with open("model_lr.pkl", "wb") as f:
    pickle.dump(model, f)