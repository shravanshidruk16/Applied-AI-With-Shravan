import streamlit as st
import os

# Website title
st.title("My website")

# Header
st.header("This is a header")

# SubHeader
st.subheader("This is a sub-header")

# Markdown
st.markdown("This is my **Markdown** text")

# Caption
st.caption("This is small caption")

# Code eg
code_eg = """
def sum(a,b):
    return a+b
"""

st.code(code_eg,language="python")

# Line divider
st.divider()

# Adding image
st.image(os.path.join(os.getcwd(),"static","image.jpg"),width=300)




