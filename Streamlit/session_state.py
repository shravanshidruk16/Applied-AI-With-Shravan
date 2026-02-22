"""
Docstring for session_state
Session state : This concept came from the issue in streamlit forms that whenever any changes happen in the form it gets updated only when we submit the entire form , not dynamically it gets updated so due to this issue session state comes in the picture

Session state : It is something that we can use to store values within the same user session
Session get reset when we explicitly reload the website
"""

import streamlit as st

if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button('Increment Counter'):
    st.session_state.counter += 1
    st.write(f"Counter incremented to {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0

st.write(f"Counter value: {st.session_state.counter}")
