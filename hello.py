import streamlit as st

st.title("OpenCV Streamlit Demo")
st.header('header')

image = st.file_uploader("Upload image file")
st.text("this is text")
selected_value = st.selectbox("Select box", options=['None', 'Filter 1', 'Filter 2'])
st.write(selected_value)

checkbox_value = st.checkbox("Apply Filter")
st.write(checkbox_value)