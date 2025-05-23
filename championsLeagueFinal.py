import streamlit as st

# Title
st.title("Simple Streamlit Input/Output App")

# Text input from the user
user_input = st.text_input("Enter something:")

# Output
if user_input:
    st.write("You entered:", user_input)
