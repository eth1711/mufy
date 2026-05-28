import streamlit as st
import random

# -----------------------------------
# PAGE SETTINGS
# -----------------------------------
st.set_page_config(
    page_title="Student AI Excuse Generator",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------------
# TITLE
# -----------------------------------
st.title("🤖 Student AI Excuse Generator")
st.write("Generate realistic student excuses instantly 😎")

# -----------------------------------
# SCENARIOS
# -----------------------------------
scenario = st.selectbox(
    "What happened?",
    [
        "I forgot my homework",
        "I am late for class",
        "I missed a deadline",
        "I skipped class",
        "I forgot about a meeting",
        "I didn't reply my lecturer",
        "I forgot to study for a test"
    ]
)

# -----------------------------------
# EXCUSE DATABASE
# -----------------------------------
excuses = {

    "I forgot my homework": [
        "I accidentally uploaded the wrong file and only realized this morning.",
        "My laptop updated overnight and corrupted my document.",
        "I completed it but forgot to bring my laptop charger so I couldn't open it.",
        "I thought I submitted it but apparently the upload failed.",
        "I saved the file in the wrong folder and spent an hour trying to find it."
    ],

    "I am late for class": [
        "The traffic suddenly became terrible because of an accident nearby.",
        "My alarm somehow switched itself off after an update.",
        "The bus driver stopped for breakfast and everyone just accepted it.",
        "I entered the wrong lecture hall and only realized halfway through.",
        "Google Maps sent me to the opposite side of campus."
    ],

    "I missed a deadline": [
        "I misunderstood the submission timing and thought it was tonight.",
        "My internet disconnected right when I was uploading the file.",
        "The document suddenly became corrupted before submission.",
        "I accidentally submitted the draft version instead of the final version.",
        "I was rushing multiple assignments and mixed up the deadlines."
    ],

    "I skipped class": [
        "I genuinely thought today was still the semester break.",
        "I woke up feeling sick and went back to sleep immediately.",
        "I joined the online link from last week's class by mistake.",
        "I checked the timetable incorrectly and thought the class was cancelled.",
        "I got stuck helping my group finish another assignment."
    ],

    "I forgot about a meeting": [
        "I entered the wrong date into my calendar.",
        "I thought the meeting was scheduled for tomorrow.",
        "My reminder notification never appeared.",
        "I got pulled into another discussion and completely lost track of time.",
        "I mixed up the meeting timing with another subject."
    ],

    "I didn't reply my lecturer": [
        "I opened the email while busy and forgot to respond later.",
        "I thought I had already replied but apparently I only replied in my head.",
        "Your email got buried under multiple assignment notifications.",
        "I was trying to draft a proper response and delayed it too long.",
        "I accidentally archived the email while clearing notifications."
    ],

    "I forgot to study for a test": [
        "I focused so much on another assignment that I completely lost track of the test date.",
        "I thought the test was next week.",
        "My study plan collapsed after one unexpected nap.",
        "I spent hours studying the wrong chapter.",
        "I joined a group study session that somehow became a dinner outing."
    ]
}

# -----------------------------------
# BUTTON
# -----------------------------------
if st.button("Generate Excuse 🎲"):

    selected_excuse = random.choice(excuses[scenario])

    st.success(selected_excuse)

    st.balloons()

# -----------------------------------
# BONUS MODE
# -----------------------------------
st.divider()

if st.checkbox("Enable Dramatic Mode 🎭"):

    dramatic_addons = [
        "It has honestly been a very chaotic week.",
        "Everything that could go wrong somehow went wrong.",
        "I wish I was making this up.",
        "This situation escalated way too quickly.",
        "Even my friends didn't believe me."
    ]

    st.info(random.choice(dramatic_addons))

# -----------------------------------
# FOOTER
# -----------------------------------
st.divider()
st.caption("Built with Streamlit + Python")