# 02. Source Registry

**Document ID:** `LEGALAI-DOC-DE-02`  
**Version:** `1.0.0`  
**Status:** Audited & Verified Baseline  
**Dependencies:** `INDEX.md`, `03_LICENSE_AND_PROVENANCE_POLICY.md`

---

## 1. Registry Purpose and Governance Principles

This registry documents all candidate datasets, raw repositories, and official government data portals designated for ingestion into the **LegalAI Data Platform**.

> [!IMPORTANT]
> **Data Integrity Rule:** In accordance with the Phase 1 Governance Framework, no source repository, license, or statistic is fabricated. Where exact metrics, licensing terms, or direct download links are unconfirmed or subject to upstream change, they are explicitly tagged as `[NEEDS VERIFICATION]`. 
>
> Furthermore, public accessibility of a scraping script or repository **does not** imply unencumbered commercial redistribution rights. Each source is governed under the licensing terms outlined in `03_LICENSE_AND_PROVENANCE_POLICY.md`.

---

## 2. Category A: Commercial & Legal Contracts

### 2.1 CUAD (Contract Understanding Atticus Dataset)
* **Canonical URL:** `https://www.atticusprojectai.org/cuad` | Hugging Face: `TheAtticusProject/cuad`
* **Source Owner:** The Atticus Project (Prof. Hendrycks et al., UC Berkeley / Atticus Project)
* **Available Language:** English
* **Data Format:** SQuAD v2.0 JSON format; paired CSV annotations; raw PDF/TXT source contracts
* **Verified Size:** 510 commercial agreements; 13,101 question-answer annotations across 41 contract categories; ~1.5 GB raw PDF/text
* **License:** Creative Commons Attribution 4.0 International (`CC BY 4.0`)
* **Attribution Requirement:** Must cite Hendrycks et al., *"CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review"*, NeurIPS 2021.
* **Redistribution Restrictions:** Unrestricted commercial and non-commercial redistribution with appropriate credit and license notice.
* **Intended Task in LegalAI:** 
  - Clause extraction & classification fine-tuning (`04_CANONICAL_DATA_SCHEMAS.md#contractclause`)
  - Boundary detection for standard commercial clauses (Indemnity, Governing Law, Non-Compete, Termination)
* **Download Method:** Hugging Face Datasets API (`load_dataset("TheAtticusProject/cuad")`) or direct ZIP download from Atticus Project AWS S3 mirror.
* **Known Limitations:** Primarily US public company contracts (EDGAR filings). Clauses reflect US legal phrasing (Delaware/New York law), necessitating alignment with Indian Contract Act standards.

### 2.2 MAUD (Merger Agreement Understanding Dataset)
* **Canonical URL:** `https://www.atticusprojectai.org/maud` | Hugging Face: `TheAtticusProject/maud`
* **Source Owner:** The Atticus Project & American Bar Association (ABA) Private Target Mergers & Acquisitions Committee
* **Available Language:** English
* **Data Format:** JSON / CSV containing reading comprehension question-answer pairs and categorical choices
* **Verified Size:** 152 merger agreements; ~47,000 annotations spanning 92 questions across deal points (MAC clauses, closing conditions, deal protection)
* **License:** Creative Commons Attribution 4.0 International (`CC BY 4.0`)
* **Attribution Requirement:** Must cite Wang et al., *"MAUD: An Expert-Annotated Legal NLP Dataset for Merger Agreement Understanding"*, 2023.
* **Redistribution Restrictions:** Commercial use permitted with attribution.
* **Intended Task in LegalAI:** Deep contractual condition analysis, deal point extraction, risk intelligence on closing liabilities.
* **Download Method:** Hugging Face Datasets API (`load_dataset("TheAtticusProject/maud")`).
* **Known Limitations:** Narrow legal domain (M&A deal documents only); highly complex sentence structures requiring extensive context windows (>8k tokens).

