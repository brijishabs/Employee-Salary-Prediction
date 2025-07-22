import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("best_model.pkl")

# Title
st.title("Employee Salary Prediction App")

# Sidebar inputs
st.sidebar.header("Enter Employee Details")

# Sample categories – replace these with your actual values from the dataset
education_levels = ["High School", "Bachelor", "Master", "PhD", "Other"]
age_range = list(range(18, 66))  # from 18 to 65
occupations = ["Software Engineer", "Data Scientist", "Manager", "Sales", "HR", "Other"]

# Select inputs
education = st.sidebar.selectbox("Education Level", education_levels)
age = st.sidebar.selectbox("Age", age_range)
occupation = st.sidebar.selectbox("Occupation", occupations)

# Map inputs to numerical values if required by the model
# Update this mapping as per your model's training
education_map = {level: i for i, level in enumerate(education_levels)}
occupation_map = {job: i for i, job in enumerate(occupations)}

# Prepare the input for prediction
input_features = np.array([[education_map[education], age, occupation_map[occupation]]])

# Predict button
if st.button("Predict Salary"):
    prediction = model.predict(input_features)
    st.success(f"Predicted Salary: ₹ {prediction[0]:,.2f}")
