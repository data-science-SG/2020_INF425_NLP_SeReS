import streamlit as st
import time

def createSpaces():
    '''
    Cria um espaço para separar as informaçç
    '''
    st.write('#')

def showProgressBar(sleep=0.01):
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(sleep)
        my_bar.progress(percent_complete + 1)