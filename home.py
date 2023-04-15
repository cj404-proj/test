import streamlit as st
import pandas as pd
st.header("Hellow")
slider_value = st.slider(label="Slider",max_value=100,min_value=0,step=10)
st.write(f"The slider value is {slider_value}")