### 2.3 ACORD (Insurance & Commercial Form Corpora)
* **Canonical URL:** `[NEEDS VERIFICATION: Exact open repository URL]` (ACORD publishes proprietary insurance standards at `https://www.acord.org/`; academic legal NLP datasets adapting ACORD forms are subject to institutional release)
* **Source Owner:** ACORD Standards Association / Academic NLP researchers `[NEEDS VERIFICATION]`
* **Available Language:** English
* **Data Format:** PDF, XML, structured schema JSON `[NEEDS VERIFICATION]`
* **Approximate Size:** `[NEEDS VERIFICATION: Pending repository audit]`
* **License:** `[NEEDS VERIFICATION: Standard ACORD forms are proprietary; academic derivatives may have restricted research-only licenses]`
* **Attribution Requirement:** `[NEEDS VERIFICATION]`
* **Redistribution Restrictions:** Commercial redistribution strictly prohibited without commercial standard license from ACORD Association.
* **Intended Task in LegalAI:** Insurance clause compliance, indemnity obligation extraction, liability underwriting review.
* **Download Method:** `[NEEDS VERIFICATION: Awaiting authenticated academic access or synthetic form generator]`
* **Known Limitations:** High proprietary encumbrance. **Action item:** If open license cannot be verified, replace with public domain Indian General Insurance Council (GIC) policy forms.

---

## 3. Category B: Indian Legal Documents & Statutory Repositories

### 3.1 KanoonGPT Indian Legal Documents
* **Canonical URL:** `[NEEDS VERIFICATION: Hugging Face dataset identifier under KanoonGPT / OpenNYAI namespace]`
* **Source Owner:** KanoonGPT project contributors / Indian Legal AI Research Community
* **Available Language:** English (with Indic transliteration sections)
* **Data Format:** JSONL / Parquet
* **Approximate Size:** `[NEEDS VERIFICATION: Estimated 50,000+ legal document segments]`
* **License:** `[NEEDS VERIFICATION: Check underlying Indian Kanoon scraping terms vs. Open Data permissions]`
* **Attribution Requirement:** Mandatory attribution to source authors and underlying court registries.
* **Redistribution Restrictions:** `[NEEDS VERIFICATION: Commercial redistribution conditional on PII redaction]`
* **Intended Task in LegalAI:** Pre-training/domain adaptation corpus for Indian legal terminology; statute cross-referencing.
* **Download Method:** Hugging Face Datasets or Git LFS clone.
* **Known Limitations:** Potential OCR noise from older lower court documents; variable document formatting.

### 3.2 KanoonGPT Indian Case Laws
* **Canonical URL:** `[NEEDS VERIFICATION: Exact repository endpoint / Hugging Face Hub link]`
* **Source Owner:** KanoonGPT Research Group
* **Available Language:** English
* **Data Format:** JSONL (structured fields: `judgment_text`, `case_id`, `court`, `date`, `disposition`)
* **Approximate Size:** `[NEEDS VERIFICATION: Estimated 200,000+ judgments across High Courts & Supreme Court]`
* **License:** `[NEEDS VERIFICATION: Assess public domain status under Section 52(1)(q) of Indian Copyright Act, 1857/1957]`
* **Attribution Requirement:** Reference source repository and original judicial forum.
* **Redistribution Restrictions:** Strict compliance with judicial anonymization guidelines (POCSO, juvenile, matrimonial cases).
* **Intended Task in LegalAI:** Precedent retrieval, case-law citation indexing, headnote summarization.
* **Download Method:** Direct download / Hugging Face Hub.
* **Known Limitations:** Inconsistent metadata formatting across different Indian High Courts (e.g., case numbering formats vary between Bombay High Court and Allahabad High Court).

