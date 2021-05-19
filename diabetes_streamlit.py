import pandas as pd
import streamlit as st
data=pd.read_csv('diabetes.csv')
st.write('Developed by Adil')
st.title('Diabetes Onset Prediction App')
st.sidebar.header('User Inputs')

def user_input():
	pregnancy=st.sidebar.slider('Pregnancy(No.of times Pregnant)',0,17)
	glucose=st.sidebar.slider('Glucose(Plasma Glucose Level)',0,199)
	bp=st.sidebar.slider('Diastolic Blood Pressure(mmHg)',0,122)
	skinThickness=st.sidebar.slider('Triceps SkinFold Thickness',0,99)
	insulin=st.sidebar.slider('Insulin',0,846)
	bmi=st.sidebar.slider('BMI',0.0, 67.1)
	dpf=st.sidebar.slider('Diabetes pedigree function',0.078, 2.42)
	age=st.sidebar.slider('Age',0,81)
	data={'pregnancy':pregnancy,
	'glucose':glucose,
	'B.P':bp,
	'Skin Thickness':skinThickness,
	'Insulin':insulin,
	'BMI':bmi,
	'DPF':dpf,
	'Age':age}
	df=pd.DataFrame(data,index=[0])
	st.write(df)
	return df
f=user_input()
#model
x=data.drop(['Outcome'],axis=1)
y=data['Outcome']
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
model.fit(x,y)
pred=model.predict(f)
st.write('Class Labels')
st.write(pd.DataFrame({'0':'Safe','1':'Not Safe'},index=[0]))
st.write("""
# Prediction	""")
st.write(pred)





