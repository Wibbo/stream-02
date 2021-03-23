import streamlit as st
import numpy as np
import pandas as pd

st.title('This is streamlit')

left_column, right_column = st.beta_columns(2)
# You can use a column just like st.sidebar:
st.button('wazzap')


if st.button('wazzap'):
    st.write('You clicked me')


# Add a select box to the sidebar:
#add_selectbox = st.sidebar.selectbox(
#    'How would you like to be contacted?',
#    ('Email', 'Home phone', 'Mobile phone')
#)

# Add a slider to the sidebar:
#add_slider = st.sidebar.slider(
#    'Select a range of values',
#    0.0, 100.0, (25.0, 75.0)
#)



