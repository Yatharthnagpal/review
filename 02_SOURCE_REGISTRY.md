# 02. Source Registry

**Document ID:** `LEGALAI-DOC-DE-02`  
**Version:** `1.2.2`  
**Status:** Draft v1.0 — Pending Technical and Legal Review  
**Audited Date:** 2026-11-13  
**Dependencies:** `INDEX.md`, `03_LICENSE_AND_PROVENANCE_POLICY.md`, `PHASE_1_2_2_EVIDENCE_REGISTER.md`

---

## 1. Registry Purpose and Governance Principles

This registry documents all candidate datasets, raw repositories, and official government data portals designated for evaluation or ingestion into the **LegalAI Data Platform**.

> [!IMPORTANT]
> **Data Integrity and Licensing Boundaries (LEG-122-02 & SRC-122-01):**
> 1. In accordance with the Phase 1.2.2 Governance Framework, no source repository, license, or statistic is assumed. Where exact metrics, licensing terms, or direct download links are unconfirmed or subject to upstream change, they are explicitly tagged as **`NOT VERIFIED`**, **`CONDITIONAL`**, or **`UNKNOWN`**.
> 2. **Public Availability Fallacy:** Public accessibility of a web portal, regulatory filing, API, or scraping script **does not** imply permission to download, train on, or commercially redistribute data.
> 3. **Separation of Annotation Rights from Underlying Source Documents:** An open-source license covering dataset annotations (e.g., `CC BY 4.0`) does **not** convey a license to the underlying contracts or judgments. Both tiers must be audited independently.
> 4. **No Universal Blanket Licensing:** Portals hosting legal materials (e.g., *India Code*) contain multiple distinct material classes (Acts, Rules, Gazette notices, Reports). A general portal policy (e.g., GODL India) does not automatically override statutory copyright conditions (such as Copyright Act § 52(1)(q)(ii)).
> 5. **Dimensional Verification:** Every source is evaluated across 8 independent verification dimensions: Publisher, Dataset Identity, Release/Version, License, Endpoint, Commercial Rights, Redistribution Rights, and Training Rights.

---

## 2. Category A: Commercial & Legal Contracts

### 2.1 CUAD (Contract Understanding Atticus Dataset)
* **Source ID:** `SRC-CONT-CUAD-01`
* **Publisher / Owner:** The Atticus Project (Prof. Dan Hendrycks et al., UC Berkeley / The Atticus Project)
* **Dataset Name:** Contract Understanding Atticus Dataset (CUAD v1)
* **Repository ID:** `TheAtticusProject/cuad` | Hugging Face: `TheAtticusProject/cuad`
* **Release / Version:** v1.0 (NeurIPS 2021 Release)
* **Access URL:** `https://www.atticusprojectai.org/cuad` | `https://huggingface.co/datasets/TheAtticusProject/cuad`
* **Dataset Size:** 510 commercial contracts; 13,101 question-answer annotations; ~1.5 GB raw PDF/text.
* **Verification Date:** 2026-11-13
* **Rights Separation Analysis (LEG-122-02):**
  - **A. Dataset Annotations (Atticus Project):**
    - *License:* Creative Commons Attribution 4.0 International (`CC BY 4.0`).
    - *License Evidence:* Published in repository `LICENSE` file and NeurIPS 2021 proceedings.
    - *Commercial Use (Annotations):* **Allowed** with required attribution.
    - *Redistribution (Annotations):* **Allowed** with attribution.
    - *Training Use (Annotations):* **Allowed** for question-answering and clause span classification.
  - **B. Underlying Contract Documents (SEC EDGAR Filings):**
    - *Origin:* Material corporate agreements filed as exhibits under SEC Regulation S-K.
    - *Source Rights:* Filings fulfill statutory corporate transparency obligations under US law; filers do not grant an explicit open-source or commercial reuse license to third parties. The Atticus Project explicitly does not warrant the copyright status of underlying agreements.
    - *Collection & Storage:* **Allowed** for internal research and evaluation from public regulatory records.
    - *Processing & Parsing:* **Allowed** for internal benchmark evaluation.
    - *Embedding Generation:* **Conditional** (Permitted under fair use for evaluation; commercial deployment unwarranted).
    - *Model Training on Full Contract Text:* **NOT VERIFIED / UNWARRANTED BY ATTICUS**.
    - *Redistribution of Raw Contracts:* **RESTRICTED / NOT VERIFIED** (Excluded from raw public redistribution).
    - *Commercial SaaS Serving:* **NOT VERIFIED** (LegalAI serving pipeline evaluates user-uploaded contracts, not underlying CUAD raw files).
