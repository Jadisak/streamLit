import streamlit as st
import pandas as pd

st.title("Getting started StreamLIT")
st.title("Getting started StreamLIT")

run_btn = st.button("Ruuuun!")
if run_btn:
    st.markdown("Button has already clicked")

show_btn = st.button("SHOW!")
if show_btn:
    st.markdown("Button SHOW has already clicked")

age_inp = st.number_input("Input your Age")
st.markdown(f"Your age is {age_inp}")

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

st.dataframe(df, use_container_width=True)