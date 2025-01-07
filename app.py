
import streamlit as st
from utils.connection import predict as lung_predict
from utils.connection2 import predict as breast_predict



# Map user-friendly feature names to model-compatible feature names for Lung Cancer
FEATURE_MAPPING_LUNG = {
    "Age": "Age",
    "Gender": "Gender",
    "Air Pollution": "AirPollution",
    "Alcohol Use": "Alcoholuse",
    "Dust Allergy": "DustAllergy",
    "Occupational Hazards": "OccuPationalHazards",
    "Genetic Risk": "GeneticRisk",
    "Chronic Lung Disease": "chronicLungDisease",
    "Balanced Diet": "BalancedDiet",
    "Obesity": "Obesity",
    "Smoking": "Smoking",
    "Passive Smoking": "PassiveSmoker",
    "Chest Pain": "ChestPain",
    "Coughing of Blood": "CoughingofBlood",
    "Fatigue": "Fatigue",
    "Weight Loss": "WeightLoss",
    "Shortness of Breath": "ShortnessofBreath",
    "Wheezing": "Wheezing",
    "Swallowing Difficulty": "SwallowingDifficulty",
    "Clubbing of Finger Nails": "ClubbingofFingerNails",
    "Frequent Cold": "FrequentCold",
    "Dry Cough": "DryCough",
    "Snoring": "Snoring",
}

# Map user-friendly feature names to model-compatible feature names for Breast Cancer
FEATURE_MAPPING_BREAST = {
    "mean_radius": "mean_radius",
    "mean_texture": "mean_texture",
    "mean_perimeter": "mean_perimeter",
    "mean_area": "mean_area",
    "mean_smoothness": "mean_smoothness",
    "mean_compactness": "mean_compactness",
    "mean_concavity": "mean_concavity",
    "mean_concave_points": "mean_concave_points",
    "mean_symmetry": "mean_symmetry",
    "mean_fractal_dimension": "mean_fractal_dimension",
    "se_radius": "se_radius",
    "se_texture": "se_texture",
    "se_perimeter": "se_perimeter",
    "se_area": "se_area",
    "se_smoothness": "se_smoothness",
    "se_compactness": "se_compactness",
    "se_concavity": "se_concavity",
    "se_concave_points": "se_concave_points",
    "se_symmetry": "se_symmetry",
    "se_fractal_dimension": "se_fractal_dimension",
    "worst_radius": "worst_radius",
    "worst_texture": "worst_texture",
    "worst_perimeter": "worst_perimeter",
    "worst_area": "worst_area",
    "worst_smoothness": "worst_smoothness",
    "worst_compactness": "worst_compactness",
    "worst_concavity": "worst_concavity",
    "worst_concave_points": "worst_concave_points",
    "worst_symmetry": "worst_symmetry",
    "worst_fractal_dimension": "worst_fractal_dimension"
}


# Set page config
st.set_page_config(page_title="Cancer Prediction", layout="wide")


# Heading Text
st.markdown(
    "<h1 style='text-align: center; color: white;'>PREDICT, PREVENT, PROTECT</h1>", 
    unsafe_allow_html=True

    
)

# Sidebar with navigation
st.sidebar.title("Welcome to CancerCare!")
option = st.sidebar.radio(
    "Select an Option",
    ("Home","Lung Cancer Prediction", "Breast Cancer Prediction", "Trusted Cancer Information", "General Tips")
)

if(option == "Home"):
    st.write("""
    Cancer is a complex group of diseases characterized by uncontrolled cell growth and spread to other parts of the body. It is one of the leading causes of death worldwide, with millions of people being diagnosed each year. Cancer can develop in any organ or tissue in the body, and its causes are varied, including genetic factors, lifestyle choices, and environmental exposures. While each type of cancer is unique, early detection and treatment play crucial roles in improving outcomes and survival rates. Advances in medical research have led to significant improvements in cancer diagnosis, treatment, and prevention, but challenges remain, especially for more aggressive or late-stage cancers.
    
    The treatment of cancer typically involves a combination of surgery, chemotherapy, radiation therapy, and more recently, targeted therapies and immunotherapies. These treatments aim to remove or destroy cancer cells, slow their growth, and prevent recurrence. Predicting the likelihood of cancer development or its recurrence is an area of active research, with scientists focusing on genetic and molecular markers that can help assess risk and tailor treatments. Personalized medicine, which takes into account an individual's unique genetic makeup, is also a promising approach to cancer treatment, ensuring that patients receive the most effective therapies. Despite the challenges, ongoing research continues to offer hope for better treatments, early detection methods, and, ultimately, a cure for many types of cancer.
    """)


