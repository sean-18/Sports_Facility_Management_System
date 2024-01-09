import streamlit as st
from database import updateStatus
from database import get_membershipid
def update():
    p_MemberID = st.selectbox("Enter Member ID", [i[0] for i in get_membershipid()])
    p_NewFirstName = st.text_input("New First Name: ")
    p_NewLastName = st.text_input("New Last Name: ")
    if st.button("Update Record"):
        updateStatus(str(p_MemberID), p_NewFirstName, p_NewLastName)
        st.success("Successfully updated record")