import streamlit as st

st.title("Streamlit text input")

#Taking a text input from the user

name = st.text_input("Enter your name: ")

if name:
    st.write(f"Hello, {name}")
else:
    st.write("Invalid error occured")

age = st.slider("Select Your Age",18,60,25) # start slider from 18 end at 60 use default at 25

st.write("Your age is : ",age)