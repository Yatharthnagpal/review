# Phase 1.1 Issue Register

**Document ID:** `LEGALAI-DOC-DE-ISSUE-REGISTER`  
**Version:** `1.0.0`  
**Status:** Active Tracking  
**Phase:** 1.1 — Documentation Audit & Corrections  
**Target Platform:** LegalAI (Indian Legal Intelligence Platform)

---

## 1. Issue Tracking Summary

This register consolidates all factual, legal, architectural, data-governance, and cross-document inconsistencies identified during the Phase 1 review. Every issue is tracked with severity, owner, resolution status, and affected documents.

| Issue ID | Category | Severity | Title | Status | Affected Documents |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `ISS-LEG-01` | Legal Accuracy | Critical | Conflation of BNS Section 72 and Section 73 | Resolved in Phase 1.1 | `03`, `05`, `12`, `13` |
| `ISS-LEG-02` | Legal Accuracy | Critical | Representation of DPDP Act 2023 Commencement Status | Resolved in Phase 1.1 | `01`, `03`, `05`, `07`, `13` |
| `ISS-LEG-03` | Legal Accuracy | High | Section 10 vs. Section 11 Contract Competency Attribution | Resolved in Phase 1.1 | `01`, `04`, `05`, `06` |
| `ISS-LEG-04` | Legal Accuracy | High | Section 73 vs. Section 74 Damages Distinction | Resolved in Phase 1.1 | `05`, `06`, `08` |
| `ISS-LEG-05` | Legal Accuracy | Medium | Section 52(1)(q) Text Quotation Alignment | Resolved in Phase 1.1 | `02`, `03` |
| `ISS-LEG-06` | Legal Accuracy | Medium | Family Courts Act §11 and POCSO §24(5)/§33(7) Precision | Resolved in Phase 1.1 | `03`, `13` |
| `ISS-SRC-01` | Source Registry | Critical | Conflation of Atticus ACORD with ACORD Standards Body | Resolved in Phase 1.1 | `02`, `03`, `14` |
| `ISS-SRC-02` | Source Registry | High | Uniform License Imposition on Mixed-License Datasets | Resolved in Phase 1.1 | `02`, `11` |
| `ISS-SRC-03` | Source Registry | High | KanoonGPT Terms and Redistribution Rights Clarification | Resolved in Phase 1.1 | `02`, `03` |
| `ISS-SRC-04` | Source Registry | Medium | AWS Open Data SC/HC Judgments Metadata Precision | Resolved in Phase 1.1 | `02` |
| `ISS-SRC-05` | Source Registry | Medium | LegalTransEn Indic & BhashaBench-Legal Source Audit | Resolved in Phase 1.1 | `02`, `07` |
| `ISS-SCH-01` | Canonical Schema | Critical | Divergence between `RiskSeverity` and `RiskLevel` | Resolved in Phase 1.1 | `04`, `05`, `06`, `11` |
| `ISS-SCH-02` | Canonical Schema | Critical | Divergence between `ClauseCategory` and `ClauseType` | Resolved in Phase 1.1 | `04`, `05`, `06`, `11` |
| `ISS-SCH-03` | Canonical Schema | High | Conflicting Legal NER Entity Counts (9 vs. 11) | Resolved in Phase 1.1 | `01`, `04`, `05` |
| `ISS-SCH-04` | Canonical Schema | High | Missing Perspective Lens in Core Schema | Resolved in Phase 1.1 | `04`, `05`, `06` |
| `ISS-SCH-05` | Canonical Schema | High | Hypothetical Case Study Field Distinction (Ground Truth vs. Synthetic) | Resolved in Phase 1.1 | `04`, `08` |
| `ISS-SCH-06` | Canonical Schema | Medium | Character Offset Definition (Bytes vs. Code Points) | Resolved in Phase 1.1 | `04`, `09` |
| `ISS-SCH-07` | Canonical Schema | Medium | Missing Vector Embedding Metadata Fields | Resolved in Phase 1.1 | `04`, `11` |
| `ISS-PRE-01` | Preprocessing | High | Aggressive Marginal Line Number Regex Stripping Real Clauses | Resolved in Phase 1.1 | `09` |
| `ISS-PRE-02` | Preprocessing | High | Blind Hyphenation Removal Corrupting Legal Terms | Resolved in Phase 1.1 | `09` |
| `ISS-PRE-03` | Preprocessing | Medium | Hardcoded Section Maximums Treated as Proof of Validity | Resolved in Phase 1.1 | `12` |
| `ISS-SPL-01` | Data Splitting | Critical | English-Hindi Character N-Gram Overlap Fallacy for Translation Leakage | Resolved in Phase 1.1 | `10` |
| `ISS-SPL-02` | Data Splitting | High | MinHash Precision/Recall Quality & Trade-off Measurement | Resolved in Phase 1.1 | `10` |
| `ISS-PRI-01` | Privacy | Critical | Regex Character Class Syntax Error in Email Filter (`[A-Z\|a-z]`) | Resolved in Phase 1.1 | `13` |
| `ISS-PRI-02` | Privacy | High | Overly Broad Bank Account Regex Matching All 9-18 Digit Numbers | Resolved in Phase 1.1 | `13` |
| `ISS-PRI-03` | Privacy | High | Equating Salted Hashing with Irreversible Anonymization | Resolved in Phase 1.1 | `13` |
| `ISS-PRI-04` | Privacy | High | Broad Corporate Name Exemption Risk | Resolved in Phase 1.1 | `13` |
| `ISS-PRI-05` | Privacy | Medium | Divergence between `AuditLog` Schema and `db_models.py` | Resolved in Phase 1.1 | `13` |
| `ISS-COD-01` | Codebase Alignment | Critical | Codebase Status Classification of Agents & RAG | Resolved in Phase 1.1 | `01`, `14`, `INDEX` |
| `ISS-ROA-01` | Roadmap & Status | High | Inconsistent Project Status Claims (Approved vs. Draft v1.0) | Resolved in Phase 1.1 | `INDEX`, `01`, `14` |

