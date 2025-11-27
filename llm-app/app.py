import streamlit as st
from langchain_google_genai import GoogleGenerativeAI

# API_KEY_HERE = API_KEY_HERE
st.title("Simple LLM App")


def generate_response(input):
    llm = GoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_API_KEY_HERE=API_KEY_HERE
    )
    st.info(llm.invoke(input))


with st.form('my_form'):

    if "API_KEY_HERE" not in st.session_state:
        API_KEY_HERE = st.text_input(
            "Enter your API key:",
            type="password"
        )
        if API_KEY_HERE:
            st.session_state.API_KEY_HERE = API_KEY_HERE
            st.success("API Key saved.")
        else:
            st.warning('Please Enter your API Key', icon='⚠')
    text = st.text_area('Enter Text:', '')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)