import pandas as pd
import os
from sklearn.linear_model import LinearRegression

# 1. Get correct file path (prevents FileNotFoundError)
file_path = os.path.join(os.path.dirname(__file__), "data", "dataset.csv")

# 2. Load dataset
df = pd.read_csv(file_path)

# 3. Split data
X = df[["hours"]]
y = df["score"]

# 4. Create model
model = LinearRegression()

# 5. Train model
model.fit(X, y)

# 6. Get user input
try:
    hours = float(input("Enter study hours: "))

    # 7. Predict
    prediction = model.predict([[hours]])

    # 8. Output result
    print("Predicted score:", round(prediction[0], 2))

except ValueError:
    print("Please enter a valid number for study hours.")