# 🤖 AI Tech Consultant
### A Smart, Local Prototype for Knowledge Search, Email Assistance & Project Scoping

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Search-TF--IDF-orange)
![API](https://img.shields.io/badge/API%20Key-Not%20Required-success)

**AI Tech Consultant** is a Python-based web application prototype designed to demonstrate three practical business workflows. It runs locally and does not require a paid AI API key.

---

## ✨ Features

### 📚 1. Knowledge Brain
- Searches a local support knowledge base.
- Uses TF-IDF similarity to find relevant passages.
- Displays matching information and source details.

### 📧 2. Inbox Agent
- Classifies emails into Technical Support, Billing, or General Inquiry.
- Creates suggested email replies.
- Downloads replies as text files.
- Keeps a human in control of sending messages.

### 📝 3. Meeting-to-Scope
- Accepts meeting notes and transcripts.
- Extracts preliminary project requirements.
- Suggests next steps for feasibility and estimation.
- Downloads project scopes as text files.

### 🧪 4. Evaluation Dashboard
- Runs basic automated prototype checks.
- Displays passed and failed tests.
- Helps verify that core workflows are functioning.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive web interface |
| scikit-learn | TF-IDF text similarity |
| pathlib | Local file handling |

---

## 📂 Project Structure

```text
ai-tech-consultant/
│
├── app.py                 # Main Streamlit application
├── README.md              # Project documentation
├── data/
│   └── knowledge.txt      # Sample knowledge base
└── venv/                  # Python virtual environment
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10 or newer
- Visual Studio Code (recommended)

### Step 1: Clone or download the project

If your project is already on your computer, open its folder in VS Code and skip this step.

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

### Step 3: Activate the environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

```bash
pip install streamlit scikit-learn
```

### Step 5: Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

---

## 🧪 How to Test

| Feature | Sample input |
|---|---|
| Knowledge Brain | How do I troubleshoot a website error? |
| Inbox Agent | My membership website is broken and users cannot register. |
| Meeting-to-Scope | Build a directory website with registration and member profiles. |
| Evaluation | Click **Run Evaluation Tests**. |

---

## 🔐 Privacy & Safety

- The current prototype processes its inputs locally.
- It does not send emails automatically.
- Review all generated replies and project requirements before using them.
- Do not place passwords, API keys, or sensitive customer information in sample documents.

---

## ⚠️ Current Limitations

This is an early-stage prototype, not a complete autonomous AI system. It uses TF-IDF retrieval, rule-based email classification, and simple templates. It does not yet implement external documentation crawling, generative AI, production-grade RAG, email-provider integration, or a complete multi-agent workflow.

---

## 🔮 Future Enhancements

- [ ] Crawl approved support documentation.
- [ ] Improve retrieval quality and citations.
- [ ] Add a larger evaluation dataset and quality metrics.
- [ ] Generate structured proposals with effort estimates.
- [ ] Add email integration with approval controls.
- [ ] Implement and evaluate multi-agent workflows.
- [ ] Add deployment instructions and a demonstration video.

---
