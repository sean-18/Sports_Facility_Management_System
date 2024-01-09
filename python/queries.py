import streamlit as st
import pandas as pd
from database import viewQueryResult


def predef_queries():
    q = [   "Get members with Gym membership who have made payments",
            "Get members with Sports membership who have made payments",
            "Get members with Combination membership who have made payments",
            "Get trainers who have scheduled training sessions",
            "Get member with all their numbers and emails"
            ]
    choice = st.selectbox("Choose a Query: ", q)
    print(choice)
    result = viewQueryResult(q.index(choice) + 1)
    if (choice == q[0]):
        df = pd.DataFrame(result, columns=("MembershipID", "FirstName", "LastName", "Amount"))
        st.dataframe(df)
    elif (choice == q[1]):
        df = pd.DataFrame(result, columns=("MembershipID", "FirstName", "LastName", "Amount"))
        st.dataframe(df)
    elif (choice == q[2]):
        df = pd.DataFrame(result, columns=("MembershipID", "FirstName", "LastName", "Amount"))
        st.dataframe(df)
    elif (choice == q[3]):
        df = pd.DataFrame(result, columns=("FirstName", "LastName", "TrainingSessionsCount"))
        st.dataframe(df)
    elif (choice == q[4]):
        df = pd.DataFrame(result, columns=("MembershipID", "FullName", "Emails", "PhoneNumbers"))
        st.dataframe(df)
