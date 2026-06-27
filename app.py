import streamlit as st

st.title("Age Detection Application")

name = st.text_input("Enter your name")

age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=120,
    step=1
)

if st.button("Submit"):
    if name == "":
        st.warning("Please enter your name")
    else:
        if age < 13:
            age_group = "Child"
        elif age < 20:
            age_group = "Teenager"
        elif age < 60:
            age_group = "Adult"
        else:
            age_group = "Senior Citizen"

        st.markdown(
            "<h3 style='color:blue'>Result:</h3>",
            unsafe_allow_html=True
        )
        st.success(f"Hello {name}, you are an {age_group}.")
