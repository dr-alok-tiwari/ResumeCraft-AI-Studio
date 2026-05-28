# 🎯 ResumeCraft AI Studio

> **Build, score, improve, and export ATS-ready resumes — without paid AI APIs.**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red?logo=streamlit)](https://streamlit.io)
[![No API Key Required](https://img.shields.io/badge/No%20API%20Key-Required-green)](.)
[![Offline](https://img.shields.io/badge/Works-Offline-brightgreen)](.)
[![License](https://img.shields.io/badge/License-MIT-purple)](.)

---

## 📋 Overview

ResumeCraft AI Studio is a **complete, production-ready, zero-cost resume tool** that runs entirely on your local machine. It provides:

- 🔍 **Resume Parsing** — PDF, DOCX, and TXT files
- 📊 **ATS Scoring** — Transparent 100-point rule-based system
- 🎯 **JD Matching** — TF-IDF cosine similarity keyword matching
- ✏️ **Bullet Improvement** — Rule-based writing pattern enhancement
- 🔨 **Resume Builder** — Guided form-based resume creation
- 📄 **Export** — PDF, DOCX, and TXT download
- 🎭 **Demo Mode** — Try with pre-loaded sample resumes

---

## ✅ Zero-Cost, No-API Statement

**This app does NOT use:**
- ❌ OpenAI API / ChatGPT
- ❌ Google Gemini API
- ❌ Claude / Anthropic API
- ❌ Perplexity API
- ❌ Groq API
- ❌ Any paid OCR or resume parsing API
- ❌ Any cloud database or storage service
- ❌ Any subscription service

**It ONLY uses:**
- ✅ Free, open-source Python libraries
- ✅ scikit-learn for TF-IDF (local, offline)
- ✅ pdfplumber/python-docx for parsing (local)
- ✅ reportlab for PDF export (local)
- ✅ Streamlit for the UI (local)
- ✅ Rule-based NLP (no model downloads required)

---

## 🗂️ Folder Structure

```
ResumeBuilder/
│
├── app.py                    # Main Streamlit entry point
├── requirements.txt          # Python dependencies
├── README.md                 # This file
│
├── modules/
│   ├── __init__.py
│   ├── parser.py             # PDF/DOCX/TXT parser + section extractor
│   ├── scorer.py             # ATS scoring engine (0–100, rule-based)
│   ├── jd_matcher.py         # JD keyword/TF-IDF/cosine matcher
│   ├── resume_builder.py     # Form-based resume builder data model
│   ├── bullet_improver.py    # Rule-based bullet point rewriter
│   ├── templates.py          # Resume HTML template rendering
│   ├── export_utils.py       # PDF/DOCX/TXT export utilities
│   ├── ui_components.py      # Shared Streamlit UI helpers
│   ├── sample_data.py        # Demo content and sample resumes
│   ├── role_profiles.py      # 13 role-specific keyword profiles
│   └── privacy.py            # Privacy policy content
│
├── assets/
│   └── style.css             # Custom Streamlit CSS theme
│
├── samples/
│   ├── sample_fresher_resume.txt
│   ├── sample_experienced_resume.txt
│   ├── sample_academic_cv.txt
│   ├── sample_data_analyst_jd.txt
│   ├── sample_business_analyst_jd.txt
│   └── sample_assistant_professor_jd.txt
│
├── exports/                  # Local export output directory
│
└── tests/
    ├── test_parser.py
    ├── test_scorer.py
    └── test_jd_matcher.py
```

---

## 🚀 Installation

### Prerequisites
- Python 3.10 or higher
- pip

### Step 1: Clone or download the project

```bash
cd d:\ResumeBuilder
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

---

## 🏃 Quick Start

1. **Demo Mode**: Navigate to "🎭 Demo Mode" in the sidebar to try the app instantly with pre-loaded resumes.

2. **Upload Resume**: Go to "📤 Upload & Parse Resume" to upload your PDF/DOCX/TXT resume.

3. **Score Resume**: Go to "📊 ATS Resume Scorer" and click "Run ATS Score Analysis".

4. **Match JD**: Paste a job description in "🎯 Job Description Matcher" and click "Match".

5. **Export**: Go to "👁️ Resume Preview & Export" to download your resume as PDF, DOCX, or TXT.

---

## 📊 How ATS Scoring Works

The scoring system is fully transparent and rule-based:

| Section | Max Points | Method |
|---|---|---|
| Contact Information | 10 | Regex: email, phone, LinkedIn detection |
| Professional Summary | 10 | Presence, word count (40–100), action verbs |
| Education | 10 | Degree keywords + year presence |
| Skills | 15 | Skill count + tech tool detection |
| Experience / Projects | 20 | Bullet count + dates + org names |
| Action Verbs | 10 | Match against curated verb list (100+) |
| Quantified Achievements | 10 | Regex patterns for numbers/percentages |
| ATS Formatting | 10 | Section heading detection + symbol check |
| Length & Readability | 5 | Word count range (300–700 words) |
| **Total** | **100** | |

---

## 🎯 How JD Matching Works

1. **TF-IDF Vectorization**: Both the resume and JD are converted to TF-IDF vectors using scikit-learn
2. **Cosine Similarity**: Measures overall textual similarity (0–100%)
3. **Keyword Extraction**: Top keywords extracted from the JD
4. **Skill Dictionary**: 100+ predefined skills matched in both texts
5. **Gap Analysis**: Missing skills labeled "Verify before adding" or "Learn before claiming"

---

## 🌐 Deployment

### Streamlit Cloud (Free)

1. Push the project to a GitHub repository
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set `app.py` as the main file
5. Deploy

### Local Network Sharing

```bash
streamlit run app.py --server.address=0.0.0.0 --server.port=8501
```

Access from other devices on the same network via `http://<your-ip>:8501`

---

## 🔒 Privacy

- All resume data is processed **locally in your session**
- No data is transmitted to external servers or APIs
- Files are not permanently stored unless you explicitly download them
- Session data is cleared when you close the browser tab
- Works completely **offline** after installation

> **Recommendation**: Avoid uploading highly sensitive personal data (government IDs, financial details) unless strictly necessary for your resume.

---

## 🧪 Running Tests

```bash
python -m pytest tests/ -v
```

Or run individual test files:

```bash
python tests/test_parser.py
python tests/test_scorer.py
python tests/test_jd_matcher.py
```

---

## ⚠️ Known Limitations

1. **PDF Parsing**: Scanned/image-only PDFs cannot be parsed (no OCR support). Text-based PDFs work well.
2. **Name Detection**: Heuristic-based. Works best with standard resume formatting (name on first line).
3. **Section Detection**: Requires recognizable English section headings. Non-standard headings may not be detected.
4. **Scoring vs. Human**: Rule-based scoring may differ from human evaluation. Use as a guide, not absolute truth.
5. **Bullet Improvement**: Template-based. Always review and verify before using improved bullets.
6. **Language**: Best results with English-language resumes in standard formats.
7. **Multi-column PDFs**: May produce mixed text order after parsing.

---

## 🚀 Future Improvements

- [ ] OCR support for scanned PDFs (tesseract)
- [ ] More languages support (Hindi, French, German)
- [ ] LinkedIn profile import
- [ ] Resume version history
- [ ] Spell check integration
- [ ] More export templates
- [ ] Grammar checking using local models
- [ ] Real-time collaborative editing
- [ ] Resume analytics dashboard

---

## 📦 Dependencies

| Package | Version | Purpose |
|---|---|---|
| streamlit | ≥1.32 | Web UI framework |
| scikit-learn | ≥1.3 | TF-IDF vectorization, cosine similarity |
| pdfplumber | ≥0.10 | PDF text extraction |
| PyPDF2 | ≥3.0 | PDF fallback parser |
| python-docx | ≥1.0 | DOCX parsing and export |
| docx2txt | ≥0.8 | DOCX text extraction fallback |
| reportlab | ≥4.0 | PDF generation |
| plotly | ≥5.15 | Interactive charts |
| pandas | ≥2.0 | Data manipulation |
| numpy | ≥1.24 | Numerical operations |
| textstat | ≥0.7 | Readability metrics |
| regex | ≥2023 | Advanced regex |
| Pillow | ≥10.0 | Image support |

---

## 📄 License

MIT License — Free to use, modify, and distribute.

---

*Built with ❤️ using Python, Streamlit, and scikit-learn. No AI APIs. No cloud. No cost.*
