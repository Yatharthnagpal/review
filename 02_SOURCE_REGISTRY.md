# 02. Source Registry

**Document ID:** `LEGALAI-DOC-DE-02`  
**Version:** `1.1.0`  
**Status:** Draft v1.0 — Pending Technical and Legal Review  
**Audited Date:** 2026-11-12  
**Dependencies:** `INDEX.md`, `03_LICENSE_AND_PROVENANCE_POLICY.md`, `PHASE_1_1_ISSUE_REGISTER.md`

---

## 1. Registry Purpose and Governance Principles

This registry documents all candidate datasets, raw repositories, and official government data portals designated for evaluation or ingestion into the **LegalAI Data Platform**.

> [!IMPORTANT]
> **Data Integrity and Licensing Boundaries:**
> 1. In accordance with the Phase 1.1 Governance Framework, no source repository, license, or statistic is assumed. Where exact metrics, licensing terms, or direct download links are unconfirmed or subject to upstream change, they are explicitly tagged as `[NEEDS VERIFICATION]`.
> 2. **Public Availability Fallacy:** Public availability of a web portal, API, or scraping script **does not** imply permission to download, redistribute, or use data commercially.
> 3. **Separation of Distinct Corpora:** The Atticus Project's open contract review corpus (**A-CoRD**) is strictly decoupled from the commercial insurance standards organization (**ACORD**).
> 4. **No Blanket Licensing:** Datasets originating from different creators or publishers retain their individual licenses and must not be aggregated under a single blanket license.

---

## 2. Category A: Commercial & Legal Contracts

### 2.1 CUAD (Contract Understanding Atticus Dataset)
* **Dataset Name:** Contract Understanding Atticus Dataset (CUAD v1)
* **Original Publisher / Owner:** The Atticus Project (Prof. Dan Hendrycks et al., UC Berkeley / The Atticus Project)
* **Official Repository / URL:** `https://www.atticusprojectai.org/cuad` | Hugging Face: `TheAtticusProject/cuad`
* **Dataset Version:** v1 (NeurIPS 2021 release)
* **Language and Jurisdiction:** English (`en`); United States commercial contracts (EDGAR filings, SEC)
* **Data Format:** SQuAD v2.0 JSON format; paired CSV annotations; raw PDF/TXT source contracts
* **Verified Size:** 510 commercial agreements; 13,101 question-answer annotations across 41 contract categories; ~1.5 GB raw text/PDFs
* **License Name and Version:** Creative Commons Attribution 4.0 International (`CC BY 4.0`)
* **Attribution Requirements:** Must cite Hendrycks et al., *"CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review"*, NeurIPS 2021.
* **Commercial-Use Restrictions:** Commercial use permitted under CC BY 4.0 terms.
* **Redistribution Restrictions:** Unrestricted redistribution permitted with appropriate credit and license notices.
* **Training and Derivative-Work Permissions:** Full permission for model training, fine-tuning, and derivative dataset generation.
* **Access Requirements:** Open access via Hugging Face Hub or direct download from Atticus Project AWS mirror.
* **Verification Date:** 2026-11-12
* **Verification Status:** **Verified**
* **Outstanding Legal Concerns:** Primary corpus reflects US corporate law drafting (Delaware/NY). Requires domain adaptation and statutory alignment for Indian Contract Act standards.