# Display content based on selection
if option == "Lung Cancer Prediction":
    st.subheader("Lung Cancer Prediction")
    st.header("Enter Patient Details for Lung Cancer Prediction (1-10)")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        user_input = {}
        user_input["Age"] = st.number_input("Age", min_value=1, max_value=120, value=30)
        user_input["Gender"] = st.number_input("Gender (1 for Male, 2 for Female)", min_value=1, max_value=2, value=1)
        user_input["Air Pollution"] = st.number_input("Air Pollution Level", min_value=1, max_value=10, value=5)
        user_input["Alcohol Use"] = st.number_input("Alcohol Use Level", min_value=1, max_value=10, value=5)
        user_input["Dust Allergy"] = st.number_input("Dust Allergy Severity", min_value=1, max_value=10, value=5)
        user_input["Occupational Hazards"] = st.number_input("Occupational Hazards Level", min_value=1, max_value=10, value=5)

    with col2:
        user_input["Genetic Risk"] = st.number_input("Genetic Risk Level", min_value=1, max_value=10, value=5)
        user_input["Chronic Lung Disease"] = st.number_input("Chronic Lung Disease Level", min_value=1, max_value=10, value=5)
        user_input["Balanced Diet"] = st.number_input("Balanced Diet Level", min_value=1, max_value=10, value=5)
        user_input["Obesity"] = st.number_input("Obesity Level", min_value=1, max_value=10, value=5)
        user_input["Smoking"] = st.number_input("Smoking Level", min_value=1, max_value=10, value=5)

    with col3:
        user_input["Passive Smoking"] = st.number_input("Passive Smoking Level", min_value=1, max_value=10, value=5)
        user_input["Chest Pain"] = st.number_input("Chest Pain Level", min_value=1, max_value=10, value=5)
        user_input["Coughing of Blood"] = st.number_input("Coughing of Blood Level", min_value=1, max_value=10, value=5)
        user_input["Fatigue"] = st.number_input("Fatigue Level", min_value=1, max_value=10, value=5)
        user_input["Weight Loss"] = st.number_input("Weight Loss Level", min_value=1, max_value=10, value=5)

    with col4:
        user_input["Shortness of Breath"] = st.number_input("Shortness of Breath Level", min_value=1, max_value=10, value=5)
        user_input["Wheezing"] = st.number_input("Wheezing Level", min_value=1, max_value=10, value=5)
        user_input["Swallowing Difficulty"] = st.number_input("Swallowing Difficulty Level", min_value=1, max_value=10, value=5)
        user_input["Clubbing of Finger Nails"] = st.number_input("Clubbing of Finger Nails Level", min_value=1, max_value=10, value=5)
        user_input["Frequent Cold"] = st.number_input("Frequent Cold Level", min_value=1, max_value=10, value=5)

    with col5:
        user_input["Dry Cough"] = st.number_input("Dry Cough Level", min_value=1, max_value=10, value=5)
        user_input["Snoring"] = st.number_input("Snoring Level", min_value=1, max_value=10, value=5)

        # Convert user-friendly input to model-compatible input for lung cancer
    model_input = {FEATURE_MAPPING_LUNG[key]: value for key, value in user_input.items()}

        # Predict button for Lung Cancer
    if st.button("Predict Lung Cancer Risk"):
            try:
                prediction = lung_predict(model_input)
                if prediction == 1:  # High risk
                    st.error("High Risk of Lung Cancer\n\nIt's important to consult a healthcare professional immediately for further tests and advice.\nConsider quitting smoking, avoiding exposure to harmful substances, and adopting a healthy lifestyle.")
                else:  # Low risk
                    st.success("Low Risk of Lung Cancer\n\nGreat news! Keep up with healthy habits and stay proactive about your health.\nRemember to maintain regular check-ups and a balanced lifestyle to reduce any future risks.")

            except Exception as e:
                st.error(f"An error occurred: {e}")
    
