import streamlit as st
from langchain_google_genai import GoogleGenerativeAI

st.title("Simple LLM App")


def generate_response(input):
    llm = GoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key
    )
    st.info(llm.invoke(input))


with st.form('my_form'):

    if "api_key" not in st.session_state:
        api_key = st.text_input(
            "Enter your API key:",
            type="password"
        )
        if api_key:
            st.session_state.api_key = api_key
            st.success("API Key saved.")
        else:
            st.warning('Please Enter your API Key', icon='⚠')
    text = st.text_area('Enter Text:', '')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)