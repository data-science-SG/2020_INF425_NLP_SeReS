import streamlit as st
import time

@st.cache
def loadEmbedding():
    time.sleep(2)
    return "boy it's loaded"

username = st.text_input('Insira o usuário:')

if (st.button('Executar algoritmo')):
    st.write(loadEmbedding())

# @st.cache(suppress_st_warning=True)  # 👈 Changed this
# def expensive_computation(a, b):
#     # 👇 Added this
#     st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
#     time.sleep(2)  # This makes the function take 2s to run
#     return a * b

# a = 2
# b = 22
# res = expensive_computation(a, b)

# st.write("Result:", res)