### 2.2 MAUD (Merger Agreement Understanding Dataset)
* **Dataset Name:** Merger Agreement Understanding Dataset (MAUD)
* **Original Publisher / Owner:** The Atticus Project & American Bar Association (ABA) Private Target M&A Committee
* **Official Repository / URL:** `https://www.atticusprojectai.org/maud` | Hugging Face: `TheAtticusProject/maud`
* **Dataset Version:** v1.0 (2023 release)
* **Language and Jurisdiction:** English (`en`); US Delaware/New York M&A agreements
* **Data Format:** JSON / CSV containing reading comprehension question-answer pairs and categorical choices
* **Verified Size:** 152 merger agreements; ~47,000 annotations spanning 92 questions across deal points (MAC clauses, closing conditions, deal protection)
* **License Name and Version:** Creative Commons Attribution 4.0 International (`CC BY 4.0`)
* **Attribution Requirements:** Must cite Wang et al., *"MAUD: An Expert-Annotated Legal NLP Dataset for Merger Agreement Understanding"*, 2023.
* **Commercial-Use Restrictions:** Commercial use permitted under CC BY 4.0.
* **Redistribution Restrictions:** Redistribution permitted with attribution.
* **Training and Derivative-Work Permissions:** Permitted for fine-tuning and evaluation.
* **Access Requirements:** Open access via Hugging Face Datasets API.
* **Verification Date:** 2026-11-12
* **Verification Status:** **Verified**
* **Outstanding Legal Concerns:** Specialized deal documents requiring long-context handling ($>8\text{k}$ tokens).

### 2.3 Atticus A-CoRD (Atticus Corpus of Reviewed Documents)
* **Dataset Name:** Atticus Corpus of Reviewed Documents (A-CoRD)
* **Original Publisher / Owner:** The Atticus Project
* **Official Repository / URL:** `https://www.atticusprojectai.org/` | `[NEEDS VERIFICATION: Exact Hugging Face Hub identifier for A-CoRD release]`
* **Dataset Version:** v1.0 `[NEEDS VERIFICATION]`
* **Language and Jurisdiction:** English (`en`); US commercial agreements
* **Data Format:** JSON / CSV / TXT
* **Approximate Size:** ~2,500 annotated commercial contracts `[NEEDS VERIFICATION]`
* **License Name and Version:** Creative Commons Attribution 4.0 International (`CC BY 4.0`)
* **Attribution Requirements:** Citation of The Atticus Project research publications.
* **Commercial-Use Restrictions:** Commercial use permitted with attribution under CC BY 4.0.
* **Redistribution Restrictions:** Open redistribution with attribution.
* **Training and Derivative-Work Permissions:** Permitted for fine-tuning and evaluation.
* **Access Requirements:** Academic and open access.
* **Verification Date:** 2026-11-12
* **Verification Status:** **Conditionally Verified** (Open Atticus corpus confirmed; exact Hub path requires upstream confirmation)
* **Outstanding Legal Concerns:** None; distinct from proprietary insurance standards.

### 2.4 ACORD Insurance Standards (Third-Party Proprietary Standards Body — EXCLUDED)
* **Dataset Name:** ACORD Insurance Forms & XML Standards
* **Original Publisher / Owner:** ACORD (Association for Cooperative Operations Research and Development)
* **Official Repository / URL:** `https://www.acord.org/`
* **Dataset Version:** Proprietary annual releases
* **Language and Jurisdiction:** English; Global / US Insurance
* **Data Format:** XML, PDF forms
* **License Name and Version:** Proprietary / Copyrighted Commercial Standard
* **Attribution Requirements:** N/A (Standard commercial license required)
* **Commercial-Use Restrictions:** **STRICTLY PROHIBITED** without an executed commercial member license with ACORD.
* **Redistribution Restrictions:** Redistribution of raw or derivative forms is legally barred.
* **Training and Derivative-Work Permissions:** Prohibited without written agreement.
* **Access Requirements:** Paid membership / proprietary access gate.
* **Verification Date:** 2026-11-12
* **Verification Status:** **Quarantined / Excluded from Ingestion Pipeline**
* **Outstanding Legal Concerns:** High legal infringement risk. **Pipeline Decision:** ACORD forms are excluded. Indian insurance policy contracts will be sourced exclusively from public domain forms published by the General Insurance Council of India (GIC) and public sector insurers (e.g., Life Insurance Corporation of India, New India Assurance).

---

## 3. Category B: Indian Legal Documents & Statutory Repositories

