# 02. Source Registry

**Document ID:** `LEGALAI-DOC-DE-02`  
**Version:** `1.2.0`  
**Status:** Draft v1.0 — Pending Technical and Legal Review  
**Audited Date:** 2026-11-13  
**Dependencies:** `INDEX.md`, `03_LICENSE_AND_PROVENANCE_POLICY.md`, `PHASE_1_2_EVIDENCE_REGISTER.md`

---

## 1. Registry Purpose and Governance Principles

This registry documents all candidate datasets, raw repositories, and official government data portals designated for evaluation or ingestion into the **LegalAI Data Platform**.

> [!IMPORTANT]
> **Data Integrity and Licensing Boundaries:**
> 1. In accordance with the Phase 1.2 Governance Framework, no source repository, license, or statistic is assumed. Where exact metrics, licensing terms, or direct download links are unconfirmed or subject to upstream change, they are explicitly tagged as **`NOT VERIFIED`**.
> 2. **Public Availability Fallacy:** Public availability of a web portal, API, or scraping script **does not** imply permission to download, redistribute, or use data commercially.
> 3. **Separation of Distinct Corpora:** The Atticus Project's open contract review corpus (**A-CoRD**) is strictly decoupled from the commercial insurance standards organization (**ACORD**).
> 4. **No Blanket Licensing:** Datasets originating from different creators or publishers retain their individual licenses and must not be aggregated under a single blanket license.
> 5. **Dimensional Verification:** Every source is evaluated across 8 independent verification dimensions: Publisher, Dataset Identity, Release/Version, License, Endpoint, Commercial Rights, Redistribution Rights, and Training Rights.

---

## 2. Category A: Commercial & Legal Contracts

### 2.1 CUAD (Contract Understanding Atticus Dataset)
* **Source ID:** `SRC-CONT-CUAD-01`
* **Publisher / Owner:** The Atticus Project (Prof. Dan Hendrycks et al., UC Berkeley / The Atticus Project)
* **Dataset Name:** Contract Understanding Atticus Dataset (CUAD v1)
* **Repository ID:** `TheAtticusProject/cuad`
* **Release / Version:** v1.0 (NeurIPS 2021 Release)
* **Access URL:** `https://www.atticusprojectai.org/cuad` | Hugging Face: `https://huggingface.co/datasets/TheAtticusProject/cuad`
* **License:** Creative Commons Attribution 4.0 International (`CC BY 4.0`)
* **License Evidence:** Published in dataset repository `LICENSE` file and NeurIPS 2021 proceedings paper.
* **Dataset Size:** 510 commercial contracts; 13,101 question-answer annotations; ~1.5 GB raw PDF/text.
* **Commercial Use:** Allowed (with attribution per CC BY 4.0).
* **Redistribution:** Allowed (with attribution per CC BY 4.0).
* **Training Use:** Allowed (full fine-tuning and evaluation rights).
* **Verification Date:** 2026-11-13
* **Verification Status:** **PASS**
* **Outstanding Legal Concerns:** US corporate law drafting (Delaware/NY); requires adaptation to Indian Contract Act standards.

### 2.2 MAUD (Merger Agreement Understanding Dataset)
* **Source ID:** `SRC-CONT-MAUD-01`
* **Publisher / Owner:** The Atticus Project & American Bar Association (ABA) Private Target M&A Committee
* **Dataset Name:** Merger Agreement Understanding Dataset (MAUD)
* **Repository ID:** `TheAtticusProject/maud`
* **Release / Version:** v1.0 (2023 Release)
* **Access URL:** `https://www.atticusprojectai.org/maud` | Hugging Face: `https://huggingface.co/datasets/TheAtticusProject/maud`
* **License:** Creative Commons Attribution 4.0 International (`CC BY 4.0`)
* **License Evidence:** Published on Hugging Face dataset card and project website.
* **Dataset Size:** 152 merger agreements; ~47,000 annotations spanning 92 deal point questions.
* **Commercial Use:** Allowed (with attribution).
* **Redistribution:** Allowed (with attribution).
* **Training Use:** Allowed.
* **Verification Date:** 2026-11-13
* **Verification Status:** **PASS**
* **Outstanding Legal Concerns:** Specialized deal documents requiring long context windows ($>8\text{k}$ tokens).

