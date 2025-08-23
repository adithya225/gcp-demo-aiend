import os
from dotenv import load_dotenv
import google.generativeai as genai 
import streamlit as st

load_dotenv()

def call_llm_api(prompt, temperature=0.7, max_tokens=500) -> str:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text


if __name__=="__main__":
    prompt1="who is the prime minister of United States?"
    # print(call_llm_api(prompt))s
    st.title("welcome to the AI the Intelligence Platform")
    prompt = st.text_input("enter the question here")
    if st.button("send"):
        response = call_llm_api(prompt)
        # while response.text is null:
        #     st.loader("answer generating...")
        print(response )
        st.markdown(response)
    else:
        st.text("hit send button to get the response")
