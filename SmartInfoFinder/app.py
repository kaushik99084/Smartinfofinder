import streamlit as st
import textwrap
from config.settings import APP_NAME, APP_ICON
from services.groq_service import generate_response_stream

from database.connection import engine, Base, SessionLocal
from database import models

from database.crud import (
    create_conversation,
    get_conversations,
    get_messages,
    add_message,
    update_conversation_title,
    delete_conversation,
)

from components.auth import render_auth
from components.styles import load_styles
from components.sidebar import render_sidebar

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# LOAD STYLES
# ==================================================

load_styles()
# ==================================================
# DATABASE INITIALIZATION
# ==================================================

Base.metadata.create_all(bind=engine)


# ==================================================
# SESSION STATE
# ==================================================

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False


# ==================================================
# AUTHENTICATION CHECK
# ==================================================

if not st.session_state.authenticated:

    render_auth()

    st.stop()


# ==================================================
# DATABASE SESSION
# ==================================================

db = SessionLocal()


# ==================================================
# CURRENT USER
# ==================================================

user_id = st.session_state.user_id

user_name = st.session_state.get(
    "user_name",
    "User"
)

user_email = st.session_state.get(
    "user_email",
    ""
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    /* ==============================================
       APPLICATION
       ============================================== */

    .stApp {
        background-color: #f8fafc;
    }


    /* ==============================================
       SIDEBAR
       ============================================== */

    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e5e7eb;
    }

    [data-testid="stSidebarContent"] {
        padding-top: 25px;
    }


    /* ==============================================
       SIDEBAR BUTTONS
       ============================================== */

    [data-testid="stSidebar"] button {
        border-radius: 10px;
        transition: all 0.2s ease;
    }

    [data-testid="stSidebar"] button p {
        font-size: 14px;
    }


    /* ==============================================
       MAIN HEADER
       ============================================== */

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #64748b;
        font-size: 17px;
        margin-bottom: 30px;
    }


    /* ==============================================
       CHAT
       ============================================== */

    .stChatMessage {
        border-radius: 14px;
    }

    .stChatInputContainer {
        border-radius: 14px;
    }


    /* ==============================================
       USER PROFILE
       ============================================== */

    .user-card {
        background-color: #f8fafc;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 10px;
    }

    .user-name {
        font-size: 15px;
        font-weight: 600;
        color: #1f2937;
    }

    .user-email {
        font-size: 12px;
        color: #64748b;
        margin-top: 2px;
    }


    /* ==============================================
       MOBILE
       ============================================== */

    @media (max-width: 768px) {

        .main-title {
            font-size: 30px;
        }

        .subtitle {
            font-size: 14px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# INITIALIZE ACTIVE CHAT
# ==================================================

if "active_chat_id" not in st.session_state:

    conversations = get_conversations(
        db,
        user_id
    )

    if conversations:

        st.session_state.active_chat_id = (
            conversations[0].id
        )

    else:

        conversation = create_conversation(
            db,
            user_id
        )

        st.session_state.active_chat_id = (
            conversation.id
        )


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    # ----------------------------------------------
    # BRAND
    # ----------------------------------------------

    st.markdown(
        "## 🔍 Smart Info Finder"
    )

    st.caption(
        "AI Knowledge Assistant"
    )

    st.markdown("---")


    # ----------------------------------------------
    # USER PROFILE
    # ----------------------------------------------

    st.markdown("### 👤 Profile")

    st.write(user_name)

    if user_email:
        st.caption(user_email)

    st.markdown("---")


    # ----------------------------------------------
    # LOGOUT
    # ----------------------------------------------

    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        keys_to_remove = [
            "authenticated",
            "user_id",
            "user_name",
            "user_email",
            "active_chat_id"
        ]

        for key in keys_to_remove:

            if key in st.session_state:
                del st.session_state[key]

        st.rerun()


    st.markdown("---")


    # ----------------------------------------------
    # NEW CHAT
    # ----------------------------------------------

    if st.button(
        "＋ New Chat",
        use_container_width=True
    ):

        conversation = create_conversation(
            db,
            user_id
        )

        st.session_state.active_chat_id = (
            conversation.id
        )

        st.rerun()


    st.markdown("---")


    # ----------------------------------------------
    # RECENT CHATS
    # ----------------------------------------------

    st.markdown(
        "### 💬 Recent Chats"
    )

    conversations = get_conversations(
        db,
        user_id
    )

    if not conversations:

        st.caption(
            "No conversations yet."
        )

    else:

        for conversation in conversations:

            title = conversation.title

            if not title:
                title = "New Chat"

            if len(title) > 30:
                title = title[:30] + "..."

            if st.button(
                title,
                key=f"conversation_{conversation.id}",
                use_container_width=True
            ):

                st.session_state.active_chat_id = (
                    conversation.id
                )

                st.rerun()


    st.markdown("---")


    # ----------------------------------------------
    # DELETE CURRENT CHAT
    # ----------------------------------------------

    if st.button(
        "🗑️ Delete Current Chat",
        use_container_width=True
    ):

        deleted = delete_conversation(
            db,
            st.session_state.active_chat_id,
            user_id
        )

        if deleted:

            conversation = create_conversation(
                db,
                user_id
            )

            st.session_state.active_chat_id = (
                conversation.id
            )

            st.rerun()


    st.markdown("---")


    # ----------------------------------------------
    # LANGUAGES
    # ----------------------------------------------

    st.markdown(
        "### 🌐 Languages"
    )

    st.caption("🇬🇧 English")
    st.caption("🇮🇳 Hindi")
    st.caption("🟠 Punjabi")
    st.caption("🌍 Other languages")

    st.markdown("---")


    # ----------------------------------------------
    # VERSION
    # ----------------------------------------------

    st.caption(
        "Smart Info Finder v2.0"
    )
# ==================================================
# GET ACTIVE CHAT
# ==================================================

active_chat_id = (
    st.session_state.active_chat_id
)


# ==================================================
# GET CHAT MESSAGES
# ==================================================

messages_db = get_messages(
    db,
    active_chat_id,
    user_id
)


# ==================================================
# HEADER
# ==================================================

st.markdown(
    '<div class="main-title">'
    '🔍 Smart Info Finder'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your intelligent multilingual AI assistant'
    '</div>',
    unsafe_allow_html=True
)


# ==================================================
# WELCOME SCREEN
# ==================================================

if not messages_db:

    st.info(
        "👋 Welcome to Smart Info Finder! "
        "Ask questions, learn new concepts, "
        "or get help with technical problems."
    )

    st.markdown("### 💡 Try asking")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("### 🤖 AI")

        st.caption(
            "What is artificial intelligence?"
        )

    with col2:

        st.markdown("### 💻 Programming")

        st.caption(
            "Explain Python functions."
        )

    with col3:

        st.markdown("### 📚 Education")

        st.caption(
            "What is an operating system?"
        )


# ==================================================
# DISPLAY CHAT HISTORY
# ==================================================

for message in messages_db:

    with st.chat_message(message.role):

        st.markdown(message.content)


# ==================================================
# USER INPUT
# ==================================================

prompt = st.chat_input(
    "Ask Smart Info Finder anything..."
)


if prompt:

    # ----------------------------------------------
    # SAVE USER MESSAGE
    # ----------------------------------------------

    add_message(
        db,
        active_chat_id,
        user_id,
        "user",
        prompt
    )


    # ----------------------------------------------
    # CREATE CHAT TITLE
    # ----------------------------------------------

    current_conversation = (
        db.query(models.Conversation)
        .filter(
            models.Conversation.id == active_chat_id,
            models.Conversation.user_id == user_id
        )
        .first()
    )


    if current_conversation:

        if current_conversation.title == "New Chat":

            title = prompt.strip()

            if len(title) > 40:

                title = title[:40] + "..."

            update_conversation_title(
                db,
                active_chat_id,
                user_id,
                title
            )


    # ----------------------------------------------
    # DISPLAY USER MESSAGE
    # ----------------------------------------------

    with st.chat_message("user"):

        st.markdown(prompt)


    # ----------------------------------------------
    # GET UPDATED HISTORY
    # ----------------------------------------------

    updated_messages = get_messages(
        db,
        active_chat_id,
        user_id
    )


    conversation_history = []

    for message in updated_messages:

        conversation_history.append(
            {
                "role": message.role,
                "content": message.content
            }
        )


    # ----------------------------------------------
    # GENERATE AI RESPONSE
    # ----------------------------------------------

    with st.chat_message("assistant"):

        try:

            answer = st.write_stream(
                generate_response_stream(
                    conversation_history
                )
            )


            # --------------------------------------
            # SAVE AI RESPONSE
            # --------------------------------------

            add_message(
                db,
                active_chat_id,
                user_id,
                "assistant",
                answer
            )


        except Exception as error:

            st.error(
                "Something went wrong. "
                "Please try again."
            )

            st.caption(
                f"Error: {error}"
            )


# ==================================================
# CLOSE DATABASE
# ==================================================

db.close()