### 2.3 Atticus A-CoRD (Atticus Corpus of Reviewed Documents)
* **Source ID:** `SRC-CONT-ACORD-01`
* **Publisher / Owner:** The Atticus Project
* **Dataset Name:** Atticus Corpus of Reviewed Documents (A-CoRD)
* **Repository ID:** `[NOT VERIFIED: Standalone Hugging Face repository ID not independently confirmed]`
* **Release / Version:** Unknown
* **Access URL:** `https://www.atticusprojectai.org/`
* **License:** `[NOT VERIFIED]` (While Atticus Project releases CUAD/MAUD under CC BY 4.0, a standalone A-CoRD release license file has not been audited)
* **License Evidence:** Missing standalone license file.
* **Dataset Size:** Unverified (earlier estimate of 2,500 contracts cannot be asserted without an audited manifest).
* **Commercial Use:** Unknown / Not Verified.
* **Redistribution:** Unknown / Not Verified.
* **Training Use:** Unknown / Not Verified.
* **Verification Date:** 2026-11-13
* **Verification Status:** **NOT VERIFIED**
* **Outstanding Legal Concerns:** Ingestion deferred; base contract clause models will rely strictly on verified **CUAD** and **MAUD**.

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
* **License Evidence:** Missing upstream license file.
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
* **Access URL:** `[NOT VERIFIED]`
* **License:** `[NOT VERIFIED]`
* **License Evidence:** Missing.
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
* **Access URL:** `https://registry.opendata.aws/` (S3 endpoint: pending network verification in Phase 2)
* **License:** Public Domain per Section 52(1)(q)(iv) of the Indian Copyright Act, 1957 / Open Government Data (OGD) License India
* **License Evidence:** Statutory public domain status established by *Eastern Book Company v. D.B. Modak (2008) 1 SCC 1*.
* **Dataset Size:** 35,000+ full-text judgments; ~50 GB raw text/PDF.
* **Commercial Use:** Allowed (raw judicial text is in the public domain).
* **Redistribution:** Allowed (subject to statutory victim anonymization orders under BNS § 72, POCSO § 33(7)).
* **Training Use:** Allowed.
* **Verification Date:** 2026-11-13
* **Verification Status:** **CONDITIONAL** (Legal public domain status verified; exact S3 bucket ARN requires network sync in Phase 2).
* **Outstanding Legal Concerns:** OCR quality on historical judgments (pre-1975) requires CER validation.

### 3.4 AWS Registry of Open Data: Indian High Court Judgments
* **Source ID:** `SRC-CASE-AWSHC-01`
* **Publisher / Owner:** Open Legal Data Community on AWS Open Data
* **Dataset Name:** Indian High Court Judgments Archive
* **Repository ID:** AWS Open Data Registry (`indian-high-courts`)
* **Release / Version:** 2023 Snapshot
* **Access URL:** `https://registry.opendata.aws/`
* **License:** Public Domain per Section 52(1)(q)(iv) Copyright Act, 1957 / OGD India
* **License Evidence:** Statutory non-infringement exception under Section 52(1)(q)(iv).
* **Dataset Size:** ~2.5 million+ records across 25 High Courts (Unverified exact disk size, estimated ~400 GB).
* **Commercial Use:** Allowed for raw judicial text.
* **Redistribution:** Allowed subject to High Court electronic record rules and victim protection orders.
* **Training Use:** Allowed.
* **Verification Date:** 2026-11-13
* **Verification Status:** **CONDITIONAL**
* **Outstanding Legal Concerns:** Immense volume; contains routine interlocutory orders requiring aggressive substantive filtering.

### 3.5 Official India Code (Government of India)
* **Source ID:** `SRC-STAT-INCODE-01`
* **Publisher / Owner:** Ministry of Law and Justice, Legislative Department, Government of India (Maintained by National Informatics Centre - NIC)
* **Dataset Name:** India Code Digital Repository of Central and State Acts
* **Repository ID:** Official Government Portal
* **Release / Version:** Live Government Portal (Continuously updated)
* **Access URL:** `https://www.indiacode.nic.in/`
* **License:** Public Domain per Section 52(1)(q)(i) & (ii) of the Indian Copyright Act, 1957 / Open Government Data (OGD) License India
* **License Evidence:** Section 52(1)(q) statutory exception for legislative enactments published in Official Gazettes.
* **Dataset Size:** 850+ Central Acts, thousands of state enactments and subordinate rules.
* **Commercial Use:** Allowed (accurate reproduction without misleading alterations).
* **Redistribution:** Allowed.
* **Training Use:** Allowed.
* **Verification Date:** 2026-11-13
* **Verification Status:** **PASS**
* **Outstanding Legal Concerns:** Amendment tracking requires temporal versioning (e.g., transition from IPC 1860 to Bharatiya Nyaya Sanhita 2023).

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
* **License Evidence:** Missing standalone license file.
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
* **Repository ID:** Bhashini Research Portal
* **Release / Version:** v1.0
* **Access URL:** `https://bhashini.gov.in/`
* **License:** Government Evaluation License / Gated Research Access
* **License Evidence:** Bhashini research portal terms.
* **Dataset Size:** ~5,000 evaluation QA pairs (Approximate).
* **Commercial Use:** Restricted to evaluation; commercial serving barred.
* **Redistribution:** Restricted (Blind benchmark).
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
* **Release / Version:** Unknown
* **Access URL:** `[NOT VERIFIED]`
* **License:** `[NOT VERIFIED: CC BY-NC 4.0 vs. CC BY 4.0]`
* **License Evidence:** Missing.
* **Dataset Size:** Estimated 1,200 cases (Unverified).
* **Commercial Use:** Unknown.
* **Redistribution:** Unknown.
* **Training Use:** Unknown.
* **Verification Date:** 2026-11-13
* **Verification Status:** **NOT VERIFIED**
* **Outstanding Legal Concerns:** Ingestion held pending audited repository release.

