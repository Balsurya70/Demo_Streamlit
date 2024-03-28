import streamlit as st
import sqlite3
connector = sqlite3.connect('Student.db')
cursor = connector.cursor()

fname = st.text_input("Enter First Name : ")
lname = st.text_input("Enter Last Name : ")
adr = st.text_area("Enter Address : ")
clas = st.selectbox("Select class ", (1, 2, 3, 4, 5, 6, 7))
button = st.button("done")

if button:
    st.markdown(f"""
    First name : {fname}
    Last Name : {lname}
    Address : {adr}
    Class : {clas} """)

