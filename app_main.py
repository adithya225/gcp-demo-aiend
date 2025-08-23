import os
from dotenv import load_dotenv
import google.generativeai as genai 
import streamlit as st

load_dotenv()

# Configure the Generative AI client at the start
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("`GOOGLE_API_KEY` not found in environment variables. Please set it in your .env file.")
        st.stop()
    genai.configure(api_key=api_key)
except Exception as e:
    st.error(f"Error configuring Generative AI: {e}")
    st.stop()

def call_llm_api(prompt: str, temperature: float = 0.7, max_tokens: int = 500) -> str:
    """Calls the Gemini API and returns the response text."""
    try:
        # Use a valid and current model name
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        generation_config = genai.types.GenerationConfig(
            temperature=temperature,
            max_output_tokens=max_tokens
        )
        response = model.generate_content(f"description: act as a expert in all areas and generate response for the prompt in detailed way. here is the user prompt: {prompt}", generation_config=generation_config)
        return response.text
    except Exception as e:
        st.error(f"An error occurred while calling the API: {e}")
        return ""

if __name__=="__main__":
    st.title("AI Intelligence Platform")
    prompt = st.text_input("Enter your question here:")

    if st.button("Send") and prompt:
        with st.spinner("Generating response for your prompt please wait till then..."):
            response = call_llm_api(prompt)
            if response:
                st.markdown(response)