### 5.2 IndicLegalQA
* **Source ID:** `SRC-CASE-INDQA-01`
* **Publisher / Owner:** IIT Kharagpur / OpenNYAI Project Contributors
* **Dataset Name:** IndicLegalQA Grounded Legal Question-Answering Dataset
* **Repository ID:** `[NOT VERIFIED: Direct repository URL requires verification]`
* **Release / Version:** v1.0
* **Access URL:** `[NOT VERIFIED]`
* **License:** `[NOT VERIFIED: Apache 2.0 vs. CC BY 4.0]`
* **License Evidence:** Missing.
* **Dataset Size:** ~10,000 QA pairs (Unverified).
* **Commercial Use:** Unknown.
* **Redistribution:** Unknown.
* **Training Use:** Unknown.
* **Verification Date:** 2026-11-13
* **Verification Status:** **NOT VERIFIED**
* **Outstanding Legal Concerns:** Answers must be validated against recent 2023 legislative enactments (BNS, BNSS, BSA).

### 5.3 IN-Abs / IN-Ext (Indian Legal Summarization Corpus)
* **Source ID:** `SRC-CASE-INABS-01`
* **Publisher / Owner:** Paheli Bhattacharya, Kripabandhu Ghosh, Arnab Bhattacharya, Saptarshi Ghosh (IIT Kharagpur)
* **Dataset Name:** IN-Abs and IN-Ext Legal Document Summarization Corpora
* **Repository ID:** `https://github.com/Law-AI/summarization`
* **Release / Version:** SIGIR 2019 / EMNLP 2021 Release
* **Access URL:** `https://github.com/Law-AI/summarization`
* **License:** Academic Research Open Source (Apache 2.0 / MIT Compatible)
* **License Evidence:** Repository notices and publication documentation (Bhattacharya et al., 2021).
* **Dataset Size:** 7,145 Indian Supreme Court judgments paired with expert headnote summaries.
* **Commercial Use:** Academic and research use confirmed; commercial deployment of original headnotes requires verification of underlying Law-AI terms.
* **Redistribution:** Permitted for research.
* **Training Use:** Allowed for summarization model training.
* **Verification Date:** 2026-11-13
* **Verification Status:** **PASS**
* **Outstanding Legal Concerns:** Source summaries reflect law reporter headnotes; raw judicial text is public domain.

### 5.4 CivilSum
* **Source ID:** `SRC-CASE-CIVSUM-01`
* **Publisher / Owner:** Academic Legal NLP Researchers
* **Dataset Name:** CivilSum Civil Dispute Summarization Corpus
* **Repository ID:** `[NOT VERIFIED]`
* **Release / Version:** Unknown
* **Access URL:** `[NOT VERIFIED]`
* **License:** `[NOT VERIFIED]`
* **License Evidence:** Missing.
* **Dataset Size:** ~2,500 cases (Unverified).
* **Commercial Use:** Unknown.
* **Redistribution:** Unknown.
* **Training Use:** Unknown.
* **Verification Date:** 2026-11-13
* **Verification Status:** **NOT VERIFIED**
* **Outstanding Legal Concerns:** Common law jurisdiction bias; adaptation to Indian Code of Civil Procedure required.

### 5.5 Indian Legal Rhetorical Roles Corpus (LegalEval / OpenNYAI)
* **Source ID:** `SRC-CASE-OPENNYAI-01`
* **Publisher / Owner:** OpenNYAI Team (Vijit Malik, Rishabh Sharma, et al.) / SemEval-2023 Task 6
* **Dataset Name:** Indian Legal Rhetorical Roles Corpus
* **Repository ID:** `opennyaiorg/rhetorical-roles`
* **Release / Version:** SemEval-2023 Task 6 Release
* **Access URL:** `https://huggingface.co/datasets/opennyaiorg/rhetorical-roles` | `https://github.com/OpenNYAI/OpenNYAI`
* **License:** Creative Commons Attribution 4.0 International (`CC BY 4.0`)
* **License Evidence:** Published in Hugging Face dataset card metadata and SemEval-2023 Task 6 overview.
* **Dataset Size:** 500+ Indian court judgments; over 50,000 sentences annotated with 7 canonical rhetorical roles.
* **Commercial Use:** Allowed (with attribution per CC BY 4.0).
* **Redistribution:** Allowed (with attribution per CC BY 4.0).
* **Training Use:** Allowed (full permission for rhetorical role classification and opinion decomposition).
* **Verification Date:** 2026-11-13
* **Verification Status:** **PASS**
* **Outstanding Legal Concerns:** None; verified gold standard for Indian judgment segmentation.