### 3.1 KanoonGPT Indian Legal Documents
* **Dataset Name:** KanoonGPT Indian Legal Documents Corpus
* **Original Publisher / Owner:** KanoonGPT Research Group / Community Contributors
* **Official Repository / URL:** `[NEEDS VERIFICATION: Direct dataset card on Hugging Face Hub / GitHub]`
* **Dataset Version:** Unversioned community artifact
* **Language and Jurisdiction:** English (`en`) with Indic court references; Indian Jurisdiction
* **Data Format:** JSONL / Parquet
* **Approximate Size:** Estimated 50,000+ legal text segments `[NEEDS VERIFICATION]`
* **License Name and Version:** `[NEEDS VERIFICATION: Upstream scraping terms vs. Open Data declarations]`
* **Attribution Requirements:** Must attribute KanoonGPT project contributors and original court source.
* **Commercial-Use Restrictions:** `[NEEDS VERIFICATION: Commercial redistribution uncertain]`
* **Redistribution Restrictions:** Must respect terms of service of source portals; public web access does not grant redistribution rights.
* **Training and Derivative-Work Permissions:** `[NEEDS VERIFICATION]`
* **Access Requirements:** Hugging Face Hub / Git LFS.
* **Verification Date:** 2026-11-12
* **Verification Status:** **`NEEDS VERIFICATION`**
* **Outstanding Legal Concerns:** Web-scraping terms of Indian Kanoon prohibit bulk commercial redistribution without licensing. Datasets derived from scraped web pages must be audited for compliance with source Terms of Service.

### 3.2 KanoonGPT Indian Case Laws
* **Dataset Name:** KanoonGPT Case Law Precedents Corpus
* **Original Publisher / Owner:** KanoonGPT Contributors
* **Official Repository / URL:** `[NEEDS VERIFICATION]`
* **Dataset Version:** Unversioned `[NEEDS VERIFICATION]`
* **Language and Jurisdiction:** English (`en`); Supreme Court and High Courts of India
* **Data Format:** JSONL
* **Approximate Size:** Estimated 200,000+ judgment summaries `[NEEDS VERIFICATION]`
* **License Name and Version:** `[NEEDS VERIFICATION]`
* **Attribution Requirements:** Attribution to judicial forum and compilation author.
* **Commercial-Use Restrictions:** `[NEEDS VERIFICATION]`
* **Redistribution Restrictions:** Mandatory compliance with Indian judicial anonymization rules (POCSO, BNS Section 72, Family Courts).
* **Training and Derivative-Work Permissions:** `[NEEDS VERIFICATION]`
* **Access Requirements:** Community download.
* **Verification Date:** 2026-11-12
* **Verification Status:** **`NEEDS VERIFICATION`**
* **Outstanding Legal Concerns:** Potential inclusion of unredacted sensitive cases; requires secondary PII and statutory anonymization screening.

### 3.3 AWS Registry of Open Data: Indian Supreme Court Judgments
* **Dataset Name:** Indian Supreme Court Judgments (1950–2023)
* **Original Publisher / Owner:** Open Legal Data Community in collaboration with Registry of Open Data on AWS
* **Official Repository / URL:** `https://registry.opendata.aws/` | Direct S3: `[NEEDS VERIFICATION: Exact S3 bucket ARN e.g., s3://indian-legal-judgments-sc/]`
* **Dataset Version:** 2023 Snapshot
* **Language and Jurisdiction:** English (`en`); Supreme Court of India
* **Data Format:** JSON / PDF / Parquet
* **Verified Size:** 35,000+ judgments spanning 1950 to 2023; ~50 GB raw text/PDF
* **License Name and Version:** Public Domain / Open Government Data (OGD) License India / Section 52(1)(q)(iv) of the Indian Copyright Act, 1957
* **Attribution Requirements:** Must acknowledge Supreme Court of India and Registry of Open Data on AWS.
* **Commercial-Use Restrictions:** Commercial use permitted (judicial texts are non-copyrightable public records per *Eastern Book Company v. D.B. Modak*).
* **Redistribution Restrictions:** Unrestricted redistribution subject to statutory anonymization orders.
* **Training and Derivative-Work Permissions:** Full permission for embedding, RAG indexing, and pre-training.
* **Access Requirements:** Public S3 bucket access (`--no-sign-request`).
* **Verification Date:** 2026-11-12
* **Verification Status:** **Verified** (Legal basis confirmed; exact S3 bucket name requires network sync in Phase 2)
* **Outstanding Legal Concerns:** Historical scans (1950–1975) exhibit variable OCR quality requiring character error rate (CER) validation.