* **Composite Verification Status:** **CONDITIONAL** (Annotations PASS; Underlying Contracts Restricted/Not Verified).
* **Outstanding Legal Concerns:** US corporate law drafting (Delaware/NY); requires adaptation to Indian Contract Act standards.

### 2.2 MAUD (Merger Agreement Understanding Dataset)
* **Source ID:** `SRC-CONT-MAUD-01`
* **Publisher / Owner:** The Atticus Project & American Bar Association (ABA) Private Target M&A Committee
* **Dataset Name:** Merger Agreement Understanding Dataset (MAUD)
* **Repository ID:** `TheAtticusProject/maud` | Hugging Face: `TheAtticusProject/maud`
* **Release / Version:** v1.0 (2023 Release)
* **Access URL:** `https://www.atticusprojectai.org/maud` | `https://huggingface.co/datasets/TheAtticusProject/maud`
* **Dataset Size:** 152 merger agreements; ~47,000 annotations spanning 92 deal point questions.
* **Verification Date:** 2026-11-13
* **Rights Separation Analysis (LEG-122-02):**
  - **A. Dataset Annotations (Atticus Project & ABA):**
    - *License:* Creative Commons Attribution 4.0 International (`CC BY 4.0`).
    - *License Evidence:* Published on Hugging Face dataset card and project website.
    - *Commercial Use (Annotations):* **Allowed** with attribution.
    - *Redistribution (Annotations):* **Allowed** with attribution.
    - *Training Use (Annotations):* **Allowed**.
  - **B. Underlying Merger Agreements (SEC EDGAR Filings):**
    - *Origin:* Public merger agreements filed on SEC EDGAR.
    - *Source Rights:* Corporate disclosure exhibits; underlying rights retained by filing parties; unwarranted by Atticus Project.
    - *Collection & Storage:* **Allowed** for research/benchmark.
    - *Embedding & Training:* **NOT VERIFIED / UNWARRANTED**.
    - *Redistribution of Raw Documents:* **RESTRICTED / NOT VERIFIED**.
    - *Commercial SaaS Serving:* **NOT VERIFIED**.
* **Composite Verification Status:** **CONDITIONAL** (Annotations PASS; Underlying Agreements Restricted/Not Verified).
* **Outstanding Legal Concerns:** Specialized deal documents requiring long context windows ($>8\text{k}$ tokens).

### 2.3 Atticus A-CoRD (Atticus Corpus of Reviewed Documents)
* **Source ID:** `SRC-CONT-ACORD-01`
* **Publisher / Owner:** The Atticus Project
* **Dataset Name:** Atticus Corpus of Reviewed Documents (A-CoRD)
* **Repository ID:** `[NOT VERIFIED: Standalone Hugging Face repository ID not independently confirmed]`
* **Release / Version:** Unknown
* **Access URL:** `https://www.atticusprojectai.org/`
* **License:** `[NOT VERIFIED]` (Standalone release license file has not been audited)
* **License Evidence:** Missing standalone license file.
* **Dataset Size:** Unverified.
* **Commercial Use:** Unknown / Not Verified.
* **Redistribution:** Unknown / Not Verified.
* **Training Use:** Unknown / Not Verified.
* **Verification Date:** 2026-11-13
* **Verification Status:** **NOT VERIFIED**
* **Outstanding Legal Concerns:** Ingestion deferred; base contract clause models rely strictly on verified CUAD and MAUD annotations.

### 2.4 ACORD Insurance Standards (Commercial Standards Body — EXCLUDED)
* **Source ID:** `SRC-EXCL-ACORD-01`
* **Publisher / Owner:** ACORD (Association for Cooperative Operations Research and Development)
* **Dataset Name:** ACORD Insurance Forms & Electronic Standards
* **Repository ID:** Proprietary commercial repository
* **Release / Version:** Annual member releases
* **Access URL:** `https://www.acord.org/`
* **License:** Proprietary / Copyrighted Commercial Standards
* **License Evidence:** ACORD Intellectual Property and Licensing Policy (`https://www.acord.org/standards/licensing`).
* **Dataset Size:** Proprietary form library.
* **Commercial Use:** **Prohibited** without executed commercial licensing agreement.
* **Redistribution:** **Prohibited**.
* **Training Use:** **Prohibited**.
* **Verification Date:** 2026-11-13
* **Verification Status:** **QUARANTINED / EXCLUDED**
* **Outstanding Legal Concerns:** High copyright infringement risk. Indian insurance contracts will be sourced exclusively from public domain forms published by the General Insurance Council of India (GIC) and public sector insurers (LIC, New India Assurance).

