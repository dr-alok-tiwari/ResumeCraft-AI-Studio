"""
ResumeCraft AI Studio - Privacy, About Developer, and Limitations Page Content
"""

PRIVACY_CONTENT = """
## 👨‍🏫 About the Developer

**Dr Alok Tiwari**  
Assistant Professor – Big Data Analytics  
Goa Institute of Management, Goa

Dr Alok Tiwari develops learning-focused, no-cost AI and analytics tools for management education, student mentoring, faculty development, executive training, and applied decision support. His work connects machine learning, healthcare analytics, data visualization, responsible AI, and practical business analytics with classroom-ready applications.

**Academic and professional focus areas:**

- Artificial Intelligence, Machine Learning, Deep Learning, and Computer Vision
- Healthcare Analytics, medical imaging AI, and decision-support applications
- Big Data Analytics, MLOps, dashboarding, and data storytelling
- AI-enabled pedagogy, executive education, and student mentoring
- Responsible, transparent, and context-aware use of AI

**Portfolio:** [dr-alok-tiwari.github.io](https://dr-alok-tiwari.github.io/)

> **Copyright@ Dr Alok Tiwari**  
> ResumeCraft AI Studio | Goa Institute of Management | Built with Python and Streamlit

---

## 🎯 About ResumeCraft AI Studio

**ResumeCraft AI Studio** helps students, early-career professionals, and academic applicants build, evaluate, improve, and export ATS-ready resumes without depending on paid AI APIs. The app prioritizes truthful claims, transparent scoring, practical feedback, and local-first processing.

The studio includes resume parsing, rule-based ATS scoring, job-description matching, bullet-point improvement, guided resume building, resume quality checks, and export support in a single Streamlit interface.

---

## 🔒 Privacy, Safety & Limitations

### Data Processing

**How your data is processed:**

> ResumeCraft AI Studio processes uploaded files and pasted text within the active app session.  
> The app does not depend on paid AI APIs or external resume-scoring services.

- ✅ Resume parsing uses Python libraries
- ✅ Scoring and analysis are rule-based and transparent
- ✅ No API key is required
- ✅ Files are not saved unless the user explicitly downloads/exports them
- ✅ Session data is cleared when the browser session ends

### What This App Does NOT Do

- ❌ It does NOT send resumes to OpenAI, Gemini, Claude, or other paid AI APIs
- ❌ It does NOT require account creation or login
- ❌ It does NOT use paid resume-parsing APIs
- ❌ It does NOT tell users to claim skills they do not have
- ❌ It does NOT replace human judgment, mentoring, or final resume review

### Recommendation

> **Avoid uploading highly sensitive personal data** such as government IDs, financial details, or sensitive medical information unless strictly necessary for your resume. A resume should contain professional information only.

---

## 📊 How ATS Scoring Works

The ATS scoring system is **fully rule-based and transparent**:

| Section | Max Points | Method |
|---|---:|---|
| Contact Information | 10 | Regex detection of email, phone, LinkedIn |
| Professional Summary | 10 | Presence, length, and action verb check |
| Education | 10 | Degree keywords and date presence |
| Skills | 15 | Skill count and technical-tool detection |
| Experience / Projects | 20 | Bullet count, dates, organization names |
| Action Verbs | 10 | Match against a curated verb list |
| Quantified Achievements | 10 | Regex patterns for numbers and percentages |
| ATS Formatting | 10 | Section heading detection and symbol check |
| Length & Readability | 5 | Word count range check |

**No generative AI is used for scoring.** All criteria are openly defined so users can understand why a score was assigned.

---

## 🎯 Job Description Matching

The JD matcher uses:

- **TF-IDF vectorization** and cosine similarity through scikit-learn
- **Keyword extraction** from the job description
- **Skill dictionary matching** using locally defined skill lists

**Important:** The app should never be used to add false claims. Missing skills should be treated as:

- *Verify before adding* — confirm that you actually have the skill first
- *Learn before claiming* — upskill before listing it on the resume

---

## ⚠️ Known Limitations

1. **PDF parsing quality** depends on how the PDF was created. Scanned/image-only PDFs may not parse well without OCR.
2. **Name detection** is heuristic and may not work perfectly for non-standard formatting.
3. **Section detection** depends on recognizable headings. Unconventional headings may not be detected.
4. **Scoring is rule-based** and may differ from a human evaluator’s assessment.
5. **Bullet improvement** uses templates. Always review and verify suggestions before using them.
6. The app works best with **English-language resumes**.
7. Complex multi-column PDF layouts may produce mixed text order after parsing.

---

## ✅ Responsible Use

- Use suggested improvements only if they reflect your actual experience.
- Replace placeholders with real, verifiable facts.
- Do not claim skills, certifications, or achievements you do not actually have.
- Treat the score as a diagnostic guide, not as a hiring guarantee.
- Final resume accuracy remains the responsibility of the user.

---

*ResumeCraft AI Studio is open-source, free, and designed for educational and career-readiness use. No paid APIs. No unnecessary complexity. No false claims.*
"""

LIMITATIONS = [
    "PDF parsing may fail for scanned/image-based PDFs without OCR support",
    "Name extraction is heuristic and works best with standard resume formatting",
    "Section detection requires recognizable English section headings",
    "Scoring is rule-based and may differ from human evaluation",
    "Bullet improvement uses templates and must be verified before use",
    "Best results with English-language resumes in standard formats",
    "Multi-column PDF layouts may produce mixed text order",
]
