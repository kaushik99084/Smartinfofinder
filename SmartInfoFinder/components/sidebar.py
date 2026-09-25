import streamlit as st

from database.connection import SessionLocal

from database.crud import (
    get_conversations,
    create_conversation,
    update_conversation_title,
    delete_conversation,
)


def render_sidebar():

    db = SessionLocal()

    try:

        with st.sidebar:

            # ==================================================
            # BRAND
            # ==================================================

            st.markdown(
                "# 🔍 Smart Info Finder"
            )

            st.caption(
                "AI Knowledge Assistant"
            )

            st.markdown("---")

            # ==================================================
            # NEW CHAT
            # ==================================================

            if st.button(
                "＋ New Chat",
                use_container_width=True,
                type="primary"
            ):

                conversation = create_conversation(db)

                st.session_state.active_chat_id = conversation.id

                st.rerun()

            st.markdown("### 💬 Recent Chats")

            # ==================================================
            # GET CONVERSATIONS
            # ==================================================

            conversations = get_conversations(db)

            if not conversations:

                st.info(
                    "No conversations yet.\n\n"
                    "Click **＋ New Chat** to start."
                )

            else:

                for conversation in conversations:

                    conversation_id = conversation.id

                    title = (
                        conversation.title
                        or "New Chat"
                    )

                    # Shorten long titles

                    if len(title) > 30:

                        title = title[:30] + "..."

                    # ==================================================
                    # CHAT ROW
                    # ==================================================

                    col1, col2 = st.columns(
                        [5, 1],
                        gap="small"
                    )

                    # --------------------------------------------------
                    # OPEN CHAT
                    # --------------------------------------------------

                    with col1:

                        if st.button(
                            f"💬 {title}",
                            key=f"chat_{conversation_id}",
                            use_container_width=True
                        ):

                            st.session_state.active_chat_id = (
                                conversation_id
                            )

                            st.rerun()

                    # --------------------------------------------------
                    # CHAT OPTIONS
                    # --------------------------------------------------

                    with col2:

                        with st.popover("⋮"):

                            st.markdown(
                                "### Chat Options"
                            )

                            # ==================================================
                            # RENAME
                            # ==================================================

                            new_title = st.text_input(
                                "Chat name",
                                value=conversation.title or "New Chat",
                                key=f"rename_input_{conversation_id}"
                            )

                            if st.button(
                                "✏️ Rename",
                                key=f"rename_{conversation_id}",
                                use_container_width=True
                            ):

                                new_title = new_title.strip()

                                if new_title:

                                    update_conversation_title(
                                        db,
                                        conversation_id,
                                        new_title
                                    )

                                    st.success(
                                        "Chat renamed!"
                                    )

                                    st.rerun()

                            st.markdown("---")

                            # ==================================================
                            # DELETE
                            # ==================================================

                            if st.button(
                                "🗑️ Delete",
                                key=f"delete_{conversation_id}",
                                use_container_width=True
                            ):

                                delete_conversation(
                                    db,
                                    conversation_id
                                )

                                # If active chat was deleted

                                if (
                                    st.session_state.get(
                                        "active_chat_id"
                                    )
                                    == conversation_id
                                ):

                                    new_chat = create_conversation(
                                        db
                                    )

                                    st.session_state.active_chat_id = (
                                        new_chat.id
                                    )

                                st.rerun()

            # ==================================================
            # SETTINGS
            # ==================================================

            st.markdown("---")

            st.markdown(
                "### ⚙️ Settings"
            )

            st.caption(
                "🌐 Multilingual AI"
            )

            st.caption(
                "🇬🇧 English"
            )

            st.caption(
                "🇮🇳 Hindi"
            )

            st.caption(
                "🟠 Punjabi"
            )

            st.caption(
                "🌍 Other languages"
            )

            # ==================================================
            # FOOTER
            # ==================================================

            st.markdown("---")

            st.caption(
                "Smart Info Finder"
            )

            st.caption(
                "AI Assistant v2.0"
            )

    finally:

        db.close()