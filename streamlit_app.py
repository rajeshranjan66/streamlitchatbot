import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title("Basic chatbot with OpenAI")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def generate_response(input_text):
    model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    st.info(model.invoke(input_text))


with st.form("my_form"):
    text = st.text_area(
        "Ask anything....",
        "",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key which starts with sk-", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