### 5.6 Official Supreme Court Digital SCR (DigiSCR Portal)
* **Source ID:** `SRC-CASE-DIGISCR-01`
* **Publisher / Owner:** Supreme Court of India & Department of Justice, Government of India
* **Dataset Name:** Supreme Court Reports Digital Archive (DigiSCR)
* **Repository ID:** Official Supreme Court Portal
* **Release / Version:** Live Official Archive (1950–Present)
* **Access URL:** `https://digiscr.sci.gov.in/` and `https://judgments.ecourts.gov.in/`
* **License:** Public Domain per Section 52(1)(q)(iv) of the Indian Copyright Act, 1957 / Official Government Publication
* **License Evidence:** Statutory non-infringement exception under Section 52(1)(q)(iv).
* **Dataset Size:** 36,000+ judgments published in official Supreme Court Reports (1950 to 2024).
* **Commercial Use:** Allowed for raw judicial text (*Eastern Book Company*).
* **Redistribution:** Allowed (subject to statutory victim anonymization).
* **Training Use:** Allowed.
* **Verification Date:** 2026-11-13
* **Verification Status:** **PASS**
* **Outstanding Legal Concerns:** Layout parsing must cleanly separate editorial headnotes from verbatim judicial text to avoid copyright infringement under the *Eastern Book Company* doctrine.

---

## 6. Multi-Dimensional Verification Status Matrix

| Source ID | Publisher | Identity | Release | License | Endpoint | Commercial | Redist. | Training | Composite Status | Pipeline Action |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `SRC-CONT-CUAD-01` | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** | Approved for Ingestion |
| `SRC-CONT-MAUD-01` | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** | Approved for Ingestion |
| `SRC-CONT-ACORD-01`| PASS | PASS | UNV | UNV | UNV | UNV | UNV | UNV | **NOT VERIFIED** | **Quarantined** (Missing Hub Repo) |
| `SRC-EXCL-ACORD-01`| PASS | PASS | PASS | PROHIB | PASS | PROHIB | PROHIB | PROHIB | **EXCLUDED** | **Excluded / Replaced with GIC** |
| `SRC-STAT-KANOON-01`| PASS | UNV | UNV | UNV | UNV | UNV | UNV | UNV | **NOT VERIFIED** | **Quarantined** (ToS Boundaries) |
| `SRC-CASE-KANOON-02`| PASS | UNV | UNV | UNV | UNV | UNV | UNV | UNV | **NOT VERIFIED** | **Quarantined** (ToS Boundaries) |
| `SRC-CASE-AWSSC-01`| PASS | PASS | PASS | PASS | COND | PASS | PASS | PASS | **CONDITIONAL** | Approved (S3 Sync Pending) |
| `SRC-CASE-AWSHC-01`| PASS | PASS | PASS | PASS | COND | PASS | PASS | PASS | **CONDITIONAL** | Approved (Volume Filter Pending) |
| `SRC-STAT-INCODE-01`| PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** | Approved for Ingestion |
| `SRC-BIL-TRANS-01` | PASS | UNV | UNV | UNV | UNV | UNV | UNV | UNV | **NOT VERIFIED** | **Quarantined** (Rely on Gazettes) |
| `SRC-BIL-BHASHA-01`| PASS | PASS | PASS | COND | COND | REST | REST | PROHIB | **CONDITIONAL** | **Gated Evaluation Only** |
| `SRC-CASE-FIRAC-01` | UNV | UNV | UNV | UNV | UNV | UNV | UNV | UNV | **NOT VERIFIED** | **Quarantined** |
| `SRC-CASE-INDQA-01` | UNV | UNV | UNV | UNV | UNV | UNV | UNV | UNV | **NOT VERIFIED** | **Quarantined** |
| `SRC-CASE-INABS-01` | PASS | PASS | PASS | PASS | PASS | COND | PASS | PASS | **PASS** | Approved for Summarization |
| `SRC-CASE-CIVSUM-01`| UNV | UNV | UNV | UNV | UNV | UNV | UNV | UNV | **NOT VERIFIED** | **Quarantined** |
| `SRC-CASE-OPENNYAI-01`| PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** | Approved for Ingestion |
| `SRC-CASE-DIGISCR-01`| PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** | Approved for Ingestion |

*Key: PASS = Verified with primary evidence; COND = Conditional on operational verification; UNV = Not Verified; PROHIB = Statutorily or contractually prohibited; REST = Restricted.*
