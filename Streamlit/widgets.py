import streamlit as st

st.write("If don't give unique key to these below two button then definately streamlit will give an error to us as you of duplicate button is done ! ")
st.button("Ok",key='btn1')
st.button("Ok",key='btn2')