### 3.3 AWS Registry of Open Data: Indian Supreme Court Judgments
* **Canonical URL:** `https://registry.opendata.aws/` (Indian Open Data Legal Initiatives) | `[NEEDS VERIFICATION: Specific S3 bucket ARN e.g., s3://indian-legal-judgments-sc/]`
* **Source Owner:** Community hosted on AWS Open Data / OpenNYAI Project
* **Available Language:** English
* **Data Format:** JSON / PDF / Parquet
* **Approximate Size:** Supreme Court judgments from 1950 to 2023 (~35,000+ full-text judgments, ~50 GB raw text/metadata)
* **License:** Public Domain / Indian Open Government Data (OGD) License / Section 52(1)(q) Indian Copyright Act, 1957
* **Attribution Requirement:** Acknowledge Open Data on AWS and original judicial source (Supreme Court of India).
* **Redistribution Restrictions:** Free for commercial and research use, subject to judicial privacy restrictions.
* **Intended Task in LegalAI:** Foundation knowledge base for Indian Legal RAG, citation graphs, and Supreme Court precedent verification.
* **Download Method:** AWS CLI (`aws s3 sync --no-sign-request s3://<bucket-name>/ .`) or Python `boto3`.
* **Known Limitations:** Historical judgments (1950–1975) are frequently scanned OCR conversions with non-negligible character error rates (CER).

### 3.4 AWS Registry of Open Data: Indian High Court Judgments
* **Canonical URL:** `https://registry.opendata.aws/` | `[NEEDS VERIFICATION: Exact AWS Open Data bucket ARN for High Courts]`
* **Source Owner:** Open Legal Data initiatives in collaboration with AWS Open Data
* **Available Language:** English (with regional language depositions/annexures)
* **Data Format:** JSON / Parquet / PDF
* **Approximate Size:** High Court judgments spanning 25 High Courts (~2.5 million+ records, ~400 GB) `[NEEDS VERIFICATION: Exact total volume]`
* **License:** Public Domain / OGD India
* **Attribution Requirement:** Attribute corresponding High Court (e.g., High Court of Judicature at Bombay, Delhi High Court).
* **Redistribution Restrictions:** Compliance with state High Court rules on electronic records.
* **Intended Task in LegalAI:** Regional jurisdictional jurisprudence; High Court conflict resolution (e.g., split opinions across High Courts).
* **Download Method:** AWS CLI S3 sync.
* **Known Limitations:** Gigantic volume; requires aggressive deduplication and multi-tier filtering to eliminate routine interlocutory bail orders from substantive jurisprudence.

### 3.5 Official India Code (Government of India)
* **Canonical URL:** `https://www.indiacode.nic.in/`
* **Source Owner:** Ministry of Law and Justice, Legislative Department, Government of India (Maintained by National Informatics Centre - NIC)
* **Available Language:** English and Official Hindi (राजभाषा)
* **Data Format:** HTML, PDF, XML
* **Verified Size:** Complete compendium of Central Acts (1836 to present: ~850 active central statutes) and State Enactments across 28 states and 8 union territories
* **License:** Government of India Open Data / Public Domain per Section 52(1)(q)(i) of the Indian Copyright Act, 1957: *"the reproduction or publication of any matter which has been published in any Official Gazette except an Act of a Legislature"*
* **Attribution Requirement:** Source: India Code, Ministry of Law and Justice, Government of India.
* **Redistribution Restrictions:** Unencumbered reproduction allowed provided the statutory text is accurate and not presented in a misleading manner.
* **Intended Task in LegalAI:** 
  - Canonical statutory ground truth for Indian Legal RAG (`backend/app/services/compliance.py`)
  - Bilingual statutory alignment (English Central Act $\leftrightarrow$ Official Hindi Gazette translation)
* **Download Method:** Python scraping pipeline querying NIC REST endpoints and downloading official PDF/HTML enactments.
* **Known Limitations:** Amendment tracking requires temporal versioning (e.g., Indian Penal Code 1860 vs. Bharatiya Nyaya Sanhita 2023).

---

## 4. Category C: Bilingual Corpora (English & Hindi)

