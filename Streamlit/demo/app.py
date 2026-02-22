import numpy as np
import pandas as pd
import streamlit as st

# Title of the application
st.title("Hello Streamlit!")

# Writing a simple text
st.write("Writing a text")

# Creating a dataframe and displaying it
df = pd.DataFrame(
    np.random.randint(1,100,size=(3,3)),
    columns=["No.1","No.2","No.3"]
)

st.write("The dataframe is: \n")
st.write(df)
st.line_chart(df)