---

## 3. Category B: Indian Legal Documents & Statutory Repositories

### 3.1 KanoonGPT Indian Legal Documents
* **Source ID:** `SRC-STAT-KANOON-01`
* **Publisher / Owner:** KanoonGPT Community Contributors
* **Dataset Name:** KanoonGPT Indian Legal Documents Corpus
* **Repository ID:** `[NOT VERIFIED]`
* **Release / Version:** Unversioned
* **Access URL:** `[NOT VERIFIED: No public Hugging Face dataset card independently located]`
* **License:** `[NOT VERIFIED]`
* **Dataset Size:** Estimated 50,000+ segments (Unverified).
* **Commercial Use:** Unknown / Restricted by underlying website Terms of Service.
* **Redistribution:** Unknown / Restricted.
* **Training Use:** Unknown.
* **Verification Date:** 2026-11-13
* **Verification Status:** **NOT VERIFIED / QUARANTINED**
* **Outstanding Legal Concerns:** Terms of Service of underlying scraped legal portals bar unauthorized bulk redistribution. Ingestion quarantined.

### 3.2 KanoonGPT Indian Case Laws
* **Source ID:** `SRC-CASE-KANOON-02`
* **Publisher / Owner:** KanoonGPT Contributors
* **Dataset Name:** KanoonGPT Case Law Precedents Corpus
* **Repository ID:** `[NOT VERIFIED]`
* **Release / Version:** Unversioned
* **License:** `[NOT VERIFIED]`
* **Dataset Size:** Estimated 200,000+ cases (Unverified).
* **Commercial Use:** Unknown.
* **Redistribution:** Unknown / Subject to judicial anonymization.
* **Training Use:** Unknown.
* **Verification Date:** 2026-11-13
* **Verification Status:** **NOT VERIFIED / QUARANTINED**
* **Outstanding Legal Concerns:** Potential presence of unredacted sensitive cases (POCSO, sexual offenses); Terms of Service restrictions.

### 3.3 AWS Registry of Open Data: Indian Supreme Court Judgments
* **Source ID:** `SRC-CASE-AWSSC-01`
* **Publisher / Owner:** Open Legal Data Community in collaboration with Registry of Open Data on AWS
* **Dataset Name:** Indian Supreme Court Judgments (1950–2023)
* **Repository ID:** AWS Open Data Registry (`indian-legal-judgments-sc`)
* **Release / Version:** 2023 Archive Snapshot
* **Access URL:** `https://registry.opendata.aws/` (S3 endpoint: pending network verification in Sprint 2.1)
* **License:** Non-infringing Public Record per Section 52(1)(q)(iv) Copyright Act, 1957; Open Government Data principles.
* **License Evidence:** Statutory non-infringement status under Section 52(1)(q)(iv) and *Eastern Book Company v. D.B. Modak (2008) 1 SCC 1*.
* **Dataset Size:** Provisional Estimate: ~35,000 full-text judgments; ~50 GB raw text/PDF (Exact manifest unverified pending S3 sync).
* **Commercial Use:** Allowed for raw judicial text (*Eastern Book Company*).
* **Redistribution:** Allowed (subject to statutory victim anonymization orders under BNS § 72, POCSO § 33(7)).
* **Training Use:** Permitted for RAG and legal NLP research; commercial weight licensing pending legal review.
* **Verification Date:** 2026-11-13
* **Verification Status:** **CONDITIONAL** (Legal basis verified; exact S3 bucket ARN and record manifest pending operational sync in Sprint 2.1).
* **Outstanding Legal Concerns:** OCR quality on historical judgments (pre-1975) requires CER validation.

