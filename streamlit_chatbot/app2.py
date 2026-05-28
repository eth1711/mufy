import streamlit as st
from google import genai

# -----------------------------------
# PAGE SETTINGS
# -----------------------------------
st.set_page_config(
    page_title="AI Excuse Generator",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------------
# GEMINI CLIENT
# -----------------------------------
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# -----------------------------------
# TITLE
# -----------------------------------
st.title("🤖 AI Excuse Generator")
st.write("Generate ridiculous AI-powered excuses.")

# -----------------------------------
# USER INPUT
# -----------------------------------
scenario = st.text_area(
    "Describe your situation:",
    placeholder="Example: I forgot to submit my assignment because..."
)

# -----------------------------------
# GENERATE BUTTON
# -----------------------------------
if st.button("Generate Funny AI Excuse 🚀"):

    if scenario.strip() == "":
        st.warning("Please enter a scenario.")

    else:

        with st.spinner("Generating excuse..."):

            prompt = f"""
            You are a funny excuse generator.

            Generate ONE short funny excuse based on this situation:

            {scenario}

            Rules:
            - Keep it under 2 sentences
            - Make it funny
            - Family friendly
            - Sound creative and ridiculous
            """

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            st.success(response.text)

            st.balloons()

# -----------------------------------
# FOOTER
# -----------------------------------
st.divider()
st.caption("Powered by Gemini 2.5 Flash + Streamlit") 