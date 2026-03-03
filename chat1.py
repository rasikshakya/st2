import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("💬 Gemini Chatbot with Memory")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    role, content = msg
    if role == "user":
        st.markdown(f"**You:** {content}")
    else:
        st.markdown(f"**Gemini:** {content}")

# User input
user_input = st.text_input("Type your message:")

if st.button("Send"):
    if user_input:
        st.session_state.messages.append(("user", user_input))

        response = model.generate_content(
            [m[1] for m in st.session_state.messages]
        )

        st.session_state.messages.append(("assistant", response.text))
        st.experimental_rerun()