### 3.4 AWS Registry of Open Data: Indian High Court Judgments
* **Source ID:** `SRC-CASE-AWSHC-01`
* **Publisher / Owner:** Open Legal Data Community on AWS Open Data
* **Dataset Name:** Indian High Court Judgments Archive
* **Repository ID:** AWS Open Data Registry (`indian-high-courts`)
* **Release / Version:** 2023 Snapshot
* **Access URL:** `https://registry.opendata.aws/`
* **License:** Non-infringing Public Record per Section 52(1)(q)(iv) Copyright Act, 1957.
* **Dataset Size:** Provisional Estimate: ~2.5 million records across 25 High Courts (Unverified exact disk size, estimated ~400 GB).
* **Commercial Use:** Allowed for raw judicial text.
* **Redistribution:** Allowed subject to High Court electronic record rules and victim protection orders.
* **Training Use:** Permitted for research; commercial weights pending legal review.
* **Verification Date:** 2026-11-13
* **Verification Status:** **CONDITIONAL** (Pending operational endpoint confirmation and volume filtering).
* **Outstanding Legal Concerns:** Immense volume; contains routine interlocutory orders requiring aggressive substantive filtering.

### 3.5 Official India Code (Government of India)
* **Source ID:** `SRC-STAT-INCODE-01`
* **Publisher / Owner:** Ministry of Law and Justice, Legislative Department, Government of India (Maintained by National Informatics Centre - NIC)
* **Dataset Name:** India Code Digital Repository of Central and State Acts
* **Repository ID:** Official Government Portal (`https://www.indiacode.nic.in/`)
* **Release / Version:** Live Government Portal (Continuously updated)
* **Access URL:** `https://www.indiacode.nic.in/`
* **Dataset Size:** 850+ Central Acts, thousands of state enactments and subordinate rules.
* **Verification Date:** 2026-11-13
* **Material-Category Rights Disentanglement (SRC-122-01):**
  1. *Central Acts of Parliament:* Governed by Section 52(1)(q)(ii) of the Copyright Act, 1957. Republication requires accompanying commentary or other original matter. The general GODL policy on `data.gov.in` does not supersede the statutory condition of Section 52(1)(q)(ii). Standalone bare commercial resale without commentary is restricted.
  2. *Subordinate Rules & Regulations:* Governed by Section 52(1)(q)(i) (Official Gazette matter other than Acts). Reproduction is non-infringing.
  3. *Official Gazette Notifications:* Section 52(1)(q)(i) applies; non-infringing.
  4. *Government Reports laid before Legislature:* Governed by Section 52(1)(q)(iii) unless prohibited.
  5. *Portal Metadata, Search Index & DB Structure:* Governed by NIC terms / GODL India.
  6. *Commercial Use:* **Conditional** (Permitted when integrated with original LegalAI analytical metadata, subject to formal copyright counsel opinion).
  7. *Redistribution:* **Restricted** (Only with accompanying original matter).
  8. *Training Use:* **Conditional** (Internal RAG indexing permitted; commercial model training pending legal review).
* **Composite Verification Status:** **CONDITIONAL (PENDING LEGAL REVIEW)**
* **Outstanding Legal Concerns:** Temporal versioning required for transitioning statutes (e.g., IPC 1860 to Bharatiya Nyaya Sanhita 2023).

---

## 4. Category C: Bilingual Corpora (English & Hindi)

### 4.1 LegalTransEn Indic
* **Source ID:** `SRC-BIL-TRANS-01`
* **Publisher / Owner:** AI4Bharat / IndicNLP / Community
* **Dataset Name:** LegalTransEn Indic
* **Repository ID:** `[NOT VERIFIED: Standalone Hugging Face dataset repository not independently confirmed]`
* **Release / Version:** Unknown
* **Access URL:** `[NOT VERIFIED]`
* **License:** `[NOT VERIFIED]`
* **Dataset Size:** Estimated 150,000+ pairs (Unverified).
* **Commercial Use:** Unknown / Not Verified.
* **Redistribution:** Unknown.
* **Training Use:** Unknown.
* **Verification Date:** 2026-11-13
* **Verification Status:** **NOT VERIFIED**
* **Outstanding Legal Concerns:** Ingestion deferred. Bilingual parallel statutory corpora will be sourced directly from official Government parallel gazettes (*India Code* + *Vidhi Sahitya Prakashan*) and confirmed subsets of IndicTrans2.

### 4.2 BhashaBench-Legal
* **Source ID:** `SRC-BIL-BHASHA-01`
* **Publisher / Owner:** National Language Translation Mission (NLTM) / Bhashini / MeitY
* **Dataset Name:** BhashaBench Legal Evaluation Benchmark
* **Repository ID:** Bhashini Research Portal (`https://bhashini.gov.in/`)
* **Release / Version:** v1.0
* **License:** Government Evaluation License / Gated Research Access
* **Dataset Size:** ~5,000 evaluation QA pairs (Approximate).
* **Commercial Use:** **Restricted to evaluation; commercial serving barred.**
* **Redistribution:** **Restricted (Blind benchmark).**
* **Training Use:** **STRICTLY PROHIBITED FOR TRAINING** (Benchmark integrity rule).
* **Verification Date:** 2026-11-13
* **Verification Status:** **CONDITIONAL** (Gated evaluation credentials required from Bhashini in Phase 2).
* **Outstanding Legal Concerns:** Must be kept strictly isolated from all model training and fine-tuning pipelines.

