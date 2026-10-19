# 🧪 AI Tech Consultant — Evaluation Report

> **Project:** AI Tech Consultant  
> **Evaluation Type:** Functional Testing  
> **Environment:** Local Python + Streamlit  
> **AI API Required:** No

---

## 📌 1. Evaluation Overview

The purpose of this evaluation is to verify that the core workflows of AI Tech Consultant behave as expected.

The prototype contains four main components:

- 📚 Knowledge Brain
- 📧 Inbox Agent
- 📝 Meeting-to-Scope
- 🧪 Evaluation Dashboard

**Important:** Record actual test results before reporting that a test has passed. Planned tests and example results are not evidence of successful execution.

---

## 📊 2. Test Summary

| Metric | Value |
|---|---|
| Planned test cases below | 12 |
| Tests passed | Update after testing |
| Tests failed | Update after testing |
| Tests pending | 12 initially |
| Test execution | Manual + basic functional checks |

---

## 🧪 3. Knowledge Brain Tests

| Test ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| KB-01 | Search for website troubleshooting information | Relevant passage appears | ⬜ Pending |
| KB-02 | Submit an empty question | Validation message appears | ⬜ Pending |
| KB-03 | Ask about an unknown subject | No-relevant-information message appears | ⬜ Pending |

### Sample test input

```text
What details should I collect when a website page shows an error?
```

**Evaluation criteria:**
- Does the search return relevant text?
- Is the source filename displayed?
- Does the application handle empty input safely?

---

## 📧 4. Inbox Agent Tests

| Test ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| IA-01 | Email describes a website error | Technical Support category | ⬜ Pending |
| IA-02 | Email asks about an invoice | Billing category | ⬜ Pending |
| IA-03 | Email contains a general question | General Inquiry category | ⬜ Pending |
| IA-04 | Generate a suggested reply | Reply is displayed for review | ⬜ Pending |
| IA-05 | Download a generated reply | Text file downloads successfully | ⬜ Pending |

### Sample test inputs

**Technical Support**
```text
My membership website is broken and users cannot register.
```

**Billing**
```text
Please explain the payment on my subscription invoice.
```

**General Inquiry**
```text
Could you tell me more about your services?
```

**Evaluation criteria:**
- Is the email assigned to the expected category?
- Is the reply relevant and readable?
- Can the draft be downloaded?
- Does the application avoid sending email automatically?

---

## 📝 5. Meeting-to-Scope Tests

| Test ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| MS-01 | Submit several meeting requirements | Requirements appear in the output | ⬜ Pending |
| MS-02 | Submit an empty transcript | Validation message appears | ⬜ Pending |
| MS-03 | Generate and download a scope | Text file downloads successfully | ⬜ Pending |

### Sample test input

```text
Build a membership directory website.
Allow user registration and login.
Add member profile management.
Enable search by location.
Send email notifications.
```

**Evaluation criteria:**
- Are the input requirements displayed?
- Is the scope file created correctly?
- Are next steps clearly communicated?
- Is human review recommended before sharing the scope?

---

## ⚙️ 6. Evaluation Dashboard Tests

| Test ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| EV-01 | Run the built-in evaluation checks | Test results are displayed | ⬜ Pending |

The built-in dashboard currently checks a small number of predefined conditions. It is not a comprehensive benchmark of AI quality.

---

## 📈 7. Evaluation Metrics

As the application improves, use these metrics to assess it:

| Metric | Meaning |
|---|---|
| Retrieval relevance | Whether retrieved passages answer the question |
| Classification accuracy | Correct email categories ÷ total evaluated emails |
| Requirement extraction quality | How many required items are correctly captured |
| Download success rate | Successful downloads ÷ download attempts |
| Response latency | Time taken to produce a result |
| Human review rate | Outputs requiring manual correction or approval |

For classification accuracy:

```text
Accuracy (%) = Correct classifications / Total test cases × 100
```

Record measurements from actual tests rather than inventing scores.

---

## 🔍 8. Limitations

The current prototype:

- Uses TF-IDF text similarity rather than semantic embeddings.
- Uses keyword rules for email classification.
- Generates email replies from predefined templates.
- Extracts meeting requirements from text lines.
- Does not implement full AI answer generation or multi-agent orchestration.
- Does not measure hallucination rates or comprehensive answer correctness.

---

## 🚀 9. Future Evaluation Plan

- [ ] Prepare at least 20 representative test cases per major workflow.
- [ ] Include empty, ambiguous, unusual, and out-of-scope inputs.
- [ ] Test retrieval relevance and citation correctness.
- [ ] Measure email classification accuracy.
- [ ] Review meeting requirement extraction against expected outputs.
- [ ] Compare alternative models or methods where available.
- [ ] Record quality, execution time, and cost for any optional external AI services.
- [ ] Save failures and document improvements.

---

## ✅ 10. Conclusion

This document defines an initial functional evaluation plan for AI Tech Consultant. The current tests are intended to verify prototype behavior, not to certify production readiness.

Complete the test cases, record the actual results, and document failures before submitting the evaluation report.
