import streamlit as st
from datetime import datetime

st.title("User Information form")

# With the help of the with statement every single change on the website prevents reloading the website and submiting the data
# When we press submit button then only everything gets submitted

form_values = {
    "Name":None,
    "Height":None,
    "Gender":None,
    "DOB":None
}

min_date = datetime(1990,1,1)
max_date = datetime.now()

with st.form(key="user_info_form"):
    form_values['Name'] = st.text_input("Enter Your Name:")
    form_values['Height'] = st.number_input("Enter Your Height (cm):")
    form_values['Gender'] = st.selectbox("Enter Your Gender:",["Male","Female"])
    form_values['DOB'] = st.date_input("Enter Your birth date:",max_value = max_date, min_value = min_date)

    submit_btn = st.form_submit_button(label="Submit Info")
    if submit_btn:
        if not all(form_values.values()):
            st.warning("Please fill in all of your fields")
        else:
            st.balloons() # to pass balloon from the screen as successfull completion of form is done
            st.write("### Your Information")
            for (key,value) in form_values.items():
                st.write(f"{key} : {value}")
