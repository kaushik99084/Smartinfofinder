import streamlit as st


def render_home():

    st.markdown(
        """
        <div class="home-container">

            <div class="status-badge">
                <span class="status-dot"></span>
                AI Assistant Online
            </div>

            <div class="home-icon">
                🔍
            </div>

            <h1 class="home-title">
                Smart Info Finder
            </h1>

            <p class="home-subtitle">
                Your intelligent multilingual AI knowledge assistant
            </p>

            <p class="home-description">
                Ask questions, learn new concepts, solve programming problems,
                and explore ideas with AI.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-title">
            ✨ What can I help you with today?
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🤖</div>
                <h3>Artificial Intelligence</h3>
                <p>
                    Understand AI, machine learning, deep learning
                    and modern technologies.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Ask about AI →",
            key="home_ai",
            use_container_width=True
        ):
            st.session_state.suggested_prompt = (
                "What is artificial intelligence?"
            )
            st.rerun()

    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">💻</div>
                <h3>Programming</h3>
                <p>
                    Learn programming concepts, debug code,
                    and solve technical problems.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Ask about Programming →",
            key="home_programming",
            use_container_width=True
        ):
            st.session_state.suggested_prompt = (
                "Explain Python functions with examples."
            )
            st.rerun()

    with col3:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">📚</div>
                <h3>Education</h3>
                <p>
                    Study concepts, prepare for exams,
                    and understand difficult topics.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Ask about Education →",
            key="home_education",
            use_container_width=True
        ):
            st.session_state.suggested_prompt = (
                "Explain operating systems in simple language."
            )
            st.rerun()

    st.markdown(
        """
        <div class="tips-card">

            <div class="tips-icon">
                💡
            </div>

            <div>
                <strong>Tip</strong>
                <p>
                    You can ask your question in English, Hindi,
                    Punjabi, or another language.
                </p>
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )