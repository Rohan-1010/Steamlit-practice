#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import streamlit as st
import time


#st.title("Progress Bar")

#st.header("We are going to test out the progress bar..")

#prog = 0
#my_bar = st.progress(prog)

#prog = prog + 50
#my_bar.progress(prog)
#time.sleep(5)
#prog = prog + 50
#my_bar.progress(prog)
#st.success('Success!')


st.title("Creating a Web App")

" "

st.markdown("We are going to create a web app that takes 2 numbers and performs the chosen mathematical function.")

a = st.number_input("Enter 1st number: ", value = 0)

b = st.number_input("Enter 2nd number: ", value = 0)

" "

selection = st.radio('Which Mathematical Operation would you like to do?', ["Add", "Subtract", "Multiply", "Divide"])



if selection == "Add":

    prog = 0
    my_bar = st.progress(prog)
    time.sleep(2)
    prog = prog + 20
    my_bar.progress(prog)
    time.sleep(4)
    prog = prog + 60
    my_bar.progress(prog)
    prog = prog + 20
    my_bar.progress(prog)
    "Answer is: " + str(a + b)
    
elif selection == "Subtract":

    "Answer is: " + str(a - b)
    
elif selection == "Multiply":

    "Answer is: " + str(a * b)

elif selection == "Divide":

    "Answer is: " + str(a/b)

st.header("Testing out file uploader: ")

st.subheader("Do you have a file to upload?")

file_upload_q = st.button('Yes!')

if file_upload_q == True:

    file_upload = st.file_uploader("Upload your csv file")

    if file_upload is not None:

        df = pd.read_csv(file_upload)
        he = df.head()
        st.write(he)