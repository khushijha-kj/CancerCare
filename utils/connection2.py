import joblib
import pandas as pd
import numpy as np

def preprocess(data):
    """
    Preprocess the input data for prediction.
    - Drop unnecessary columns
    - Handle categorical encoding or scaling if done during training
    """
    # Convert input to a DataFrame if necessary
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame([data])
    
    # Drop the 'Patient Id' column if present (assuming this column might be there)
    if 'Patient Id' in data.columns:
        data = data.drop('Patient Id', axis=1)

    # Ensure data types match the training data (convert to float)
    data = data.astype(float)

    return data




# List of features the model was trained on
required_features = [
    "mean_radius", "mean_texture", "mean_perimeter", "mean_area", "mean_smoothness",
    "mean_compactness", "mean_concavity", "mean_concave_points", "mean_symmetry", "mean_fractal_dimension",
    "se_radius", "se_texture", "se_perimeter", "se_area", "se_smoothness",
    "se_compactness", "se_concavity", "se_concave_points", "se_symmetry", "se_fractal_dimension",
    "worst_radius", "worst_texture", "worst_perimeter", "worst_area", "worst_smoothness",
    "worst_compactness", "worst_concavity", "worst_concave_points", "worst_symmetry", "worst_fractal_dimension"
]

def predict(data):
    """
    Predict the cancer risk level using the trained Logistic Regression model.
    """
    # Load the trained Logistic Regression model
    model = joblib.load("notebooks/LR.pkl")
    
    # Ensure the input data contains only the required features
    data = {key: data[key] for key in required_features if key in data}
    
    # Check if we have all required features
    if len(data) != len(required_features):
        raise ValueError(f"Input data is missing features. Expected {len(required_features)} features, but got {len(data)}.")
    
    # Convert the dictionary to a list of feature values
    data = list(data.values())
    
    # Ensure the data is in 2D array format
    data_2d = [data]  # Wrap the input data in a list to make it 2D
    
    # Make prediction using the model
    prediction = model.predict(data_2d)  # Now data_2d is 2D
    
    # Return the prediction
    return prediction[0]  # Return the first (and only) prediction

