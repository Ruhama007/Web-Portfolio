import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")

content = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit."
           "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
           "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi.")
st.write(content)

st.title("Our Team")

col1, empty_col1, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

df = pandas.read_csv("4data.csv", sep=",")

with col1:
    for index, row in df[:5].iterrows():
        list1 = row.get("first name")
        st.header(row["first name"])
        #st.header(["last name"])
        st.write(row["role"])
        st.image("4images/" + row["image"])

with col2:
    for index, row in df[5:10].iterrows():
        list1 = row.get("first name")
        st.header(row["first name"])
        #st.header(["last name"])
        st.write(row["role"])
        st.image("4images/" + row["image"])

with col3:
    for index, row in df[10:12].iterrows():
        list1 = row.get("first name")
        st.header(row["first name"])
        #st.header(["last name"])
        st.write(row["role"])
        st.image("4images/" + row["image"])