---

## 2. Detailed Issue Records

### ISS-LEG-01: Conflation of BNS Section 72 and Section 73
* **Category:** Indian Legal Accuracy
* **Severity:** Critical
* **Description:** Previous documentation stated that Indian Penal Code (IPC) Section 228A corresponds to Bharatiya Nyaya Sanhita (BNS) Section 73. In fact, Section 72 of BNS, 2023 corresponds to IPC Section 228A (disclosure of the identity of victims of certain sexual offences). BNS Section 73 deals with printing or publishing court proceedings without court permission (in-camera proceedings).
* **Resolution:** Clearly distinguish Section 72 (victim identity disclosure) and Section 73 (in-camera proceedings disclosure). Both are relevant to judicial text processing but serve distinct legal purposes.

### ISS-LEG-02: Representation of DPDP Act 2023 Commencement Status
* **Category:** Indian Legal Accuracy
* **Severity:** Critical
* **Description:** The DPDP Act, 2023 received Presidential assent on August 11, 2023, but Section 1(2) provides that it comes into force on dates appointed by Central Government notifications. As of early 2026, operational rules and the Data Protection Board are in phased establishment. Describing DPDP provisions as fully in force and legally actionable without qualification is inaccurate.
* **Resolution:** Qualify all DPDP Act references to note its phased commencement, distinguish statutory intent from currently enforceable rules, and present compliance measures as forward-looking governance architecture.

### ISS-LEG-03: Section 10 vs. Section 11 Contract Competency Attribution
* **Category:** Indian Legal Accuracy
* **Severity:** High
* **Description:** Previous drafts conflated the competence requirement under Section 10 with the definition of competence under Section 11, citing *Mohori Bibee v. Dharmodas Ghose* under Section 10/11 interchangeably.
* **Resolution:** Detail that Section 10 establishes the general prerequisite of "parties competent to contract", while Section 11 specifically defines who is competent (majority age, sound mind, not disqualified). *Mohori Bibee* directly construes Section 11.

