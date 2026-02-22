import pandas as pd
import streamlit as st

st.title("Pandas Dataframe")


st.header("Dataframe")

# Create a dataframe
df = pd.DataFrame({
    'Name':['Alice','Bob','Charlie','David'],
    'Age':[25,32,37,45],
    'Occupation':['Engineer','Doctor','Artist','Chef']
})

# To parse the dataframe on the website
st.dataframe(df)

# To make a dataframe editor 
st.header("Data Editor")
editable_df = st.data_editor(df) # Here the edited vales will get stored in this editable_df variable which we can use later on
st.subheader("Edited data: ")
st.dataframe(editable_df)

st.header("Simple table")
st.table(df)

# Metrics section
st.subheader("Metrics Section")
st.metric(label="Total Rows",value=len(df))
st.metric(label="Average age",value=df['Age'].mean())