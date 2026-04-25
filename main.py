import pandas as pd
from sklearn.linear_model import LinearRegression

# dataset (very small)
data = {
    "hours": [1, 2, 3, 4, 5],
    "score": [20, 40, 50, 70, 90]
}

df = pd.DataFrame(data)

# inputs and outputs
X = df[["hours"]]
y = df["score"]

# model
model = LinearRegression()
model.fit(X, y)

# prediction
predicted = model.predict(pd.DataFrame([[6]], columns=["hours"]))

print("Predicted score for 6 hours:", predicted[0])