import streamlit as st
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
le1 = LabelEncoder()
le1 = joblib.load('GenreEncoding.joblib')
model = joblib.load('MLmodel.h5')
scaler = joblib.load('MLscaler.h5')
input = list()
st.title('IMDB movie earning prediction')
with st.form(key='my_form'):
    name = st.text_input('Enter the name of the movie')
    year = st.text_input('Enter the year of the movie realese')
    duration = st.number_input('Enter the duration in minute of the movie')
    rating = st.number_input('Enter the movie rating')
    metascore = st.number_input('Enter the meta score')
    votes = st.text_input('Enter number of votes')
    Genres = st.text_input('Enter the movies genres')


    submit_button = st.form_submit_button(label='Predict')
if submit_button:
    years = int(float(year))
    votes = int(float(votes))
    Genres = le1.transform([Genres])[0]
    input.append(years)
    input.append(duration)
    input.append(rating)
    input.append(metascore)
    input.append(votes)
    input.append(Genres)
    profit = model.predict(scaler.transform([input]))
    st.header('the movie '+name+' predicted earning will be '+ str(profit))
