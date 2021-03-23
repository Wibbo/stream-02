import streamlit as st
import numpy as np
import pandas as pd

st.title('Exploring Excel data')

file_loader = st.sidebar.file_uploader('Please select an Excel file:')


if file_loader is not None:
    df_excel = pd.read_excel(file_loader)



