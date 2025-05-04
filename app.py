import streamlit as st
import random

st.title("🎯 Number Prediction Game")
st.write("Guess a number between 1 and 10")

# Generate a random number only once per session
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 10)

guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)

if st.button("Submit Guess"):
    if guess == st.session_state.number:
        st.success("🎉 Correct! You guessed it!")
        st.session_state.number = random.randint(1, 10)  # reset for new game
    elif guess < st.session_state.number:
        st.warning("Too low. Try again!")
    else:
        st.warning("Too high. Try again!")
