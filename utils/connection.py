import joblib
import pandas as pd
import numpy as np
from scipy.stats import mode

def preprocess(data):
    """
    Preprocess the input data for prediction.
    - Drop unnecessary columns
    - Handle categorical encoding or scaling if done during training
    """
    # Convert input to a DataFrame if necessary
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame([data])
    
    # Drop the 'Patient Id' column if present
    if 'Patient Id' in data.columns:
        data = data.drop('Patient Id', axis=1)

    # Ensure data types match the training data
    data = data.astype(float)

    return data

def predict(data):
    """
    Predict the cancer risk level using all trained models and return a cumulative prediction.
    """
    # Preprocess the input data
    data = preprocess(data)

    # Load all trained models
    models = {
        "RandomForest": joblib.load("notebooks/random.pkl"),
        "KNN": joblib.load("notebooks/KNN.pkl"),
        "KMeans": joblib.load("notebooks/KM.pkl"),
        "DecisionTree": joblib.load("notebooks/tree.pkl"),
        "SVM": joblib.load("notebooks/svm.pkl")
    }

    # Collect predictions from all models
    predictions = []
    for name, model in models.items():
        pred = model.predict(data)
        # print(f"Prediction from {name}: {pred}")  # Debug: Check the model output
        # Ensure we are getting a scalar value from the prediction
        predictions.append(int(pred[0]))  # Convert to int to avoid numpy issues

    # print(f"Predictions: {predictions}")  # Debug: Show the list of predictions

    # Aggregate predictions (Majority Voting)
    mode_result = mode(predictions)  # This returns a ModeResult object
    # print(f"Mode result: {mode_result}")  # Debugging the mode result
    final_prediction = int(mode_result.mode)  # Access the mode directly as int

    return final_prediction