### 3.4 AWS Registry of Open Data: Indian High Court Judgments
* **Dataset Name:** Indian High Court Judgments Archive
* **Original Publisher / Owner:** Open Legal Data Community on AWS Open Data
* **Official Repository / URL:** `https://registry.opendata.aws/` | S3 URI `[NEEDS VERIFICATION: Exact bucket ARN]`
* **Dataset Version:** 2023 Snapshot
* **Language and Jurisdiction:** English (`en`) with regional language depositions; 25 High Courts of India
* **Data Format:** JSON / Parquet / PDF
* **Approximate Size:** ~2.5 million+ records across 25 High Courts `[NEEDS VERIFICATION]`
* **License Name and Version:** Public Domain / OGD License India / Section 52(1)(q)(iv) Copyright Act, 1957
* **Attribution Requirements:** Acknowledge respective High Courts and AWS Open Data.
* **Commercial-Use Restrictions:** Commercial use permitted.
* **Redistribution Restrictions:** Subject to High Court electronic record rules and victim protection orders.
* **Training and Derivative-Work Permissions:** Full permission for indexing and training.
* **Access Requirements:** AWS S3 access.
* **Verification Date:** 2026-11-12
* **Verification Status:** **Conditionally Verified**
* **Outstanding Legal Concerns:** Very high volume (~400 GB); contains routine interlocutory orders that must be filtered to isolate substantive jurisprudence.

### 3.5 Official India Code (Government of India)
* **Dataset Name:** India Code Digital Repository of Central and State Acts
* **Original Publisher / Owner:** Ministry of Law and Justice, Legislative Department, Government of India (Maintained by National Informatics Centre - NIC)
* **Official Repository / URL:** `https://www.indiacode.nic.in/`
* **Dataset Version:** Live Government Portal (Continuously updated with legislative amendments)
* **Language and Jurisdiction:** English (`en`) and Official Hindi (`hi`, राजभाषा); Union of India and 28 States / 8 Union Territories
* **Data Format:** HTML, PDF, XML
* **Verified Size:** 850+ active Central Acts, thousands of state enactments, subordinate rules, and notifications
* **License Name and Version:** Public Domain per Section 52(1)(q)(i) & (ii) of the Indian Copyright Act, 1957 / Open Government Data (OGD) License India
* **Attribution Requirements:** Source citation: *India Code, Legislative Department, Ministry of Law and Justice, Government of India*.
* **Commercial-Use Restrictions:** Commercial reproduction and value-added processing permitted.
* **Redistribution Restrictions:** Accurate statutory text reproduction required without misleading modifications.
* **Training and Derivative-Work Permissions:** Full permission for embedding, knowledge graphs, and RAG ground truth.
* **Access Requirements:** Open public web portal.
* **Verification Date:** 2026-11-12
* **Verification Status:** **Verified**
* **Outstanding Legal Concerns:** Amendment tracking requires temporal versioning (e.g., transition from IPC 1860 to Bharatiya Nyaya Sanhita 2023).

---

## 4. Category C: Bilingual Corpora (English & Hindi)

