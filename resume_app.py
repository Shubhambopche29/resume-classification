# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 12:44:35 2023

@author: Jeevika
"""

import numpy as np
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import streamlit as st 


from PIL import Image

#loading in the model the random forest  file
pkl_in = open('rf_clf.pkl', 'rb')
loaded_random = pickle.load(pkl_in)

# loading in the model to predict on the data
pickle_in = open('rf_clf.pkl', 'rb')
classifier = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs

def prediction(skills):

    r = classifier.predict(loaded_random.transform([skills]))
    print(r)
    return r

# this is the main function in which we define our webpage

def main():

    # giving the webpage a title

    st.title("Resume Screening")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed

    html_temp = '''
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Resume screening ML App </h1>
    </div>
    '''
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code

    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction

skills = st.text_input("skills", "Type Here")

result =""


if st.button("Predict"):
 result = prediction(Skills)
st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()


