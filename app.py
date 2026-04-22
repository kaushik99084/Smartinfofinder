import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("API key error check .env file")
    st.stop()

client = Groq(api_key=api_key)

# Page Config
st.set_page_config(page_title="Smart Info Finder", page_icon="🔍")

# Custom Styling
st.markdown("""
<style>
    .stApp {
        background-color: #f0f2f6;
    }
    .stApp h1 {
        color: #1E3A8A;
        text-align: center;
    }
    .stChatMessage p {
        color: #000000 !important;
    }
    .stChatMessage{
        background-color: #FFFFFF;
    }
    .stMarkdown .st-emotion-cache-r7ut5z p{
         color: #000000 !important;   
    }
    .st-emotion-cache-r7ut5z > ul, .st-emotion-cache-r7ut5z > ol{
            color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🔍 Smart Info Finder")
st.markdown("""
    <h4 style='text-align: center; color: #1E3A8A; margin-top: -15px;'>
        You can choose any language you want 
    </h4>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("In which language you want answer?")
# Sidebar
with st.sidebar:
    st.markdown("### ⚙️ Controls")
    
    if st.button("🗑️ Clear Chat History", use_container_width=True, type="secondary"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("**Supported Languages:**")
    st.markdown("• English\n• Hindi\n• Punjabi\n• Any other language")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your question here..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Strong System Prompt for Language Control
    system_prompt = """
    Tu Smart Info Finder hai, ek bahut helpful aur accurate AI assistant.
    User jis language mein baat kare ya jis language mein jawab maange, 
    usi language mein pura jawab dena hai. Kabhi bhi mix mat karna.
    
    - Hindi mein bole → Hindi mein jawab
    - Punjabi mein bole → Punjabi (Gurmukhi) mein jawab
    - English mein bole → English mein jawab
    - Koi aur language bole → usi mein jawab
    
    Hamesha natural, clear aur informative jawab dena.
    """

    # Prepare messages
    messages = [{"role": "system", "content": system_prompt}]
    for msg in st.session_state.messages:
        messages.append({"role": msg["role"], "content": msg["content"]})

    # Get response
    with st.chat_message("assistant"):
        with st.spinner("Processing ..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=messages,
                    temperature=0.7,
                    max_tokens=1024
                )
                answer = response.choices[0].message.content
                st.markdown(answer)
                
                # Save assistant response
                st.session_state.messages.append({"role": "assistant", "content": answer})
                
            except Exception as e:
                st.error(f"Something went wrong {e}")