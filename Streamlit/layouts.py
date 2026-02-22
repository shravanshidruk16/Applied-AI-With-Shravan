import streamlit as st

# Building a sidebar
st.sidebar.title("Login")
st.sidebar.write("Welcome to Coder's Of Pune Login Page")
name = st.sidebar.text_input("Enter Your Name: ")
number = st.sidebar.number_input("Enter Your Contact no. : ")

st.title("Welcome to Advance streamlit concepts")
st.button("Click me",help="Don't click me")