---

## 5. Category D: Structured Case Studies & Legal Reasoning

### 5.1 FIRAC-APPEALS
* **Source ID:** `SRC-CASE-FIRAC-01`
* **Publisher / Owner:** Legal NLP Academic Research Consortium
* **Dataset Name:** FIRAC-APPEALS Benchmark Corpus
* **Repository ID:** `[NOT VERIFIED]`
* **License:** `[NOT VERIFIED]`
* **Dataset Size:** Estimated 1,200 cases (Unverified).
* **Verification Status:** **NOT VERIFIED** (Quarantined).

### 5.2 IndicLegalQA
* **Source ID:** `SRC-CASE-INDQA-01`
* **Publisher / Owner:** IIT Kharagpur / OpenNYAI Project Contributors
* **Dataset Name:** IndicLegalQA Grounded Legal Question-Answering Dataset
* **Repository ID:** `[NOT VERIFIED]`
* **License:** `[NOT VERIFIED]`
* **Dataset Size:** ~10,000 QA pairs (Unverified).
* **Verification Status:** **NOT VERIFIED** (Quarantined).

### 5.3 IN-Abs / IN-Ext (Indian Legal Summarization Corpus)
* **Source ID:** `SRC-CASE-INABS-01`
* **Publisher / Owner:** Paheli Bhattacharya, Kripabandhu Ghosh, Arnab Bhattacharya, Saptarshi Ghosh (IIT Kharagpur)
* **Dataset Name:** IN-Abs and IN-Ext Legal Document Summarization Corpora
* **Repository ID:** `https://github.com/Law-AI/summarization`
* **Release / Version:** SIGIR 2019 / EMNLP 2021 Release
* **Code License:** Apache License 2.0 / MIT Compatible
* **Underlying Documents License:** Supreme Court of India judgments (public record under Section 52(1)(q)(iv)).
* **License Evidence:** Repository notices and publication documentation (Bhattacharya et al., 2021).
* **Dataset Size:** 7,145 Indian Supreme Court judgments paired with headnote summaries.
* **Commercial Use:** Code is commercial-friendly; headnote summaries require attribution and verification against publisher terms.
* **Redistribution:** Permitted for research and evaluation.
* **Training Use:** Allowed for summarization model training.
* **Verification Date:** 2026-11-13
* **Verification Status:** **PASS**
* **Outstanding Legal Concerns:** Source summaries reflect law reporter headnotes; raw judicial text is non-infringing.

### 5.4 CivilSum
* **Source ID:** `SRC-CASE-CIVSUM-01`
* **Publisher / Owner:** Academic Legal NLP Researchers
* **Dataset Name:** CivilSum Civil Dispute Summarization Corpus
* **Repository ID:** `[NOT VERIFIED]`
* **License:** `[NOT VERIFIED]`
* **Dataset Size:** ~2,500 cases (Unverified).
* **Verification Status:** **NOT VERIFIED** (Quarantined).

### 5.5 Indian Legal Rhetorical Roles Corpus (LegalEval / OpenNYAI)
* **Source ID:** `SRC-CASE-OPENNYAI-01`
* **Publisher / Owner:** OpenNYAI Team (Vijit Malik, Rishabh Sharma, et al.) / SemEval-2023 Task 6
* **Dataset Name:** Indian Legal Rhetorical Roles Corpus
* **Repository ID:** `opennyaiorg/rhetorical-roles` | `https://github.com/OpenNYAI/OpenNYAI`
* **Release / Version:** SemEval-2023 Task 6 Release
* **Code License:** MIT License
* **Dataset License:** Creative Commons Attribution 4.0 International (`CC BY 4.0`)
* **Underlying Documents:** Public judgments of Indian High Courts and Supreme Court (§ 52(1)(q)(iv)).
* **Dataset Size:** 500+ Indian court judgments; over 50,000 sentences annotated with 7 canonical rhetorical roles.
* **Commercial Use:** Allowed for annotations (with attribution per CC BY 4.0).
* **Redistribution:** Allowed (with attribution per CC BY 4.0).
* **Training Use:** Allowed (full permission for rhetorical role classification).
* **Verification Date:** 2026-11-13
* **Verification Status:** **PASS**