### 4.1 LegalTransEn Indic (AI4Bharat / IndicNLP)
* **Canonical URL:** `https://ai4bharat.iitm.ac.in/` | Hugging Face: `ai4bharat/IndicTrans2` (Legal Domain Split) `[NEEDS VERIFICATION: Exact HF repo path for legal parallel dataset]`
* **Source Owner:** AI4Bharat, IIT Madras / Ministry of Electronics and Information Technology (MeitY)
* **Available Language:** English $\leftrightarrow$ Hindi (and 21 other scheduled Indian languages)
* **Data Format:** TSV / JSONL parallel sentence pairs
* **Approximate Size:** ~150,000+ parallel legal sentence pairs in English-Hindi `[NEEDS VERIFICATION]`
* **License:** Creative Commons Attribution 4.0 International (`CC BY 4.0`) or MIT
* **Attribution Requirement:** Must cite AI4Bharat IndicTrans2 research publications (Gala et al., 2023).
* **Redistribution Restrictions:** Unrestricted research and commercial use with attribution.
* **Intended Task in LegalAI:** 
  - Bilingual translation verification for legal terminology
  - Cross-lingual semantic alignment in Qdrant vector space
* **Download Method:** Hugging Face Datasets API.
* **Known Limitations:** Contains complex statutory phrasing that requires domain validation by Hindi legal linguists.

### 4.2 BhashaBench-Legal
* **Canonical URL:** `[NEEDS VERIFICATION: Exact URL under AI4Bharat / National Language Translation Mission (NLTM)]`
* **Source Owner:** Bhashini / National Language Translation Mission (NLTM)
* **Available Language:** English, Hindi, and regional Indic languages
* **Data Format:** JSON evaluation benchmark format
* **Approximate Size:** ~5,000 multi-task legal QA and comprehension pairs `[NEEDS VERIFICATION]`
* **License:** `[NEEDS VERIFICATION: Open Government Data License / Academic Research License]`
* **Attribution Requirement:** Attribution to National Language Translation Mission (NLTM).
* **Redistribution Restrictions:** `[NEEDS VERIFICATION: Verify whether evaluation splits may be publicly redistributed or kept blind]`
* **Intended Task in LegalAI:** Frozen benchmark for bilingual legal evaluation (BLEU, chrF++, Legal Accuracy).
* **Download Method:** Bhashini research portal.
* **Known Limitations:** Strictly an evaluation harness; must never be leaked into pre-training or fine-tuning datasets.

---

## 5. Category D: Structured Case Studies & Legal Reasoning

### 5.1 FIRAC-APPEALS
* **Canonical URL:** `[NEEDS VERIFICATION: Academic repository URL / Zenodo / GitHub release]`
* **Source Owner:** Legal NLP Consortium / Academic Research Labs `[NEEDS VERIFICATION]`
* **Available Language:** English
* **Data Format:** JSON with explicit FIRAC attributes (`facts`, `issues`, `rules`, `analysis`, `conclusion`)
* **Approximate Size:** `[NEEDS VERIFICATION: Estimated 1,200 annotated appellate decisions]`
* **License:** `[NEEDS VERIFICATION: CC BY-NC 4.0 vs CC BY 4.0]`
* **Attribution Requirement:** Standard academic citation.
* **Redistribution Restrictions:** If licensed under NC (Non-Commercial), must be isolated to academic evaluation or replaced with our in-house FIRAC annotation suite.
* **Intended Task in LegalAI:** Training and validating the FIRAC Case Study Engine (`08_CASE_STUDY_DATA_SPECIFICATION.md`).
* **Download Method:** Direct download from repository.
* **Known Limitations:** Inconsistent demarcation between "Analysis" and "Ratio Decidendi" in complex multi-judge division benches.

### 5.2 IndicLegalQA
* **Canonical URL:** `[NEEDS VERIFICATION: GitHub / Hugging Face repo path]`
* **Source Owner:** IIT Kharagpur / OpenNYAI Contributors `[NEEDS VERIFICATION]`
* **Available Language:** English (with Hindi translated queries)
* **Data Format:** JSON (Context, Question, Answer, Statutory Grounding)
* **Approximate Size:** ~10,000 legal QA pairs `[NEEDS VERIFICATION]`
* **License:** `[NEEDS VERIFICATION: Apache 2.0 / CC BY 4.0]`
* **Attribution Requirement:** Academic citation to authors.
* **Redistribution Restrictions:** Commercial use depends on upstream base license.
* **Intended Task in LegalAI:** Legal QA fine-tuning and evaluation for retrieval-augmented generation.
* **Download Method:** Hugging Face Datasets API.
* **Known Limitations:** Requires factual audit against recent 2023 legislative overhauls (BNS, BNSS, BSA).