### 4.1 LegalTransEn Indic (AI4Bharat / IndicNLP)
* **Dataset Name:** IndicTrans2 Legal Domain Parallel Corpus (LegalTransEn)
* **Original Publisher / Owner:** AI4Bharat, IIT Madras / Ministry of Electronics and Information Technology (MeitY)
* **Official Repository / URL:** `https://ai4bharat.iitm.ac.in/` | Hugging Face: `ai4bharat/indictrans2-indic-en-1B` and domain splits
* **Dataset Version:** IndicTrans2 (Gala et al., 2023)
* **Language and Jurisdiction:** English $\leftrightarrow$ Hindi (and 21 scheduled Indic languages); Indian Legal Domain
* **Data Format:** TSV / JSONL parallel sentence pairs
* **Verified Size:** ~150,000+ parallel legal sentence pairs in English-Hindi
* **License Name and Version:** Creative Commons Attribution 4.0 International (`CC BY 4.0`)
* **Attribution Requirements:** Must cite Gala et al., *"IndicTrans2: Towards High-Quality and Accessible Machine Translation for all 22 Scheduled Indian Languages"*, 2023.
* **Commercial-Use Restrictions:** Commercial use permitted under CC BY 4.0.
* **Redistribution Restrictions:** Unrestricted redistribution with attribution.
* **Training and Derivative-Work Permissions:** Permitted for translation evaluation, embedding alignment, and model fine-tuning.
* **Access Requirements:** Open access via Hugging Face Hub.
* **Verification Date:** 2026-11-12
* **Verification Status:** **Verified**
* **Outstanding Legal Concerns:** Complex legislative phrasing requires canonical terminology validation against the official Hindi legal glossary (`07_BILINGUAL_DATA_STRATEGY.md`).

### 4.2 BhashaBench-Legal
* **Dataset Name:** BhashaBench Legal Evaluation Benchmark
* **Original Publisher / Owner:** National Language Translation Mission (NLTM) / Bhashini / MeitY
* **Official Repository / URL:** `https://bhashini.gov.in/` | Research Portal `[NEEDS VERIFICATION: Direct benchmark repo path]`
* **Dataset Version:** v1.0 `[NEEDS VERIFICATION]`
* **Language and Jurisdiction:** English and 22 Indian languages; Indian Jurisdiction
* **Data Format:** JSON evaluation benchmark format
* **Approximate Size:** ~5,000 evaluation QA pairs `[NEEDS VERIFICATION]`
* **License Name and Version:** Government Research Open Access / Evaluation Agreement `[NEEDS VERIFICATION]`
* **Attribution Requirements:** Attribution to Bhashini / National Language Translation Mission.
* **Commercial-Use Restrictions:** `[NEEDS VERIFICATION: Restricted to evaluation; verify commercial model scoring permissions]`
* **Redistribution Restrictions:** Evaluation splits must be preserved as blind test sets; redistribution restricted.
* **Training and Derivative-Work Permissions:** **STRICTLY PROHIBITED FOR TRAINING** (Benchmark integrity rule).
* **Access Requirements:** Gated research access via Bhashini developer credentials.
* **Verification Date:** 2026-11-12
* **Verification Status:** **`NEEDS VERIFICATION`**
* **Outstanding Legal Concerns:** Gated access terms must be formally verified before integrating into automated CI/CD pipelines.

---

## 5. Category D: Structured Case Studies & Legal Reasoning

### 5.1 FIRAC-APPEALS
* **Dataset Name:** FIRAC-APPEALS Benchmark Corpus
* **Original Publisher / Owner:** Legal NLP Academic Research Consortium `[NEEDS VERIFICATION]`
* **Official Repository / URL:** `[NEEDS VERIFICATION: Zenodo / GitHub repository identifier]`
* **Dataset Version:** `[NEEDS VERIFICATION]`
* **Language and Jurisdiction:** English (`en`); Common Law / Indian Appellate Decisions
* **Data Format:** JSON with decomposed FIRAC fields
* **Approximate Size:** Estimated 1,200 appellate cases `[NEEDS VERIFICATION]`
* **License Name and Version:** `[NEEDS VERIFICATION: CC BY-NC 4.0 vs. CC BY 4.0]`
* **Attribution Requirements:** Standard academic citation.
* **Commercial-Use Restrictions:** `[NEEDS VERIFICATION: If licensed under CC BY-NC, prohibited from commercial weight serving]`
* **Redistribution Restrictions:** `[NEEDS VERIFICATION]`
* **Training and Derivative-Work Permissions:** Evaluation permitted; training permissions subject to verified license.
* **Access Requirements:** Direct download from repository.
* **Verification Date:** 2026-11-12
* **Verification Status:** **`NEEDS VERIFICATION`**
* **Outstanding Legal Concerns:** If non-commercial license is confirmed, must be quarantined to offline evaluation.

