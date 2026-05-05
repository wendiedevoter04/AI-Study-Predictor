AI Study Predictor

A machine learning project built with Python that predicts a student’s exam score based on study hours. It uses a Linear Regression model trained on a small dataset to learn the relationship between time spent studying and expected performance.

This project was created to build foundational understanding of how machine learning systems are structured, trained and used for prediction.

What this project does

The system takes study hours as input and returns a predicted exam score. It is trained on historical data of study time versus scores, allowing it to learn a simple linear relationship between the two variables.

The workflow is straightforward: data input, model training and prediction output.

Tech stack

Python
Pandas
Scikit-learn
Linear Regression model

How it works

The dataset contains pairs of study hours and exam scores. The model learns a mathematical relationship between these two values using linear regression.

Once trained, it can take new study hours as input and estimate the expected score based on patterns it learned during training.

It is a basic supervised learning pipeline that demonstrates how regression models operate in practice.

What I learned from building it

This project helped me understand how machine learning models are trained and applied in real scenarios. I learned how data is structured for regression problems and how scikit-learn simplifies model building.

It also gave me hands-on experience with the full process of a basic ML workflow, from data handling to prediction output.

Possible improvements

Adding evaluation metrics such as R² score and mean absolute error
Visualizing the regression line to better understand model behavior
Expanding the dataset for better accuracy
Turning the model into a simple API using Flask or FastAPI
Adding input validation for more robustness

Project summary

A Python-based linear regression model that predicts student performance based on study hours. The project demonstrates a basic supervised learning workflow including data processing, model training and prediction generation.