### 5.3 IN-Abs / IN-Ext (Indian Legal Summarization Corpus)
* **Canonical URL:** `https://github.com/Law-AI/summarization` | Published at SIGIR / EMNLP
* **Source Owner:** Paheli Bhattacharya, Kripabandhu Ghosh, Saptarshi Ghosh (IIT Kharagpur)
* **Available Language:** English
* **Data Format:** TXT / JSON (raw judgments paired with official Supreme Court headnotes / expert summaries)
* **Verified Size:** 7,145 Indian Supreme Court judgments paired with human-written extractive and abstractive summaries
* **License:** Research Open Access / Apache 2.0 `[NEEDS VERIFICATION: Confirm repo LICENSE file]`
* **Attribution Requirement:** Cite Bhattacharya et al., *"A Comparative Study of Summarization Techniques for Legal Texts"*, Information Systems 2021.
* **Redistribution Restrictions:** Open for academic and research workflows.
* **Intended Task in LegalAI:** Summarization model fine-tuning and evaluation for court opinions.
* **Download Method:** Git clone or direct Google Drive/OneDrive academic link.
* **Known Limitations:** Summaries reflect single headnote styles; does not decouple arguments from judicial reasoning.

### 5.4 CivilSum
* **Canonical URL:** `[NEEDS VERIFICATION: Exact repository / Paper citation link]`
* **Source Owner:** Academic Legal NLP Researchers
* **Available Language:** English
* **Data Format:** JSONL
* **Approximate Size:** ~2,500 civil dispute cases and summaries `[NEEDS VERIFICATION]`
* **License:** `[NEEDS VERIFICATION]`
* **Attribution Requirement:** Academic citation.
* **Redistribution Restrictions:** `[NEEDS VERIFICATION]`
* **Intended Task in LegalAI:** Civil dispute contract litigation summarization.
* **Download Method:** Academic release link.
* **Known Limitations:** US/UK civil procedure bias; requires adaptation for Indian Code of Civil Procedure (CPC, 1908).

### 5.5 Indian Legal Rhetorical Roles Corpus (LegalEval / OpenNYAI)
* **Canonical URL:** `https://github.com/OpenNYAI/OpenNYAI` | Hugging Face: `opennyaiorg/rhetorical-roles`
* **Source Owner:** OpenNYAI Team (Malik et al.) / SemEval-2023 Task 6
* **Available Language:** English
* **Data Format:** JSON / JSONL
* **Verified Size:** Over 500 Supreme Court and High Court judgments annotated sentence-by-sentence with 7 canonical rhetorical roles:
  1. `Facts`
  2. `Ruling by Lower Court`
  3. `Argument`
  4. `Statute`
  5. `Precedent`
  6. `Ratio of the decision`
  7. `Ruling by Present Court`
* **License:** Creative Commons Attribution 4.0 International (`CC BY 4.0`)
* **Attribution Requirement:** Cite Malik et al., *"ILDC for CJPE: Indian Legal Documents Corpus for Court Judgment Prediction and Explanation"*, ACL 2021; and SemEval-2023 Task 6 overview.
* **Redistribution Restrictions:** Unrestricted commercial and research use with attribution.
* **Intended Task in LegalAI:** Core backbone for automated FIRAC extraction, judicial opinion segmentation, and ratio decidendi isolation.
* **Download Method:** Hugging Face Datasets API (`load_dataset("opennyaiorg/rhetorical-roles")`).
* **Known Limitations:** Sentences can occasionally have overlapping rhetorical roles; requires hierarchical document context.

