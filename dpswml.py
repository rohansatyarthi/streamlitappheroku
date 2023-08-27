import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the models
diabetes_model_kn = pickle.load(open('C:/Users/ashis/OneDrive/Desktop/Diabetese Prediction System/Saved Model/diabetes_model_kn.sav', 'rb'))
diabetes_model_rf = pickle.load(open('C:/Users/ashis/OneDrive/Desktop/Diabetese Prediction System/Saved Model/diabetes_model_rf.sav', 'rb'))
diabetes_model_svm = pickle.load(open('C:/Users/ashis/OneDrive/Desktop/Diabetese Prediction System/Saved Model/diabetes_model_svm.sav', 'rb'))

# Create a dictionary to map algorithm names to their respective models
algorithm_models = {
    'K Neighbour': diabetes_model_kn,
    'Random Forest': diabetes_model_rf,
    'SVM': diabetes_model_svm,
}

st.sidebar.title('Diabetes Prediction with Different Algorithms')
selected_algorithm = st.sidebar.selectbox('Select an algorithm', list(algorithm_models.keys()))

st.title(selected_algorithm)

col1, col2, col3 = st.columns(3)

with col1:
    Pregnancies = st.text_input('Number of Pregnancies')

with col2:
    Glucose = st.text_input('Glucose Level')

with col3:
    BloodPressure = st.text_input('Blood Pressure Value')

with col1:
    SkinThickness = st.text_input('Skin Thickness Value')

with col2:
    Insulin = st.text_input('Insulin Level')

with col3:
    BMI = st.text_input('BMI Value')

with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

with col2:
    Age = st.text_input('Age of the person')

diab_diagnosis = ''

if st.button('Diabetes Test Result'):
    selected_model = algorithm_models[selected_algorithm]
    # Convert input values to numeric
    input_data = [
        float(Pregnancies), float(Glucose), float(BloodPressure), 
        float(SkinThickness), float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)
    ]
    diab_prediction = selected_model.predict([input_data])

    if diab_prediction[0] == 1:
        diab_diagnosis = 'The Person is Diabetic'
    else:
        diab_diagnosis = 'The Person is Not Diabetic'

st.success(diab_diagnosis)
