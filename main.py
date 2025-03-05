import streamlit as st
from src.pipeline.prediction_pipeline import CustomData, PredictionPipeline

def main():
    st.title("Census Income Prediction App")
    st.write("Enter the details below to predict whether the income is above or below 50K.")

    # Input fields
    age = st.number_input("Age", min_value=0, format="%d")
    education_num = st.number_input("Education Num", min_value=0, format="%d")
    capital_gain = st.number_input("Capital Gain", min_value=0.0, format="%.2f")
    hours_per_week = st.number_input("Hours per Week", min_value=0, format="%d")
    workclass = st.selectbox("Workclass", ["Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov", "State-gov", "Without-pay", "Never-worked"])
    education = st.selectbox("Education", ["Bachelors", "Some-college", "11th", "HS-grad", "Prof-school", "Assoc-acdm", "Assoc-voc", "9th", "7th-8th", "12th", "Masters", "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool"])
    marital_status = st.selectbox("Marital Status", ["Married-civ-spouse", "Divorced", "Never-married", "Separated", "Widowed", "Married-spouse-absent", "Married-AF-spouse"])
    occupation = st.selectbox("Occupation", ["Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial", "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv", "Protective-serv", "Armed-Forces"])
    relationship = st.selectbox("Relationship", ["Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", "Unmarried"])
    race = st.selectbox("Race", ["White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"])
    sex = st.selectbox("Sex", ["Male", "Female"])
    
    if st.button("Predict Income"):
        try:
            # Prepare data
            data = CustomData(age, education_num, capital_gain, hours_per_week, workclass, education, marital_status, occupation, relationship, race, sex)
            final_new_data = data.get_data_as_dataframe()
            
            # Prediction
            predict_pipeline = PredictionPipeline()
            pred = predict_pipeline.predict(final_new_data)
            result = "More than 50K (>50K)" if pred[0] == 1.0 else "Less than 50K (<50K)"
            
            st.success(f"Predicted Income: {result}")
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