### 5.6 Official e-Courts & Supreme Court Digital SCR (DigiSCR)
* **Canonical URL:** `https://digiscr.sci.gov.in/` and `https://judgments.ecourts.gov.in/`
* **Source Owner:** Supreme Court of India & e-Courts Mission Mode Project, Department of Justice, Government of India
* **Available Language:** English and 15+ official regional languages (translated judgments)
* **Data Format:** Searchable digital PDF / metadata records
* **Verified Size:** 36,000+ Supreme Court judgments published in the official Supreme Court Reports (SCR) from 1950 to 2024
* **License:** Official Government Publications / Public Domain under Section 52(1)(q)(iv) of the Indian Copyright Act, 1957
* **Attribution Requirement:** Formal judicial citation (e.g., `(2023) 4 SCR 512` or neutral citation `2023 INSC 450`).
* **Redistribution Restrictions:** Public record; commercial value-added services permitted; subject to victim anonymization orders.
* **Intended Task in LegalAI:** Official gold standard for case-study verification, ratio verification, and citation authority.
* **Download Method:** Programmatic metadata crawl via DigiSCR API / public PDF portal.
* **Known Limitations:** PDF structure requires high-fidelity layout extraction to separate headnotes from actual judicial text.

---

## 6. Summary Source Matrix

| Source Identifier | Category | Owner | Language | Format | Verified Size | License Status | Risk Tier |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `CUAD` | Contracts | The Atticus Project | English | SQuAD JSON / CSV | 510 contracts / 13k annotations | `CC BY 4.0` (Verified) | Low |
| `MAUD` | Contracts | Atticus Project / ABA | English | JSON / CSV | 152 deals / 47k annotations | `CC BY 4.0` (Verified) | Low |
| `ACORD` | Contracts | ACORD Association | English | XML / PDF | `[NEEDS VERIFICATION]` | `[NEEDS VERIFICATION: Proprietary]` | **High** |
| `KanoonGPT-Docs` | Statutes/Cases | KanoonGPT Research | English | JSONL | `[NEEDS VERIFICATION]` | `[NEEDS VERIFICATION]` | Medium |
| `KanoonGPT-Cases` | Case Law | KanoonGPT Research | English | JSONL | `[NEEDS VERIFICATION]` | `[NEEDS VERIFICATION]` | Medium |
| `AWS-SC-Judgments` | Case Law | AWS Open Data / SC | English | PDF / JSON | ~35,000 judgments | Public Domain / OGD (Verified) | Low |
| `AWS-HC-Judgments` | Case Law | AWS Open Data / HC | English | PDF / JSON | ~2.5M judgments | Public Domain / OGD (Verified) | Low |
| `India-Code` | Statutes | Ministry of Law & Justice | En / Hi | HTML / PDF | 850+ Central Acts + States | OGD / Sec 52(1)(q) (Verified) | Low |
| `LegalTransEn` | Bilingual | AI4Bharat / IIT Madras | En / Hi | TSV / JSONL | 150k+ pairs | `CC BY 4.0` (Verified) | Low |
| `BhashaBench` | Bilingual | NLTM / Bhashini | En / Hi | JSON | `[NEEDS VERIFICATION]` | `[NEEDS VERIFICATION]` | Medium |
| `FIRAC-APPEALS` | Case Studies | Academic Consortium | English | JSON | `[NEEDS VERIFICATION]` | `[NEEDS VERIFICATION]` | Medium |
| `IndicLegalQA` | Case Studies | IIT KGP / OpenNYAI | En / Hi | JSON | `[NEEDS VERIFICATION]` | `[NEEDS VERIFICATION]` | Medium |
| `IN-Abs / IN-Ext` | Case Studies | IIT Kharagpur | English | TXT / JSON | 7,145 judgments | Academic Open Access (Verified) | Low |
| `CivilSum` | Case Studies | Academic NLP | English | JSONL | `[NEEDS VERIFICATION]` | `[NEEDS VERIFICATION]` | Medium |
| `Rhetorical-Roles` | Case Studies | OpenNYAI / SemEval | English | JSONL | 500+ deep judgments | `CC BY 4.0` (Verified) | Low |
| `DigiSCR-Portal` | Case Law | Supreme Court of India | En / Hi | Digital PDF | 36,000+ SCR reports | Public Domain / SCR (Verified) | Low |