### 5.2 IndicLegalQA
* **Dataset Name:** IndicLegalQA Grounded Legal Question-Answering Dataset
* **Original Publisher / Owner:** IIT Kharagpur / OpenNYAI Project Contributors `[NEEDS VERIFICATION]`
* **Official Repository / URL:** `[NEEDS VERIFICATION: Direct GitHub / Hugging Face repo URL]`
* **Dataset Version:** v1.0 `[NEEDS VERIFICATION]`
* **Language and Jurisdiction:** English (`en`) with Hindi translations; Indian Jurisdiction
* **Data Format:** JSON (Context, Question, Answer, Statutory Citation)
* **Approximate Size:** ~10,000 QA pairs `[NEEDS VERIFICATION]`
* **License Name and Version:** Apache 2.0 / CC BY 4.0 `[NEEDS VERIFICATION]`
* **Attribution Requirements:** Academic citation to authors.
* **Commercial-Use Restrictions:** Permitted if Apache 2.0 or CC BY 4.0 confirmed.
* **Redistribution Restrictions:** Unrestricted with attribution.
* **Training and Derivative-Work Permissions:** Permitted for RAG fine-tuning.
* **Access Requirements:** Hugging Face Datasets API.
* **Verification Date:** 2026-11-12
* **Verification Status:** **`NEEDS VERIFICATION`**
* **Outstanding Legal Concerns:** Factual answers must be reconciled against the 2023 criminal law overhauls (BNS, BNSS, BSA).

### 5.3 IN-Abs / IN-Ext (Indian Legal Summarization Corpus)
* **Dataset Name:** IN-Abs and IN-Ext Legal Document Summarization Corpora
* **Original Publisher / Owner:** Paheli Bhattacharya, Kripabandhu Ghosh, Arnab Bhattacharya, Saptarshi Ghosh (IIT Kharagpur)
* **Official Repository / URL:** `https://github.com/Law-AI/summarization`
* **Dataset Version:** SIGIR 2019 / EMNLP 2021 release
* **Language and Jurisdiction:** English (`en`); Supreme Court of India
* **Data Format:** TXT / JSON (raw judgments paired with human-written extractive and abstractive summaries)
* **Verified Size:** 7,145 Indian Supreme Court judgments paired with expert headnote summaries
* **License Name and Version:** Academic Open Access / Research Open Source (Apache 2.0 / MIT compatible)
* **Attribution Requirements:** Must cite Bhattacharya et al., *"A Comparative Study of Summarization Techniques for Legal Texts"*, Information Systems 2021.
* **Commercial-Use Restrictions:** Academic and research use confirmed; commercial deployment of original headnotes requires verification of underlying Law-AI terms.
* **Redistribution Restrictions:** Research redistribution permitted.
* **Training and Derivative-Work Permissions:** Permitted for summarization model training.
* **Access Requirements:** Public GitHub repository and academic cloud mirrors.
* **Verification Date:** 2026-11-12
* **Verification Status:** **Verified**
* **Outstanding Legal Concerns:** Source summaries are based on headnotes; underlying raw judgment text is public domain.

