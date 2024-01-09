import streamlit as st
import pandas as pd
from database import viewTables

def read():
    menu = ["Member", "MemberEmail", "MemberPhone", "Payment", "Facility", "MembershipFacility", "Trainer", "TrainerEmail", "TrainerPhone", "TrainerSchedule"]
    choice = st.sidebar.selectbox("Menu", menu)
    result = viewTables(choice)
    df = pd.DataFrame()  # Initialize df here


    if choice == menu[0]:
        df = pd.DataFrame(result, columns=("MembershipID", "MembershipType", "MembershipDuration", "StartDate", "EndDate", "TrainerService", "FirstName", "LastName"))
    elif choice == menu[1]:
        df = pd.DataFrame(result, columns=("MemberEmailID", "MembershipID", "Email"))
    elif choice == menu[2]:
        df = pd.DataFrame(result, columns=("MemberPhoneID", "MembershipID", "PhoneNumber"))
    elif choice == menu[3]:
        df = pd.DataFrame(result, columns=("PaymentID", "MembershipID", "PaymentDate", "Amount"))
    elif choice == menu[4]:
        df = pd.DataFrame(result, columns=("FacilityID", "FacilityName"))
    elif choice == menu[5]:
        df = pd.DataFrame(result, columns=("MembershipFacilityID", "MembershipID", "FacilityID", "BookingDate"))
    elif choice == menu[6]:
        df = pd.DataFrame(result, columns=("TrainerID", "FirstName", "LastName"))
    elif choice == menu[7]:
        df = pd.DataFrame(result, columns=("TrainerEmailID","TrainerID", "Email"))
    elif choice == menu[8]:
        df = pd.DataFrame(result, columns=("TrainerPhoneID", "TrainerID", "PhoneNumber"))
    elif choice == menu[9]:
        df = pd.DataFrame(result, columns=("TrainerScheduleID", "TrainerID", "MembershipID", "TrainingDate"))

    st.dataframe(df)

