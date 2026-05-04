import streamlit as st
import pickle
import numpy as np

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
st.title("Iris Flower Classifier")
st.write("أدخل أبعاد الزهرة لتوقع فصيلتها:")
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.0)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.0)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.5)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2)
if st.button("Predict"):

    user_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    
 
    prediction = model.predict(user_data)
    result = prediction[0]
    

    classes = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
    final_class = classes[result]
    
   
    st.success(f"Predicted Class: {final_class}")