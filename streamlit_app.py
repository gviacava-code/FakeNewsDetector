import streamlit as st
import pickle

from src.data_wrangler import clean_text

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# page configuration
st.set_page_config(
    page_title='Fake News Detector',
    layout='wide',
    initial_sidebar_state='expanded'
)

# title of the app
st.title('Fake News Detector')
text = st.text_area('Paste your text here:')

# import the model
model=pickle.load(open('./models/LinearRegressor.pkl', 'rb'))

if st.button("Text Check"):
    st.subheader('Predicted Class')
 
    # Clean Text
    text=clean_text(text)

    # Make predictions
    output=model.predict(text)
    if output == 1:
        st.write("The news is real")
    else:
        st.write("the news is false")
    # st.write(output)
