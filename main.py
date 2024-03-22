import pickle
import streamlit as st

model = pickle.load(open('C:/Users/Raj/OneDrive/Desktop/EP 6th Sem/EE769 Introduction to Machine Learning/Assignments/trained_model.sav', 'rb'))

def main():
    st.title('Wine Quality Prediction')

    #Input Variables
    fixed_acidity = st.text_input('fixed acidity')
    volatile_acidity = st.text_input('volatile_acidity')
    citric_acid = st.text_input('citric_acid')
    residual_sugar = st.text_input('residual_sugar')
    chlorides = st.text_input('chlorides')
    free_sulfur_dioxide = st.text_input('free_sulfur_dioxide')
    total_sulfur_dioxide = st.text_input('total_sulfur_dioxide')
    density = st.text_input('density')
    pH = st.text_input('pH')
    sulphates = st.text_input('sulphates')
    alcohol = st.text_input('alcohol')

    #Prediction Code
    if st.button('Predict'):
        makeprediction = model.predict([[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]])
        output = round(makeprediction[0], 2)
        st.success('Quality of wine is {}'.format(output))

if __name__== '__main__':
    main()

