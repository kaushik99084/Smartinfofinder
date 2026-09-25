import streamlit as st

from database.connection import SessionLocal
from services.auth_service import (
    create_user,
    authenticate_user
)


def render_auth():

    db = SessionLocal()

    try:

        # ==================================================
        # HEADER
        # ==================================================

        st.markdown(
            """
            # 🔍 Smart Info Finder

            **Your intelligent multilingual AI assistant**
            """
        )

        st.markdown("---")


        # ==================================================
        # CENTER AUTH SECTION
        # ==================================================

        left, center, right = st.columns(
            [1, 2, 1]
        )

        with center:

            # ==================================================
            # LOGIN / REGISTER
            # ==================================================

            mode = st.radio(
                "Authentication",
                ["Login", "Create Account"],
                horizontal=True,
                label_visibility="collapsed"
            )

            st.markdown("")


            # ==================================================
            # LOGIN
            # ==================================================

            if mode == "Login":

                st.markdown(
                    "## 👋 Welcome Back"
                )

                st.caption(
                    "Login to continue to Smart Info Finder."
                )

                st.markdown("")


                # ----------------------------------------------
                # EMAIL
                # ----------------------------------------------

                email = st.text_input(
                    "📧 Email",
                    placeholder="you@example.com",
                    key="login_email"
                )


                # ----------------------------------------------
                # PASSWORD
                # ----------------------------------------------

                password = st.text_input(
                    "🔒 Password",
                    type="password",
                    placeholder="Enter your password",
                    key="login_password"
                )

                st.markdown("")


                # ----------------------------------------------
                # LOGIN BUTTON
                # ----------------------------------------------

                if st.button(
                    "🔐 Login",
                    use_container_width=True,
                    type="primary"
                ):

                    email = email.strip().lower()

                    # ------------------------------------------
                    # VALIDATION
                    # ------------------------------------------

                    if not email:

                        st.error(
                            "Please enter your email."
                        )

                    elif not password:

                        st.error(
                            "Please enter your password."
                        )

                    elif (
                        "@" not in email
                        or "." not in email.split("@")[-1]
                    ):

                        st.error(
                            "Please enter a valid email address."
                        )

                    else:

                        # --------------------------------------
                        # AUTHENTICATE USER
                        # --------------------------------------

                        user = authenticate_user(
                            db,
                            email,
                            password
                        )


                        if user:

                            # ----------------------------------
                            # SAVE USER SESSION
                            # ----------------------------------

                            st.session_state.user_id = user.id

                            st.session_state.user_name = (
                                user.name
                            )

                            st.session_state.user_email = (
                                user.email
                            )

                            st.session_state.authenticated = True


                            st.success(
                                "Login successful!"
                            )

                            st.rerun()


                        else:

                            st.error(
                                "Invalid email or password."
                            )


            # ==================================================
            # CREATE ACCOUNT
            # ==================================================

            else:

                st.markdown(
                    "## 🚀 Create Account"
                )

                st.caption(
                    "Create your account to get started."
                )

                st.markdown("")


                # ----------------------------------------------
                # NAME
                # ----------------------------------------------

                name = st.text_input(
                    "👤 Full Name",
                    placeholder="Your name",
                    key="register_name"
                )


                # ----------------------------------------------
                # EMAIL
                # ----------------------------------------------

                email = st.text_input(
                    "📧 Email",
                    placeholder="you@example.com",
                    key="register_email"
                )


                # ----------------------------------------------
                # PASSWORD
                # ----------------------------------------------

                password = st.text_input(
                    "🔒 Password",
                    type="password",
                    placeholder="Create a password",
                    key="register_password"
                )


                # ----------------------------------------------
                # CONFIRM PASSWORD
                # ----------------------------------------------

                confirm_password = st.text_input(
                    "🔒 Confirm Password",
                    type="password",
                    placeholder="Repeat your password",
                    key="register_confirm_password"
                )

                st.markdown("")


                # ----------------------------------------------
                # CREATE ACCOUNT BUTTON
                # ----------------------------------------------

                if st.button(
                    "✨ Create Account",
                    use_container_width=True,
                    type="primary"
                ):

                    name = name.strip()
                    email = email.strip().lower()


                    # ------------------------------------------
                    # VALIDATION
                    # ------------------------------------------

                    if not name:

                        st.error(
                            "Please enter your full name."
                        )

                    elif not email:

                        st.error(
                            "Please enter your email."
                        )

                    elif (
                        "@" not in email
                        or "." not in email.split("@")[-1]
                    ):

                        st.error(
                            "Please enter a valid email address."
                        )

                    elif not password:

                        st.error(
                            "Please enter a password."
                        )

                    elif len(password) < 8:

                        st.error(
                            "Password must contain at least 8 characters."
                        )

                    elif password != confirm_password:

                        st.error(
                            "Passwords do not match."
                        )

                    else:

                        # --------------------------------------
                        # CREATE USER
                        # --------------------------------------

                        user = create_user(
                            db,
                            name,
                            email,
                            password
                        )


                        if user:

                            st.success(
                                "Account created successfully! "
                                "Please login."
                            )

                        else:

                            st.error(
                                "An account with this email "
                                "already exists."
                            )

    finally:

        db.close()