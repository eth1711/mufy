import streamlit as st
import random

# -----------------------------------
# PAGE SETTINGS
# -----------------------------------
st.set_page_config(
    page_title="Fake AI Excuse Generator",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------------
# TITLE
# -----------------------------------
st.title("🤖 Fake AI Excuse Generator")
st.write("Generate hilarious excuses instantly.")

# -----------------------------------
# INPUT
# -----------------------------------
scenario = st.text_input(
    "What happened?",
    placeholder="Example: I forgot my homework"
)

# -----------------------------------
# EXCUSE PARTS
# -----------------------------------
characters = [
    "my cat",
    "a monkey",
    "my neighbour",
    "an AI robot",
    "a delivery rider",
    "my cousin",
    "a random uncle",
]

actions = [
    "stole",
    "deleted",
    "hid",
    "accidentally launched",
    "confused",
    "replaced",
    "destroyed",
]

objects = [
    "my homework",
    "my laptop",
    "my notes",
    "my assignment",
    "my alarm",
    "my internet router",
]

reasons = [
    "during a thunderstorm.",
    "while I was sleeping.",
    "during a software update.",
    "because Mercury was in retrograde.",
    "while I was making coffee.",
    "after pressing the wrong button.",
]

# -----------------------------------
# BUTTON
# -----------------------------------
if st.button("Generate Excuse 🎲"):

    if scenario.strip() == "":
        st.warning("Please enter a scenario.")
    else:

        excuse = (
            f"Sorry, {scenario.lower()} because "
            f"{random.choice(characters)} "
            f"{random.choice(actions)} "
            f"{random.choice(objects)} "
            f"{random.choice(reasons)}"
        )

        st.success(excuse)

        st.balloons()

# -----------------------------------
# FOOTER
# -----------------------------------
st.divider()
st.caption("Built with Streamlit + Python")