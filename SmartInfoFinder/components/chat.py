import streamlit as st


def display_chat_history():

    active_chat = st.session_state.active_chat

    messages = st.session_state.chats[
        active_chat
    ]["messages"]

    for message in messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])


def add_message(role, content):

    active_chat = st.session_state.active_chat

    st.session_state.chats[
        active_chat
    ]["messages"].append({
        "role": role,
        "content": content
    })


def update_chat_title():

    active_chat = st.session_state.active_chat

    chat = st.session_state.chats[active_chat]

    messages = chat["messages"]

    if chat["title"] == "New Chat" and messages:

        # Find the first user message
        for message in messages:

            if message["role"] == "user":

                title = message["content"].strip()

                # Keep sidebar title short
                if len(title) > 30:
                    title = title[:30] + "..."

                chat["title"] = title

                break