elif option == "Breast Cancer Prediction":
    st.subheader("Breast Cancer Prediction")
    st.header("Enter Patient Details for Breast Cancer Prediction")
    # user_input_breast = {}
    # user_input_breast["mean_radius"] = st.number_input("Mean Radius", min_value=0.0)
    # user_input_breast["mean_texture"] = st.number_input("Mean Texture", min_value=0.0)
    # user_input_breast["mean_perimeter"] = st.number_input("Mean Perimeter", min_value=0.0)
    # user_input_breast["mean_area"] = st.number_input("Mean Area", min_value=0.0)
    # user_input_breast["mean_smoothness"] = st.number_input("Mean Smoothness", min_value=0.0)
    # user_input_breast["mean_compactness"] = st.number_input("Mean Compactness", min_value=0.0)
    # user_input_breast["mean_concavity"] = st.number_input("Mean Concavity", min_value=0.0)
    # user_input_breast["mean_concave_points"] = st.number_input("Mean Concave Points", min_value=0.0)
    # user_input_breast["mean_symmetry"] = st.number_input("Mean Symmetry", min_value=0.0)
    # user_input_breast["mean_fractal_dimension"] = st.number_input("Mean Fractal Dimension", min_value=0.0)
    # user_input_breast["se_radius"] = st.number_input("SE Radius", min_value=0.0)
    # user_input_breast["se_texture"] = st.number_input("SE Texture", min_value=0.0)
    # user_input_breast["se_perimeter"] = st.number_input("SE Perimeter", min_value=0.0)
    # user_input_breast["se_area"] = st.number_input("SE Area", min_value=0.0)
    # user_input_breast["se_smoothness"] = st.number_input("SE Smoothness", min_value=0.0)
    # user_input_breast["se_compactness"] = st.number_input("SE Compactness", min_value=0.0)
    # user_input_breast["se_concavity"] = st.number_input("SE Concavity", min_value=0.0)
    # user_input_breast["se_concave_points"] = st.number_input("SE Concave Points", min_value=0.0)
    # user_input_breast["se_symmetry"] = st.number_input("SE Symmetry", min_value=0.0)
    # user_input_breast["se_fractal_dimension"] = st.number_input("SE Fractal Dimension", min_value=0.0)
    # user_input_breast["worst_radius"] = st.number_input("Worst Radius", min_value=0.0)
    # user_input_breast["worst_texture"] = st.number_input("Worst Texture", min_value=0.0)
    # user_input_breast["worst_perimeter"] = st.number_input("Worst Perimeter", min_value=0.0)
    # user_input_breast["worst_area"] = st.number_input("Worst Area", min_value=0.0)
    # user_input_breast["worst_smoothness"] = st.number_input("Worst Smoothness", min_value=0.0)
    # user_input_breast["worst_compactness"] = st.number_input("Worst Compactness", min_value=0.0)
    # user_input_breast["worst_concavity"] = st.number_input("Worst Concavity", min_value=0.0)
    # user_input_breast["worst_concave_points"] = st.number_input("Worst Concave Points", min_value=0.0)
    # user_input_breast["worst_symmetry"] = st.number_input("Worst Symmetry", min_value=0.0)
    # user_input_breast["worst_fractal_dimension"] = st.number_input("Worst Fractal Dimension", min_value=0.0)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        user_input_breast = {}
        user_input_breast["mean_radius"] = st.number_input("Mean Radius", min_value=0.0)
        user_input_breast["mean_texture"] = st.number_input("Mean Texture", min_value=0.0)
        user_input_breast["mean_perimeter"] = st.number_input("Mean Perimeter", min_value=0.0)
        user_input_breast["mean_area"] = st.number_input("Mean Area", min_value=0.0)
        user_input_breast["mean_smoothness"] = st.number_input("Mean Smoothness", min_value=0.0)
        user_input_breast["mean_compactness"] = st.number_input("Mean Compactness", min_value=0.0)

    with col2:
        user_input_breast["mean_concavity"] = st.number_input("Mean Concavity", min_value=0.0)
        user_input_breast["mean_concave_points"] = st.number_input("Mean Concave Points", min_value=0.0)
        user_input_breast["mean_symmetry"] = st.number_input("Mean Symmetry", min_value=0.0)
        user_input_breast["mean_fractal_dimension"] = st.number_input("Mean Fractal Dimension", min_value=0.0)
        user_input_breast["se_radius"] = st.number_input("SE Radius", min_value=0.0)
        user_input_breast["se_texture"] = st.number_input("SE Texture", min_value=0.0)

    with col3:
        user_input_breast["se_perimeter"] = st.number_input("SE Perimeter", min_value=0.0)
        user_input_breast["se_area"] = st.number_input("SE Area", min_value=0.0)
        user_input_breast["se_smoothness"] = st.number_input("SE Smoothness", min_value=0.0)
        user_input_breast["se_compactness"] = st.number_input("SE Compactness", min_value=0.0)
        user_input_breast["se_concavity"] = st.number_input("SE Concavity", min_value=0.0)
        user_input_breast["se_concave_points"] = st.number_input("SE Concave Points", min_value=0.0)

    with col4:
        user_input_breast["se_symmetry"] = st.number_input("SE Symmetry", min_value=0.0)
        user_input_breast["se_fractal_dimension"] = st.number_input("SE Fractal Dimension", min_value=0.0)
        user_input_breast["worst_radius"] = st.number_input("Worst Radius", min_value=0.0)
        user_input_breast["worst_texture"] = st.number_input("Worst Texture", min_value=0.0)
        user_input_breast["worst_perimeter"] = st.number_input("Worst Perimeter", min_value=0.0)
        user_input_breast["worst_area"] = st.number_input("Worst Area", min_value=0.0)

    with col5:
        user_input_breast["worst_smoothness"] = st.number_input("Worst Smoothness", min_value=0.0)
        user_input_breast["worst_compactness"] = st.number_input("Worst Compactness", min_value=0.0)
        user_input_breast["worst_concavity"] = st.number_input("Worst Concavity", min_value=0.0)
        user_input_breast["worst_concave_points"] = st.number_input("Worst Concave Points", min_value=0.0)
        user_input_breast["worst_symmetry"] = st.number_input("Worst Symmetry", min_value=0.0)
        user_input_breast["worst_fractal_dimension"] = st.number_input("Worst Fractal Dimension", min_value=0.0)

    # Convert user-friendly input to model-compatible input for breast cancer
    model_input_breast = {FEATURE_MAPPING_BREAST[key]: value for key, value in user_input_breast.items()}

        # Predict button for Breast Cancer
    if st.button("Predict Breast Cancer Risk"):
            try:
                prediction = breast_predict(model_input_breast)
                if prediction == 1:  # Benign
                    st.success("Benign\n\nThis indicates a non-cancerous condition. However, further monitoring or treatment may be required. It's important to follow up with your healthcare provider for any necessary steps.")
                else:  # Malignant
                    st.error("Malignant\n\nThis indicates a potential cancerous condition. Immediate consultation with a specialist is highly recommended for further tests, diagnosis, and treatment options.")

            except Exception as e:
                st.error(f"An error occurred: {e}")
    
