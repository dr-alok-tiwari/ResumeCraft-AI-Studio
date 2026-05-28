"""
About Developer page for ResumeCraft AI Studio.

This page is intentionally self-contained so that it works on Streamlit Cloud
without any external image hosting or paid API dependency.
"""

import streamlit as st


DEVELOPER_PHOTO_B64 = """
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
""".strip()


st.set_page_config(
    page_title="About Developer | ResumeCraft AI Studio",
    page_icon="👨‍🏫",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "ResumeCraft AI Studio | Copyright@ Dr Alok Tiwari | Goa Institute of Management",
    },
)


def render_about_developer() -> None:
    """Render the About Developer section."""
    photo_uri = f"data:image/jpeg;base64,{DEVELOPER_PHOTO_B64}"

    st.markdown(
        """
        <style>
            .about-hero {
                background: linear-gradient(135deg, rgba(108,99,255,0.18), rgba(78,205,196,0.14));
                border: 1px solid rgba(108,99,255,0.28);
                border-radius: 24px;
                padding: 2.2rem;
                margin-bottom: 1.5rem;
                box-shadow: 0 14px 45px rgba(0,0,0,0.22);
            }
            .developer-photo {
                width: 230px;
                max-width: 100%;
                border-radius: 22px;
                border: 3px solid rgba(78,205,196,0.8);
                box-shadow: 0 16px 36px rgba(0,0,0,0.35);
            }
            .name-title {
                font-size: 2.2rem;
                font-weight: 900;
                color: #6C63FF;
                margin-bottom: 0.2rem;
                line-height: 1.15;
            }
            .subtitle {
                font-size: 1.05rem;
                color: #4ECDC4;
                font-weight: 700;
                margin-bottom: 0.75rem;
            }
            .body-text {
                color: #E5E7EB;
                font-size: 1rem;
                line-height: 1.75;
            }
            .info-chip {
                display: inline-block;
                padding: 0.42rem 0.72rem;
                margin: 0.22rem 0.24rem 0.22rem 0;
                border-radius: 999px;
                background: rgba(108,99,255,0.14);
                border: 1px solid rgba(108,99,255,0.25);
                color: #E5E7EB;
                font-size: 0.9rem;
                font-weight: 600;
            }
            .section-card {
                background: rgba(17,24,39,0.92);
                border: 1px solid rgba(78,205,196,0.18);
                border-radius: 18px;
                padding: 1.3rem;
                height: 100%;
                box-shadow: 0 8px 24px rgba(0,0,0,0.18);
            }
            .section-card h3 {
                color: #4ECDC4;
                margin-top: 0;
                font-size: 1.25rem;
            }
            .copyright-box {
                text-align: center;
                padding: 1.2rem;
                margin-top: 1.5rem;
                border-radius: 16px;
                background: linear-gradient(135deg, rgba(108,99,255,0.18), rgba(78,205,196,0.14));
                border: 1px solid rgba(108,99,255,0.28);
            }
            a {
                color: #4ECDC4 !important;
                text-decoration: none;
                font-weight: 700;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="about-hero">
            <div style="display:flex; gap:2rem; align-items:center; flex-wrap:wrap;">
                <div style="flex:0 0 250px; text-align:center;">
                    <img class="developer-photo" src="{photo_uri}" alt="Dr Alok Tiwari">
                </div>
                <div style="flex:1; min-width:300px;">
                    <div class="name-title">Dr Alok Tiwari</div>
                    <div class="subtitle">Assistant Professor – Big Data Analytics | Goa Institute of Management, Goa</div>
                    <p class="body-text">
                        Dr Alok Tiwari develops learning-focused, no-cost AI and analytics tools for management education,
                        student mentoring, faculty development, executive training, and applied decision support. His work
                        connects machine learning, healthcare analytics, data visualization, responsible AI, and practical
                        business analytics with classroom-ready applications.
                    </p>
                    <div>
                        <span class="info-chip">AI & Machine Learning</span>
                        <span class="info-chip">Healthcare Analytics</span>
                        <span class="info-chip">Data Visualization</span>
                        <span class="info-chip">Student Mentoring</span>
                        <span class="info-chip">Responsible AI</span>
                    </div>
                    <p class="body-text" style="margin-top:1rem;">
                        🌐 Portfolio: <a href="https://dr-alok-tiwari.github.io/" target="_blank">dr-alok-tiwari.github.io</a>
                    </p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="section-card">
                <h3>About this Studio</h3>
                <p class="body-text">
                    <strong>ResumeCraft AI Studio</strong> is designed to help students, early-career professionals,
                    and academic applicants build, evaluate, improve, and export ATS-ready resumes without depending
                    on paid AI APIs. The tool prioritizes truthful claims, transparent scoring, practical feedback,
                    and local-first processing.
                </p>
                <p class="body-text">
                    The studio combines resume parsing, rule-based ATS scoring, job-description matching,
                    bullet-point improvement, guided resume building, quality checks, and export support in one
                    Streamlit-based interface.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="section-card">
                <h3>Design Philosophy</h3>
                <p class="body-text">
                    The app is intentionally built as a <strong>no-cost, no-API, education-friendly</strong> system.
                    It avoids black-box resume promises and instead gives users visible criteria, practical warnings,
                    and review checkpoints so that each resume remains accurate, ethical, and verifiable.
                </p>
                <p class="body-text">
                    It supports career-readiness workshops, placement preparation, classroom demonstrations,
                    and individual resume improvement while keeping user data within the active session.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### Academic and Professional Focus")
    st.markdown(
        """
        - Artificial Intelligence, Machine Learning, Deep Learning, and Computer Vision
        - Healthcare Analytics, medical imaging AI, and decision-support applications
        - Big Data Analytics, MLOps, data visualization, and dashboard-based storytelling
        - AI-enabled pedagogy, executive education, faculty development, and student mentoring
        - Responsible, transparent, and context-aware use of AI in academic and professional settings
        """
    )

    st.markdown(
        """
        <div class="copyright-box">
            <div style="font-size:1.12rem; font-weight:800; color:#4ECDC4;">
                Copyright@ Dr Alok Tiwari
            </div>
            <div style="color:#CBD5E1; margin-top:0.35rem;">
                ResumeCraft AI Studio | Goa Institute of Management | Built with Python and Streamlit
            </div>
            <div style="color:#94A3B8; font-size:0.88rem; margin-top:0.3rem;">
                All content is intended for educational and career-readiness use. No paid APIs required.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


render_about_developer()
