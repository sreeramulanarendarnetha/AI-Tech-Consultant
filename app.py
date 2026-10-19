
import streamlit as st
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Tech Consultant", page_icon="🤖", layout="wide")
st.title("🤖 AI Tech Consultant")
st.caption("Local prototype — no API key required")

KNOWLEDGE_FILE = Path("data/knowledge.txt")


def load_documents():
    if not KNOWLEDGE_FILE.exists():
        return []
    content = KNOWLEDGE_FILE.read_text(encoding="utf-8")
    return [p.strip() for p in content.split("\n\n") if p.strip()]


def search_knowledge(question, documents):
    if not documents:
        return [], 0.0

    if len(question.split()) < 1:
        return [], 0.0

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(documents + [question])
    scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()

    best = scores.argsort()[::-1][:3]
    results = [
        (documents[i], float(scores[i]))
        for i in best if scores[i] > 0
    ]
    return results, max(scores, default=0.0)


documents = load_documents()

tab1, tab2, tab3, tab4 = st.tabs([
    "📚 Knowledge Brain",
    "📧 Inbox Agent",
    "📝 Meeting-to-Scope",
    "🧪 Evaluation"
])
with tab1:
    st.header("Knowledge Brain")
    question = st.text_input("Ask a question about the knowledge documents")

    if st.button("Search Knowledge"):
        if question.strip():
            results, score = search_knowledge(question, documents)

            if results:
                st.subheader("Relevant information")
                for passage, relevance in results:
                    st.write(passage)
                    st.caption(f"Source: data/knowledge.txt · Relevance: {relevance:.2f}")
            else:
                st.warning("No relevant passage found. Try another question or escalate to a human.")
        else:
            st.warning("Enter a question first.")

with tab2:
    st.header("Inbox Agent")
    email = st.text_area("Paste a customer email")

    if st.button("Classify Email and Draft Reply"):
        if email.strip():
            text = email.lower()

            if any(w in text for w in ["error", "broken", "not working", "issue", "bug"]):
                category = "Technical Support"
                reply = (
                    "Hello,\n\nThank you for reporting this issue. "
                    "Please share the affected page URL, the error message, "
                    "and the steps to reproduce the problem so our team can investigate.\n\n"
                    "Best regards,\nSupport Team"
                )
            elif any(w in text for w in ["price", "cost", "subscription", "payment", "invoice"]):
                category = "Billing"
                reply = (
                    "Hello,\n\nThank you for contacting us about billing. "
                    "Please share the relevant invoice or subscription details "
                    "without including sensitive payment information.\n\n"
                    "Best regards,\nSupport Team"
                )
            else:
                category = "General Inquiry"
                reply = (
                    "Hello,\n\nThank you for contacting us. "
                    "Could you please share a few more details about your request?\n\n"
                    "Best regards,\nSupport Team"
                )

            st.write("**Category:**", category)
            st.subheader("Suggested reply")
            st.text_area("Review before sending", reply, height=180)

            st.download_button(
                "Download Email Reply",
                data=reply,
                file_name="customer_email_reply.txt",
                mime="text/plain"
            )

            st.info("Human review required. This prototype does not send emails.")
        else:
            st.warning("Paste an email first.")

with tab3:
    st.header("Meeting-to-Scope")
    transcript = st.text_area("Paste meeting notes or a transcript")

    if st.button("Generate Project Scope"):
        if transcript.strip():
            lines = [
                line.strip(" -*•\t")
                for line in transcript.splitlines()
                if line.strip()
            ]

            st.subheader("Extracted requirements")
            for line in lines:
                st.checkbox(line, value=True, key=f"req_{lines.index(line)}")

            st.subheader("Next steps")
            st.write(
                "1. Confirm requirements with the client.\n"
                "2. Validate technical feasibility.\n"
                "3. Estimate effort, timeline, and cost.\n"
                "4. Obtain human approval before implementation."
            )
            st.download_button(
                "Download scope as text",
                "PROJECT SCOPE\n\n" + "\n".join("- " + line for line in lines),
                file_name="project_scope.txt",
                mime="text/plain"
            )
            st.warning("This is a preliminary scope; review it before sharing.")
        else:
            st.warning("Enter meeting notes first.")
with tab4:
    st.header("🧪 Evaluation Dashboard")
    st.write("Run basic checks on the three project workflows.")

    if st.button("Run Evaluation Tests"):
        tests = [
            {
                "name": "Knowledge documents loaded",
                "passed": len(documents) > 0,
                "detail": f"{len(documents)} passages found"
            },
            {
                "name": "Knowledge search returns a result",
                "passed": bool(
                    search_knowledge(
                        "website error troubleshooting",
                        documents
                    )[0]
                ),
                "detail": "Search checked against local knowledge"
            },
            {
                "name": "Email classification: technical issue",
                "passed": any(
                    word in "website is broken and showing an error"
                    for word in ["error", "broken", "not working", "issue", "bug"]
                ),
                "detail": "Sample email contains technical issue keywords"
            },
            {
                "name": "Meeting notes can be extracted",
                "passed": len([
                    line for line in
                    "Build a directory website\nAdd user registration".splitlines()
                    if line.strip()
                ]) == 2,
                "detail": "Two sample requirements extracted"
            }
        ]

        passed = sum(test["passed"] for test in tests)

        st.metric("Tests passed", f"{passed}/{len(tests)}")

        for test in tests:
            if test["passed"]:
                st.success(f"PASS — {test['name']}: {test['detail']}")
            else:
                st.error(f"FAIL — {test['name']}: {test['detail']}")

        st.caption(
            "These are basic prototype checks, not a comprehensive "
            "evaluation of AI answer quality."
        )