elif option == "Trusted Cancer Information":
    st.title("Trusted Resources for Cancer Information and Support")


    st.write(
        "Explore reliable and comprehensive resources to stay informed about cancer research, treatment, and patient care."
    )
    st.markdown(
    """
    - [**American Cancer Society**](https://www.cancer.org/): Access a wide range of information on cancer patients, survivors, caregivers, and the latest updates on cancer research and treatment.
    - [**National Cancer Institute**](https://www.cancer.gov/): Get comprehensive and up-to-date information on cancer research, treatment, and prevention, including news releases, publications, and expert blogs.
    - [**Cure Today**](https://www.curetoday.com/): Offers patient-centered information and support for individuals living with cancer, with expert advice and resources.
    - [**News-Medical.Net**](https://www.news-medical.net/medical): A science and medical news portal covering a broad spectrum of topics, including cutting-edge cancer research and advancements.
    """
    )
    st.write("These resources are dedicated to providing valuable knowledge and support for anyone impacted by cancer.")

elif option == "General Tips":
    st.subheader("General Cancer Tips")
    st.write("Here are some general cancer prevention tips:")
    st.write("- Maintain a healthy diet with plenty of fruits and vegetables.")
    st.write("- Engage in physical activity for at least 30 minutes most days of the week.")
    st.write("- Avoid smoking and tobacco products to lower your risk of various cancers.")
    st.write("- Limit alcohol consumption to reduce the risk of cancers like liver and breast cancer.")
    st.write("- Protect your skin by using sunscreen and avoiding tanning beds.")
    st.write("- Get regular screenings to catch potential cancers early.")
    st.write("- Know your family history and discuss genetic testing with your doctor.")
    st.write("- Manage stress with techniques like yoga or meditation to improve overall health.")


