import streamlit as st
from create import add
from read import read
from queries import predef_queries
from update import update
from delete import delete

def main():
    st.title("MRDCenter Facilities Database")
    menu = ["Run Predefined Queries","Add Record", "View Tables", "Update Record", "Delete Records"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Add Record":
        add()
    elif choice == "View Tables":
        read()
    elif choice == "Update Record":
        update()
    elif choice == "Delete Records":
        delete()
    elif choice == "Run Predefined Queries":
        predef_queries()

if __name__ == '__main__':
 main()
