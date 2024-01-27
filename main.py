import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Asmin Bingöl")
    content = """ 
    Hi, I am Asmin. I study Electrical Electronics Engineering in Boğaziçi University. I want to be a programmer. I hope that you like my work.
    """
    st.info(content)

content2 = """
Below you can find some apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

df = pandas.read_csv("data.csv", sep=";")
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[1::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
