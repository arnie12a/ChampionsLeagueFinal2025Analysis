import streamlit as st
import pandas as pd

# Sidebar title
st.sidebar.title("Champions League Final")

# Dropdown with 6 options
option = st.sidebar.selectbox(
    "Choose an option:",
    ("Standard", "Shooting", "Defense", "Passing", "Goalkeeping", "Fixtures")
)

# Conditional inputs based on option
if option == "Overview":
    num_input = st.sidebar.number_input("Enter a number:")
    text_input = st.sidebar.text_input("Enter some text:")
elif option == "Shooting":
    date_input = st.sidebar.date_input("Pick a date:")
    color_input = st.sidebar.color_picker("Pick a color:")
elif option == "Defense":
    slider = st.sidebar.slider("Select a range:", 0, 100, (25, 75))
    checkbox = st.sidebar.checkbox("Enable something?")
elif option == "Passing":
    radio = st.sidebar.radio("Choose one:", ["A", "B", "C"])
    file = st.sidebar.file_uploader("Upload a file:")
elif option == "Goalkeeping":
    select = st.sidebar.selectbox("Select an item:", ["Apple", "Banana", "Cherry"])
    multi = st.sidebar.multiselect("Pick some things:", ["Red", "Green", "Blue"])
elif option == "Fixtures":
    time = st.sidebar.time_input("Select time:")
    password = st.sidebar.text_input("Enter password:", type="password")

# Submit button
submit = st.sidebar.button("Submit")

# Display dummy output
if submit:
    st.write(f"### You selected: {option}")
    st.write("#### Here’s some dummy data:")

    psg_df = pd.read_csv('./data/psg/' + str(option.lower()) + '.csv')
    intermilan_df = pd.read_csv('./data/intermilan/' + str(option.lower()) + '.csv')
    st.dataframe(psg_df)
    st.dataframe(intermilan_df)
