import streamlit as st
from database import add_member, add_trainer, ScheduleTrainingSession, InsertMembershipFacility, get_membershipid_for_trainer, get_trainerid, get_membershipid_for_facility,get_membershipid, AddMemberPhoneNumber, AddTrainerEmailAddress, AddMemberEmailAddress, AddTrainerPhoneNumber

def add():
    menu = ["Member", "Trainer", "ScheduleTrainingSession", "MembershipFacility", "add another member phone", "add another trainer mail", "add another member mail", "add another trainer phone"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Member
    if choice == menu[0]:
        col1, col2 = st.columns(2)
        mapping = {"Yes": "1", "No": "0"}
        reverse_mapping = {v: k for k, v in mapping.items()}
        with col1:
            p_FirstName = st.text_input("First Name: ")
            p_LastName = st.text_input("Last Name: ")
            p_MembershipType = st.selectbox("Type: ", ["Gym", "Sports", "Combination"])
            p_StartDate = st.text_input("Select a date")
        with col2:
            p_Email = st.text_input("Email :")
            p_PhoneNumber = st.text_input("Phone Number:")
            p_MembershipDuration = st.selectbox("Duration: ", ['3', '6', '12'])
            p_TrainerService = st.selectbox("Trainer Service: ", ["Yes", "No"])

        if st.button("Add Member"):
            add_member(p_MembershipType, p_MembershipDuration, p_StartDate, mapping.get(p_TrainerService), p_FirstName, p_LastName, p_Email, p_PhoneNumber)
            st.success("Member added successfully: {}".format(p_FirstName))

    # Trainer
    if choice == menu[1]:
        col1, col2 = st.columns(2)
        with col1:
            p_FirstName = st.text_input("First Name: ")
            p_LastName = st.text_input("Last Name: ")

        with col2:
            p_Email = st.text_input("Email :")
            p_PhoneNumber = st.text_input("Phone Number:")

        if st.button("Add Trainer"):
            add_trainer(p_FirstName, p_LastName, p_Email, p_PhoneNumber)
            st.success("Trainer added successfully: {}".format(p_FirstName))

    # ScheduleTrainingSession
    if choice == menu[2]:
        col1, col2 = st.columns(2)
        list_of_id1 = []
        list_of_id2 = []
        with col1:
            list_of_id1 = [i[0] for i in get_trainerid()]
            list_of_id2 = [i[0] for i in get_membershipid_for_trainer()]
            p_TrainerID = st.selectbox("Enter TrainerID", list_of_id1)
            p_MembershipID = st.selectbox("Enter MembershipID", list_of_id2)

        with col2:
            p_TrainingDate = st.text_input("Select a date")

        if st.button("Add Trainer Session"):
            ScheduleTrainingSession(str(p_TrainerID), str(p_MembershipID), p_TrainingDate)
            st.success("Trainer session booked successfully at: {}".format(p_TrainingDate))

    # MembershipFacility
    if choice == menu[3]:
        col1, col2 = st.columns(2)
        list_of_id = []
        with col1:
            list_of_id = [i[0] for i in get_membershipid_for_facility()]
            p_FacilityID = st.text_input("Enter FacilityID")
            p_MembershipID = st.selectbox("Enter MembershipID", list_of_id)

        with col2:
            p_BookingDate = st.text_input("Select a date")

        if st.button("Add Facility Session"):
            InsertMembershipFacility(str(p_MembershipID), p_FacilityID, p_BookingDate)
            st.success("Play session booked successfully at: {}".format(p_BookingDate))

    # another member phone
    if choice == menu[4]:
        col1, col2 = st.columns(2)
        list_of_id = []
        with col1:
            list_of_id = [i[0] for i in get_membershipid()]
            p_MembershipID = st.selectbox("Enter MembershipID", list_of_id)

        with col2:
            p_NewNumber = st.text_input("Enter number")

        if st.button("Add Number"):
            AddMemberPhoneNumber(str(p_MembershipID), p_NewNumber)
            st.success("New Number Added: {}".format(p_MembershipID))

    # another trainer email
    if choice == menu[5]:
        col1, col2 = st.columns(2)
        list_of_id = []
        with col1:
            list_of_id = [i[0] for i in get_trainerid()]
            p_TrainerID = st.selectbox("Enter TrainerID", list_of_id)

        with col2:
            p_NewEmail = st.text_input("Enter Email:")

        if st.button("Add Email"):
            AddTrainerEmailAddress(str(p_TrainerID), p_NewEmail)
            st.success("New email added: {}".format(p_TrainerID))

    # another member email
    if choice == menu[6]:
        col1, col2 = st.columns(2)
        list_of_id = []
        with col1:
            list_of_id = [i[0] for i in get_membershipid()]
            p_MembershipID = st.selectbox("Enter MembershipID", list_of_id)

        with col2:
            p_NewEmail = st.text_input("Enter Email:")

        if st.button("Add Email"):
            AddMemberEmailAddress(str(p_MembershipID), p_NewEmail)
            st.success("New email added: {}".format(p_MembershipID))

    # another trainer phone
    if choice == menu[7]:
        col1, col2 = st.columns(2)
        list_of_id = []
        with col1:
            list_of_id = [i[0] for i in get_trainerid()]
            p_TrainerID = st.selectbox("Enter TrainerID", list_of_id)

        with col2:
            p_NewNumber = st.text_input("Enter number")

        if st.button("Add Number"):
            AddTrainerPhoneNumber(str(p_TrainerID), p_NewNumber)
            st.success("New Number Added: {}".format(p_TrainerID))

