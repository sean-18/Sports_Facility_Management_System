import streamlit as st
from database import delRecMember
from database import delRecTrainer
from database import get_membershipid
from database import get_trainerid

def delete():
    menu = ["Member", "Trainer"]
    choice = st.sidebar.selectbox("Menu", menu)
    list_of_id = []
    if choice == menu[0]:
        list_of_id = [i[0] for i in get_membershipid()]
        id = st.selectbox("Enter MembershipID", list_of_id)
        if st.button("Delete Record"):
            delRecMember(str(id))
            st.success("Successfully deleted member")

    elif choice == menu[1]:
        list_of_id = [i[0] for i in get_trainerid()]
        id = st.selectbox("Enter TrainerID", list_of_id)
        if st.button("Delete Record"):
            delRecTrainer(str(id))
            st.success("Successfully deleted trainer")