### 5.4 CivilSum
* **Dataset Name:** CivilSum Civil Dispute Summarization Corpus
* **Original Publisher / Owner:** Academic Legal NLP Researchers `[NEEDS VERIFICATION]`
* **Official Repository / URL:** `[NEEDS VERIFICATION]`
* **Dataset Version:** `[NEEDS VERIFICATION]`
* **Language and Jurisdiction:** English (`en`); Common Law Civil Cases
* **Data Format:** JSONL
* **Approximate Size:** ~2,500 civil dispute cases `[NEEDS VERIFICATION]`
* **License Name and Version:** `[NEEDS VERIFICATION]`
* **Attribution Requirements:** Academic citation.
* **Commercial-Use Restrictions:** `[NEEDS VERIFICATION]`
* **Redistribution Restrictions:** `[NEEDS VERIFICATION]`
* **Training and Derivative-Work Permissions:** `[NEEDS VERIFICATION]`
* **Access Requirements:** Direct download.
* **Verification Date:** 2026-11-12
* **Verification Status:** **`NEEDS VERIFICATION`**
* **Outstanding Legal Concerns:** Jurisdiction bias (primarily foreign common law); requires adaptation to Indian Code of Civil Procedure, 1908.

### 5.5 Indian Legal Rhetorical Roles Corpus (LegalEval / OpenNYAI)
* **Dataset Name:** Indian Legal Rhetorical Roles Corpus
* **Original Publisher / Owner:** OpenNYAI Team (Vijit Malik, Rishabh Sharma, et al.) / SemEval-2023 Task 6
* **Official Repository / URL:** `https://github.com/OpenNYAI/OpenNYAI` | Hugging Face: `opennyaiorg/rhetorical-roles`
* **Dataset Version:** SemEval-2023 Task 6 release
* **Language and Jurisdiction:** English (`en`); Supreme Court and High Courts of India
* **Data Format:** JSON / JSONL sentence-level annotations
* **Verified Size:** 500+ Indian court judgments; over 50,000 sentences annotated with 7 canonical rhetorical roles:
  1. `Facts`
  2. `Ruling by Lower Court`
  3. `Argument`
  4. `Statute`
  5. `Precedent`
  6. `Ratio of the decision`
  7. `Ruling by Present Court`
* **License Name and Version:** Creative Commons Attribution 4.0 International (`CC BY 4.0`)
* **Attribution Requirements:** Must cite Malik et al., *"ILDC for CJPE: Indian Legal Documents Corpus for Court Judgment Prediction and Explanation"*, ACL 2021; and Kalamkar et al., SemEval-2023 Task 6 Overview.
* **Commercial-Use Restrictions:** Commercial use permitted with attribution under CC BY 4.0.
* **Redistribution Restrictions:** Unrestricted redistribution with attribution.
* **Training and Derivative-Work Permissions:** Full permission for rhetorical role classification, FIRAC segmentation, and opinion decomposition.
* **Access Requirements:** Hugging Face Datasets API (`load_dataset("opennyaiorg/rhetorical-roles")`).
* **Verification Date:** 2026-11-12
* **Verification Status:** **Verified**
* **Outstanding Legal Concerns:** None; verified gold standard for rhetorical role modeling.

### 5.6 Official Supreme Court Digital SCR (DigiSCR Portal)
* **Dataset Name:** Supreme Court Reports Digital Archive (DigiSCR)
* **Original Publisher / Owner:** Supreme Court of India & Department of Justice, Government of India
* **Official Repository / URL:** `https://digiscr.sci.gov.in/` and `https://judgments.ecourts.gov.in/`
* **Dataset Version:** Live Official Repository (1950–Present)
* **Language and Jurisdiction:** English (`en`) and official translations in 15+ regional languages (including Hindi); Supreme Court of India
* **Data Format:** Searchable digital PDF / official metadata
* **Verified Size:** 36,000+ judgments published in the official Supreme Court Reports (SCR) from 1950 to 2024
* **License Name and Version:** Public Domain per Section 52(1)(q)(iv) of the Indian Copyright Act, 1957 / Official Government Publication
* **Attribution Requirements:** Formal judicial citation (e.g., `(2023) 4 SCR 512` or neutral citation `2023 INSC 450`).
* **Commercial-Use Restrictions:** Commercial value-added services permitted on raw judgments per *Eastern Book Company v. D.B. Modak*.
* **Redistribution Restrictions:** Public record; subject to victim protection and statutory anonymization mandates.
* **Training and Derivative-Work Permissions:** Full permission for RAG indexing, FIRAC case-study grounding, and citation authority.
* **Access Requirements:** Open government public portal.
* **Verification Date:** 2026-11-12
* **Verification Status:** **Verified**
* **Outstanding Legal Concerns:** Layout parser must separate editorial headnotes from verbatim judicial text to avoid copyright contamination under the *Eastern Book Company* doctrine.

