import streamlit as st

from src.data_wrangler import clean_text
from src.predictor import predict

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# page configuration
st.set_page_config(
    page_title='Fake News Detector',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Title
st.title('Fake News Detector')

# Text box for user input
text = st.text_area('Paste your text here:')

# Get model path
model_path = './models/LinearRegressor.pkl'

# Trigger actions when the button is clicked
if st.button("Text Check"):

    # Clean Text
    text=clean_text(text)

    # Make predictions
    predictions=predict(text, model_path)
    
    # Print a Subheader
    st.subheader('Predicted Class')
 
    # Make results
    if predictions == 1:
        st.write("The News is Real")
    else:
        st.write("The News is False")