### ISS-LEG-04: Section 73 vs. Section 74 Damages Distinction
* **Category:** Indian Legal Accuracy
* **Severity:** High
* **Description:** Sections 73 and 74 were grouped together as "Section 73-74: Compensation for breach / Penalty" without articulating the core legal divergence.
* **Resolution:** Detail that Section 73 governs unliquidated damages requiring proof of actual, direct, foreseeable loss, whereas Section 74 governs stipulated sums (liquidated damages and penalties) granting reasonable compensation capped at the stipulated amount, subject to judicial discretion (*Fateh Chand*, *Kailash Nath Associates*).

### ISS-SRC-01: Conflation of Atticus ACORD with ACORD Standards Body
* **Category:** Source Registry
* **Severity:** Critical
* **Description:** Previous text conflated ACORD (the Association for Cooperative Operations Research and Development, an insurance standards body with proprietary forms) with Atticus contract datasets. The Atticus Project developed A-CoRD / Atticus contract review corpora, which are open academic datasets.
* **Resolution:** Explicitly decouple the Atticus Project's open contract corpus from the commercial insurance standards organization ACORD. License each independently.

### ISS-SCH-01 & ISS-SCH-02: Schema Type Harmonization (`RiskSeverity` vs. `RiskLevel`, `ClauseCategory` vs. `ClauseType`)
* **Category:** Canonical Schema
* **Severity:** Critical
* **Description:** Existing backend code (`backend/app/models/schemas.py`) uses `RiskLevel` and `ClauseType`. Documentation introduced `RiskSeverity` and `ClauseCategory`, creating divergence.
* **Resolution:** Designate `RiskLevel` and `ClauseType` as canonical names matching `schemas.py`. Retain `RiskSeverity` and `ClauseCategory` as documented aliases with explicit type mappings.

### ISS-SPL-01: English-Hindi Character N-Gram Overlap Fallacy
* **Category:** Dataset Splitting
* **Severity:** Critical
* **Description:** Document `10` proposed using 13-gram token/character containment to detect cross-lingual translation leakage between English and Hindi. Because English uses the Latin script and Hindi uses the Devanagari script, character n-gram overlap between them is identically zero ($0.0\%$).
* **Resolution:** Replace with bilingual document/sentence alignment identifiers, cross-lingual semantic embedding similarity (via `BAAI/bge-m3` or `multilingual-e5`), and dictionary-based bilingual containment.

### ISS-PRI-01: Regex Character Class Syntax Error in Email Filter
* **Category:** Privacy & Governance
* **Severity:** Critical
* **Description:** In `13_DATA_PRIVACY_AND_GOVERNANCE.md`, the email regex was written as `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b`. Inside square brackets `[...]`, the pipe `|` is matched as a literal character, allowing malformed strings and missing standard multi-part top-level domains.
* **Resolution:** Correct to `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`.

### ISS-PRI-03: Salted Hashing as Anonymization Fallacy
* **Category:** Privacy & Governance
* **Severity:** High
* **Description:** Text claimed that salted SHA-256 hashing produces anonymized data. Under established data protection principles (including DPDP and GDPR guidance), keyed hashing or salted hashing of identifiers constitutes **pseudonymization**, not irreversible anonymization, because individuals can be re-identified via dictionary attacks or rainbow tables on predictable names.
* **Resolution:** Accurately classify salted hashing as pseudonymization, and define the conditions under which true anonymization is achieved.

### ISS-COD-01: Existing Codebase Status Classification
* **Category:** Codebase Alignment
* **Severity:** Critical
* **Description:** Documentation previously described multi-agent orchestration and production RAG as existing capabilities. In the actual codebase, multi-agent orchestration is a sequential prompt-chaining function within `nlu.py` (partial), and RAG is a basic Qdrant cosine similarity lookup (partial).
* **Resolution:** Audit and classify every codebase component into: Existing, Partial, Planned, Missing, or Unverified. Correct all claims across all documents.

### ISS-ROA-01: Inconsistent Project Status Claims
* **Category:** Roadmap & Governance
* **Severity:** High
* **Description:** Some documents claimed "Approved for Implementation", violating the Phase 1 rule that execution must stop and wait for human review.
* **Resolution:** Standardize status across all 15 documents to: **Draft v1.0 — Pending Technical and Legal Review**.