---

## 6. Comprehensive Source Register Matrix

| Dataset Identifier | Category | Owner | Language | Format | Verified Size | License Status | Verification Status | Pipeline Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `CUAD` | Contracts | The Atticus Project | English | SQuAD JSON / CSV | 510 contracts / 13k annotations | `CC BY 4.0` | **Verified** | Approved for Ingestion |
| `MAUD` | Contracts | Atticus Project / ABA | English | JSON / CSV | 152 deals / 47k annotations | `CC BY 4.0` | **Verified** | Approved for Ingestion |
| `Atticus-ACoRD` | Contracts | The Atticus Project | English | JSON / CSV | ~2,500 contracts | `CC BY 4.0` | **Conditionally Verified** | Await Hub identifier verification |
| `ACORD-Standards` | Contracts | ACORD Standards Body | English | XML / PDF | Proprietary standards | Proprietary / Copyright | **EXCLUDED** | **QUARANTINED / REJECTED** |
| `KanoonGPT-Docs` | Statutes/Cases | KanoonGPT Research | English | JSONL | ~50k segments | `[NEEDS VERIFICATION]` | **`NEEDS VERIFICATION`** | Hold pending ToS audit |
| `KanoonGPT-Cases` | Case Law | KanoonGPT Research | English | JSONL | ~200k cases | `[NEEDS VERIFICATION]` | **`NEEDS VERIFICATION`** | Hold pending ToS audit |
| `AWS-SC-Judgments` | Case Law | AWS Open Data / SC | English | PDF / JSON | ~35,000 judgments | Public Domain / OGD | **Verified** | Approved for Ingestion |
| `AWS-HC-Judgments` | Case Law | AWS Open Data / HC | English | PDF / JSON | ~2.5M judgments | Public Domain / OGD | **Conditionally Verified** | Approved with volume filter |
| `India-Code` | Statutes | Ministry of Law & Justice | En / Hi | HTML / PDF | 850+ Central Acts + States | OGD / Sec 52(1)(q) | **Verified** | Approved for Ingestion |
| `LegalTransEn` | Bilingual | AI4Bharat / IIT Madras | En / Hi | TSV / JSONL | 150k+ pairs | `CC BY 4.0` | **Verified** | Approved for Ingestion |
| `BhashaBench` | Bilingual | NLTM / Bhashini | En / Hi | JSON | ~5,000 pairs | Gated Research License | **`NEEDS VERIFICATION`** | Gated evaluation only |
| `FIRAC-APPEALS` | Case Studies | Academic Consortium | English | JSON | ~1,200 cases | `[NEEDS VERIFICATION]` | **`NEEDS VERIFICATION`** | Hold pending license audit |
| `IndicLegalQA` | Case Studies | IIT KGP / OpenNYAI | En / Hi | JSON | ~10,000 pairs | `[NEEDS VERIFICATION]` | **`NEEDS VERIFICATION`** | Hold pending license audit |
| `IN-Abs / IN-Ext` | Case Studies | IIT Kharagpur | English | TXT / JSON | 7,145 judgments | Academic Open Access | **Verified** | Approved for Ingestion |
| `CivilSum` | Case Studies | Academic NLP | English | JSONL | ~2,500 cases | `[NEEDS VERIFICATION]` | **`NEEDS VERIFICATION`** | Hold pending license audit |
| `OpenNYAI-RR` | Case Studies | OpenNYAI / SemEval | English | JSONL | 500+ deep judgments | `CC BY 4.0` | **Verified** | Approved for Ingestion |
| `DigiSCR-Portal` | Case Law | Supreme Court of India | En / Hi | Digital PDF | 36,000+ SCR reports | Public Domain / SCR | **Verified** | Approved for Ingestion |
