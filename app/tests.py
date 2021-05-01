import streamlit as st
import time

@st.cache(suppress_st_warning=True)  # 👈 Changed this
def expensive_computation(a, b):
    # 👇 Added this
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return a * b


def createSpaces():
    '''
    Cria um espaço para separar as informaçç
    '''
    st.write('#')

a = 2
b = 21
res = expensive_computation(a, b)

st.write("Result:", res)

createSpaces()

st.write("Result:", res)

st.write("Result:", res)

st.write("Result:", res)

st.write("Result:", res)

import time
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)