### 5.6 Official Supreme Court Digital SCR (DigiSCR Portal)
* **Source ID:** `SRC-CASE-DIGISCR-01`
* **Publisher / Owner:** Supreme Court of India & Department of Justice, Government of India
* **Dataset Name:** Supreme Court Reports Digital Archive (DigiSCR)
* **Repository ID:** Official Supreme Court Portal (`https://digiscr.sci.gov.in/`)
* **License:** Public Record per Section 52(1)(q)(iv) of the Indian Copyright Act, 1957.
* **Dataset Size:** 36,000+ judgments published in official Supreme Court Reports (1950 to 2024).
* **Commercial Use:** Allowed for verbatim judicial text (*Eastern Book Company*).
* **Redistribution:** Allowed (subject to statutory victim anonymization).
* **Training Use:** Allowed for verbatim judicial text.
* **Verification Date:** 2026-11-13
* **Verification Status:** **PASS**
* **Outstanding Legal Concerns:** Layout parsing must cleanly separate official headnotes from verbatim judicial text under the *Eastern Book Company* doctrine.

---

## 6. Multi-Dimensional Verification Status Matrix

| Source ID | Publisher | Identity | Release | License | Endpoint | Commercial | Redist. | Training | Composite Status | Pipeline Action |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `SRC-CONT-CUAD-01` | PASS | PASS | PASS | PASS (Ann) | PASS | COND | COND | COND | **CONDITIONAL** | Approved for Benchmark Ingestion (Annotations CC BY 4.0; Contracts Restricted) |
| `SRC-CONT-MAUD-01` | PASS | PASS | PASS | PASS (Ann) | PASS | COND | COND | COND | **CONDITIONAL** | Approved for Benchmark Ingestion (Annotations CC BY 4.0; Contracts Restricted) |
| `SRC-CONT-ACORD-01`| PASS | PASS | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | **NOT VERIFIED** | **Quarantined** (Missing Hub Repo) |
| `SRC-EXCL-ACORD-01`| PASS | PASS | PASS | PROHIB | PASS | PROHIB | PROHIB | PROHIB | **EXCLUDED** | **Excluded / Replaced with GIC** |
| `SRC-STAT-KANOON-01`| PASS | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | **NOT VERIFIED** | **Quarantined** (ToS Boundaries) |
| `SRC-CASE-KANOON-02`| PASS | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | **NOT VERIFIED** | **Quarantined** (ToS Boundaries) |
| `SRC-CASE-AWSSC-01`| PASS | PASS | PASS | PASS | COND | PASS | PASS | COND | **CONDITIONAL** | Approved (S3 Sync Pending) |
| `SRC-CASE-AWSHC-01`| PASS | PASS | PASS | PASS | COND | PASS | PASS | COND | **CONDITIONAL** | Approved (Volume Filter Pending) |
| `SRC-STAT-INCODE-01`| PASS | PASS | PASS | COND | PASS | COND | REST | COND | **CONDITIONAL** | Approved (Commentary condition & TDM pending legal review) |
| `SRC-BIL-TRANS-01` | PASS | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | **NOT VERIFIED** | **Quarantined** (Rely on Gazettes) |
| `SRC-BIL-BHASHA-01`| PASS | PASS | PASS | COND | COND | REST | REST | PROHIB | **CONDITIONAL** | **Gated Evaluation Only (Training Barred)** |
| `SRC-CASE-FIRAC-01` | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | **NOT VERIFIED** | **Quarantined** |
| `SRC-CASE-INDQA-01` | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | **NOT VERIFIED** | **Quarantined** |
| `SRC-CASE-INABS-01` | PASS | PASS | PASS | PASS | PASS | COND | PASS | PASS | **PASS** | Approved for Summarization |
| `SRC-CASE-CIVSUM-01`| UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | **NOT VERIFIED** | **Quarantined** |
| `SRC-CASE-OPENNYAI-01`| PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** | Approved for Ingestion |
| `SRC-CASE-DIGISCR-01`| PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** | Approved for Ingestion |

*Key: PASS = Verified with primary evidence; COND = Conditional on operational verification or legal opinion; UNKNOWN = Unknown / Not Verified; PROHIB = Statutorily or contractually prohibited; REST = Restricted.*
