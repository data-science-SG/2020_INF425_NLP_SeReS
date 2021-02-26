import streamlit as st

contact_options   = ("Email", "Home phone", "Mobile phone")

contact_selectbox = st.sidebar.selectbox("How would you like to be contacted?", 
                                     contact_options, index=2)

st.text(f'SUA SELEÇÃO FOI {contact_selectbox}')