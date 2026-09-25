import streamlit as st


def load_styles():

    st.markdown(
        """
        <style>

        /* =====================================================
           GLOBAL
        ===================================================== */

        .stApp {

            background:
                radial-gradient(
                    circle at 10% 10%,
                    rgba(99, 102, 241, 0.08),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 90% 20%,
                    rgba(59, 130, 246, 0.08),
                    transparent 30%
                ),
                #f8fafc;

        }


        .block-container {

            max-width: 1200px;

            padding-top: 2rem;

            padding-bottom: 8rem;

        }


        /* =====================================================
           SIDEBAR
        ===================================================== */

        section[data-testid="stSidebar"] {

            background:
                linear-gradient(
                    180deg,
                    #ffffff 0%,
                    #f8fafc 100%
                );

            border-right:
                1px solid #e2e8f0;

        }


        section[data-testid="stSidebar"] .block-container {

            padding-top: 2rem;

            padding-left: 1.2rem;

            padding-right: 1.2rem;

        }


        /* Sidebar buttons */

        section[data-testid="stSidebar"]
        .stButton > button {

            border-radius: 12px;

            border: 1px solid #e2e8f0;

            background: white;

            color: #1e293b;

            font-weight: 600;

            transition: all 0.2s ease;

        }


        section[data-testid="stSidebar"]
        .stButton > button:hover {

            transform: translateY(-2px);

            border-color: #93c5fd;

            box-shadow:
                0 8px 20px
                rgba(37, 99, 235, 0.10);

        }


        /* =====================================================
           HOME HEADER
        ===================================================== */

        .home-container {

            text-align: center;

            padding:
                45px 20px 30px 20px;

        }


        .home-icon {

            font-size: 58px;

            margin-bottom: 10px;

        }


        .home-title {

            font-size: 42px;

            font-weight: 800;

            margin: 0;

            letter-spacing: -1px;

            background:
                linear-gradient(
                    90deg,
                    #1e3a8a,
                    #4f46e5,
                    #2563eb
                );

            -webkit-background-clip: text;

            -webkit-text-fill-color: transparent;

        }


        .home-subtitle {

            font-size: 20px;

            font-weight: 500;

            color: #64748b;

            margin-top: 10px;

        }


        .home-description {

            max-width: 650px;

            margin: 12px auto;

            font-size: 15px;

            line-height: 1.7;

            color: #64748b;

        }


        /* =====================================================
           ONLINE STATUS
        ===================================================== */

        .status-badge {

            display: inline-flex;

            align-items: center;

            gap: 8px;

            padding: 7px 14px;

            border-radius: 30px;

            background: #ecfdf5;

            color: #047857;

            font-size: 13px;

            font-weight: 600;

            border:
                1px solid #a7f3d0;

        }


        .status-dot {

            width: 8px;

            height: 8px;

            border-radius: 50%;

            background: #10b981;

            display: inline-block;

            box-shadow:
                0 0 8px
                rgba(16, 185, 129, 0.6);

        }


        /* =====================================================
           HERO
        ===================================================== */

        .hero-card {

            margin-top: 25px;

            padding: 35px;

            border-radius: 24px;

            background:
                linear-gradient(
                    135deg,
                    #eef2ff,
                    #eff6ff
                );

            border:
                1px solid #dbeafe;

            box-shadow:
                0 10px 35px
                rgba(15, 23, 42, 0.06);

            text-align: center;

        }


        .hero-title {

            font-size: 28px;

            font-weight: 750;

            color: #1e293b;

            margin-bottom: 8px;

        }


        .hero-text {

            color: #64748b;

            font-size: 16px;

        }


        /* =====================================================
           SECTION TITLE
        ===================================================== */

        .section-title {

            font-size: 23px;

            font-weight: 700;

            color: #1f2937;

            margin:
                25px 0 18px 0;

        }


        /* =====================================================
           FEATURE CARDS
        ===================================================== */

        .feature-card {

            min-height: 180px;

            padding: 25px;

            border-radius: 20px;

            background: white;

            border:
                1px solid #e5e7eb;

            box-shadow:
                0 8px 25px
                rgba(15, 23, 42, 0.06);

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease;

        }


        .feature-card:hover {

            transform:
                translateY(-5px);

            box-shadow:
                0 15px 35px
                rgba(15, 23, 42, 0.10);

        }


        .feature-icon {

            font-size: 38px;

            margin-bottom: 12px;

        }


        .feature-card h3 {

            font-size: 18px;

            color: #1f2937;

            margin-bottom: 10px;

        }


        .feature-card p {

            color: #64748b;

            font-size: 14px;

            line-height: 1.6;

        }


        /* =====================================================
           TIPS
        ===================================================== */

        .tips-card {

            display: flex;

            align-items: center;

            gap: 15px;

            margin-top: 30px;

            padding: 18px 22px;

            border-radius: 16px;

            background: #eff6ff;

            border:
                1px solid #dbeafe;

        }


        .tips-icon {

            font-size: 28px;

        }


        /* =====================================================
           CHAT INPUT
        ===================================================== */

        div[data-testid="stChatInput"] {

            background: white;

            border-radius: 18px;

            box-shadow:
                0 10px 35px
                rgba(15, 23, 42, 0.12);

        }


        div[data-testid="stChatInput"] textarea {

            font-size: 15px;

        }


        /* =====================================================
           CHAT MESSAGES
        ===================================================== */

        div[data-testid="stChatMessage"] {

            border-radius: 18px;

            padding: 12px;

        }


        /* =====================================================
           BUTTONS
        ===================================================== */

        .stButton > button {

            border-radius: 12px;

            font-weight: 600;

            transition: all 0.2s ease;

        }


        .stButton > button:hover {

            transform:
                translateY(-2px);

            box-shadow:
                0 8px 20px
                rgba(15, 23, 42, 0.08);

        }


        /* =====================================================
           MOBILE
        ===================================================== */

        @media (max-width: 768px) {

            .block-container {

                padding-left: 1rem;

                padding-right: 1rem;

            }


            .home-title {

                font-size: 32px;

            }


            .home-subtitle {

                font-size: 17px;

            }


            .hero-card {

                padding: 25px 18px;

            }


            .hero-title {

                font-size: 23px;

            }

        }

        </style>
        """,
        unsafe_allow_html=True
    )