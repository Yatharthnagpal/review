# 02. Source Registry

**Document ID:** `LEGALAI-DOC-DE-02`  
**Version:** `1.2.2.1`  
**Status:** Canonical Audited Registry — Pending Independent Technical and Legal Review  
**Audited Date:** 2026-11-13  
**Dependencies:** `INDEX.md`, `03_LICENSE_AND_PROVENANCE_POLICY.md`, `PHASE_1_2_2_1_EVIDENCE_REGISTER.md`

---

## 1. Registry Architecture, Dimensions, and Governance Principles

This registry documents all candidate datasets, raw repositories, and official government data portals designated for evaluation or ingestion into the **LegalAI Data Platform**.

### 1.1 Governance Principles & Boundaries (LEG-122-02, SRC-122-01, HIGH-1222-01)
1. **Public Availability Fallacy:** Public accessibility of a web portal, regulatory filing, API, or scraping script **does not** imply permission to download, train on, or commercially redistribute data.
2. **Separation of Annotation Rights from Underlying Source Documents:** An open-source license covering dataset annotations (e.g., `CC BY 4.0`) does **not** convey a license to the underlying contracts or judgments. Both tiers must be audited independently.
3. **No Blanket Model-Training Inference:** Statutory non-infringement for reproducing raw court judgments under Copyright Act § 52(1)(q)(iv) does not automatically authorize commercial AI pretraining, fine-tuning, embedding generation, or RAG serving without formal legal assessment.
4. **No Universal Blanket Licensing:** Portals hosting legal materials (e.g., *India Code*) contain multiple distinct material classes (Acts, Rules, Gazette notices, Reports). A general portal policy (e.g., GODL India) does not supersede statutory conditions (such as Copyright Act § 52(1)(q)(ii)).

---

### 1.2 Structural Mapping: Registry Fields vs. Verification Dimensions vs. Operational Permissions (MED-1222-02)

To ensure transparency across documentation, validation, and operational data pipelines, the LegalAI data governance framework establishes a strict, traceable three-tier mapping:

```
+------------------------------------------------------------------------------------+
|                         LEGALAI DATA GOVERNANCE FRAMEWORK                          |
+------------------------------------------------------------------------------------+
| Tier 1: Registry Metadata Fields (What information is recorded - 14 Fields)        |
| Tier 2: Verification Dimensions   (What criteria are evaluated - 8 Dimensions)     |
| Tier 3: Operational Permissions   (What operations LegalAI evaluates - 10 Ops)     |
+------------------------------------------------------------------------------------+
```

#### Table 1.1: Structural Mapping Matrix
| # | Registry Metadata Field (Tier 1) | Corresponding Verification Dimension (Tier 2) | Granular Operational Permission Evaluated (Tier 3) | Purpose & Validation Standard |
|:---:|:---|:---|:---|:---|
| 1 | `source_id` | **Dataset Identity** | Metadata Tracking | Unique canonical identifier (e.g. `SRC-CONT-CUAD-01`). |
| 2 | `publisher_owner` | **Publisher Identity** | Provenance Verification | Verifies legal entity publishing the dataset. |
| 3 | `dataset_name` | **Dataset Identity** | Ingestion Scoping | Canonical academic or commercial title. |
| 4 | `repository_id` | **Endpoint Verification** | Pipeline Connectivity | Hugging Face ID, Git URL, or S3 bucket ARN. |
| 5 | `release_version` | **Release / Version** | Reproducibility | Tagged Git commit SHA or version snapshot. |
| 6 | `access_url` | **Endpoint Verification** | Automated Ingestion | Verified permanent download URI or portal URL. |
| 7 | `dataset_size` | **Technical Viability** | Storage & Compute Sizing | Record count, token estimate, and disk footprint. |
| 8 | `annotation_license` | **License Verification** | **Operational Op 1–6 (Annotations)** | Confirmed license for labels/spans (e.g., CC BY 4.0). |
| 9 | `underlying_license` | **License Verification** | **Operational Op 1–10 (Underlying Text)** | Rights status of raw underlying contracts/cases. |
| 10 | `commercial_use_status` | **Commercial Rights** | **Operational Op 6, 9, 10** | Commercial SaaS serving and distribution bounds. |
| 11 | `redistribution_status`| **Redistribution Rights** | **Operational Op 10** | Raw or processed public redistribution limits. |
| 12 | `training_use_status` | **Training Rights** | **Operational Op 7, 8** | Supervised fine-tuning vs. pretraining permissions. |
| 13 | `verification_date` | **Audit Provenance** | Governance Timestamp | Date of latest audit against primary source. |
| 14 | `composite_status` | **Composite Sign-off** | Pipeline Gate Decision | `PASS`, `CONDITIONAL`, `NOT VERIFIED`, `EXCLUDED`. |

---

### 1.3 Granular 10-Operation Permissions Standard (HIGH-1222-01)
Every source ingested or evaluated by LegalAI is audited against 10 distinct technical operations:
1. **Op-01: Raw Collection:** Downloading raw documents from public/gated endpoints.
2. **Op-02: Raw Storage:** Persisting raw documents in isolated internal data lakes.
3. **Op-03: Text Extraction & Parsing:** Extracting text, layout structures, and OCR layers.
4. **Op-04: Chunking & Indexing:** Generating deterministic text chunks and lexical search indexes.
5. **Op-05: Embedding Generation:** Encoding text chunks into dense vector representations.
6. **Op-06: RAG Retrieval & Commercial Serving:** Querying indexes to serve real-time context in commercial SaaS.
7. **Op-07: Supervised Fine-Tuning (SFT):** Training model parameters on task-specific question-answer or clause pairs.
8. **Op-08: Pretraining / Continual Pretraining:** Updating base language model weights on unstructured corpora.
9. **Op-09: Model-Weight Distribution:** Publishing or distributing model weights derived from the corpus.
10. **Op-10: Dataset Redistribution:** Re-hosting or redistributing raw or processed dataset files to third parties.

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
* **Rights Separation & 10-Operation Analysis (LEG-122-02, MED-1222-01):**
  - **A. Dataset Annotations (Atticus Project) — `SRC-CONT-CUAD-01-A`:**
    - *License:* Creative Commons Attribution 4.0 International (`CC BY 4.0`).
    - *License Evidence:* Published in repository `LICENSE` file and NeurIPS 2021 proceedings.
    - *Op-01 to Op-05 (Processing & Indexing):* **PASS** (Permitted with attribution).
    - *Op-06 (RAG Serving):* **PASS** (Annotations may be retrieved with attribution).
    - *Op-07 (Supervised Fine-Tuning):* **PASS** (Permitted for clause extraction and classification).
    - *Op-08 (Pretraining):* **PASS** (Permitted).
    - *Op-09 (Model Weights Distribution):* **CONDITIONAL ON LEGAL REVIEW** (LIC-1222-01: CC BY 4.0 covers annotations; downstream model weight copyright and unencumbered commercial distribution status is an evolving legal question requiring counsel sign-off).
    - *Op-10 (Redistribution):* **PASS** (Permitted with CC BY 4.0 notice).
  - **B. Underlying Contract Documents (SEC EDGAR Filings) — `SRC-CONT-CUAD-01-C`:**
    - *Origin:* Material corporate agreements filed as exhibits under SEC Regulation S-K.
    - *Source Rights:* Regulatory filings on SEC EDGAR fulfill corporate disclosure obligations. The Atticus Project explicitly disclaims copyright warranty: *"The Atticus Project makes no representation or warranty regarding the copyright status of the underlying contracts."* Third-party corporate filers and counterparties retain underlying proprietary rights and trade secrets.
    - *Op-01 & Op-02 (Collection & Storage):* **CONDITIONAL / RESTRICTED** (Quarantined for internal research and evaluation only; no commercial distribution).
    - *Op-03 to Op-05 (Parsing, Indexing, Embeddings):* **CONDITIONAL** (Permitted internally for benchmark evaluation).
    - *Op-06 (Commercial RAG Serving of Contract Text):* **NOT VERIFIED / RESTRICTED** (LegalAI serving pipeline evaluates user-uploaded contracts, never serving raw CUAD contracts to end users).
    - *Op-07 & Op-08 (Model Training on Full Contract Text):* **PENDING LEGAL REVIEW** (Unwarranted by Atticus).
    - *Op-09 (Model Weights from Full Contract Text):* **PENDING LEGAL REVIEW**.
    - *Op-10 (Redistribution of Raw Contracts):* **STRICTLY PROHIBITED**.
* **Composite Verification Status:** **CONDITIONAL** (Annotations PASS; Underlying Contracts Restricted/Pending Review).
* **Outstanding Legal Concerns:** US corporate law drafting (Delaware/NY); requires adaptation to Indian Contract Act standards.

---

### 2.2 MAUD (Merger Agreement Understanding Dataset)
* **Source ID:** `SRC-CONT-MAUD-01`
* **Publisher / Owner:** The Atticus Project & American Bar Association (ABA) Private Target M&A Committee
* **Dataset Name:** Merger Agreement Understanding Dataset (MAUD)
* **Repository ID:** `TheAtticusProject/maud` | Hugging Face: `TheAtticusProject/maud`
* **Release / Version:** v1.0 (2023 Release)
* **Access URL:** `https://www.atticusprojectai.org/maud` | `https://huggingface.co/datasets/TheAtticusProject/maud`
* **Dataset Size:** 152 merger agreements; ~47,000 annotations spanning 92 deal point questions.
* **Verification Date:** 2026-11-13
* **Rights Separation & 10-Operation Analysis (LEG-122-02, MED-1222-01):**
  - **A. Dataset Annotations (Atticus Project & ABA) — `SRC-CONT-MAUD-01-A`:**
    - *License:* Creative Commons Attribution 4.0 International (`CC BY 4.0`).
    - *Op-01 to Op-07 (Processing, SFT, QA):* **PASS** (Permitted with attribution).
    - *Op-08 (Pretraining):* **PASS** (Permitted).
    - *Op-09 (Model Weights Distribution):* **CONDITIONAL ON LEGAL REVIEW** (LIC-1222-01: Model weight copyright status requires formal legal assessment).
    - *Op-10 (Redistribution):* **PASS** (Permitted with CC BY 4.0 attribution).
  - **B. Underlying Merger Agreements (SEC EDGAR Filings) — `SRC-CONT-MAUD-01-C`:**
    - *Origin:* Public merger agreements filed on SEC EDGAR.
    - *Source Rights:* Corporate disclosure exhibits; underlying rights retained by filing parties; unwarranted by Atticus Project.
    - *Op-01 & Op-02 (Collection & Storage):* **CONDITIONAL / RESTRICTED** (Quarantined for benchmark validation).
    - *Op-03 to Op-05 (Parsing, Indexing, Embeddings):* **CONDITIONAL** (Internal benchmark evaluation only).
    - *Op-06 (Commercial RAG Serving):* **PROHIBITED** (Raw contract text not served).
    - *Op-07 to Op-09 (Training on Raw Text & Weights):* **PENDING LEGAL REVIEW**.
    - *Op-10 (Raw Redistribution):* **STRICTLY PROHIBITED**.
* **Composite Verification Status:** **CONDITIONAL** (Annotations PASS; Underlying Agreements Restricted/Pending Review).

---

### 2.3 Atticus A-CoRD (Atticus Corpus of Reviewed Documents)
* **Source ID:** `SRC-CONT-ACORD-01`
* **Publisher / Owner:** The Atticus Project
* **Dataset Name:** Atticus Corpus of Reviewed Documents (A-CoRD)
* **Repository ID:** `[NOT VERIFIED: Standalone Hugging Face repository ID not independently confirmed]`
* **Release / Version:** Unknown
* **Access URL:** `https://www.atticusprojectai.org/`
* **License:** `[NOT VERIFIED]` (Missing standalone license file)
* **Composite Status:** **NOT VERIFIED / QUARANTINED** (Ingestion deferred; models rely strictly on verified CUAD and MAUD annotations).

---

### 2.4 ACORD Insurance Standards (Commercial Standards Body — EXCLUDED)
* **Source ID:** `SRC-EXCL-ACORD-01`
* **Publisher / Owner:** ACORD (Association for Cooperative Operations Research and Development)
* **Dataset Name:** ACORD Insurance Forms & Electronic Standards
* **License:** Proprietary / Copyrighted Commercial Standards
* **Commercial / Redistribution / Training Use:** **STRICTLY PROHIBITED** without executed commercial licensing agreement.
* **Composite Status:** **QUARANTINED / EXCLUDED** (High copyright risk; replaced with public domain Indian insurance forms from General Insurance Council of India - GIC).

---

## 3. Category B: Indian Statutory Repositories

### 3.1 Official India Code (Government of India)
* **Source ID:** `SRC-STAT-INCODE-01`
* **Publisher / Owner:** Ministry of Law and Justice, Legislative Department, Government of India (Maintained by NIC)
* **Dataset Name:** India Code Digital Repository of Central and State Acts
* **Repository ID:** Official Government Portal (`https://www.indiacode.nic.in/`)
* **Release / Version:** Live Government Portal (Continuously updated)
* **Access URL:** `https://www.indiacode.nic.in/`
* **Dataset Size:** 850+ Central Acts, thousands of state enactments and subordinate rules.
* **Verification Date:** 2026-11-13
* **Material-Category Rights Disentanglement & 10-Operation Analysis (SRC-122-01, HIGH-1222-01):**
  - **Category 1: Central Acts of Parliament:**
    - *Statutory Authority:* Copyright Act, 1957, Section 52(1)(q)(ii).
    - *Legal Condition:* Reproduction is non-infringing **only when published together with commentary thereon or other original matter**.
    - *Op-01 to Op-05 (Collection, Storage, Parsing, Indexing):* **PASS** (Permitted internally).
    - *Op-06 (RAG Retrieval & Commercial Serving):* **CONDITIONAL ON LEGAL REVIEW** (Must be paired with original LegalAI structural commentary and risk analysis; standalone bare Acts restricted).
    - *Op-07 & Op-08 (Model Training / SFT):* **CONDITIONAL ON LEGAL REVIEW** (Text and data mining exceptions under Indian law require formal legal assessment; see *ANI Media v. OpenAI* interim order analysis in `03_LICENSE_AND_PROVENANCE_POLICY.md`).
    - *Op-09 (Model Weights):* **CONDITIONAL ON LEGAL REVIEW**.
    - *Op-10 (Bare Redistribution):* **RESTRICTED / PROHIBITED** (Redistribution permitted only with original analytical commentary).
  - **Category 2: Subordinate Legislation (Rules, Regulations, Notifications):**
    - *Statutory Authority:* Section 52(1)(q)(i) (Official Gazette matter other than Acts). Reproduction is non-infringing.
    - *Op-01 to Op-06:* **PASS**.
    - *Op-07 to Op-09 (Training & Weights):* **CONDITIONAL ON LEGAL REVIEW**.
    - *Op-10 (Redistribution):* **PASS** (Subject to Official Gazette attribution).
  - **Category 3: Portal Search Metadata, Taxonomies & UI Structure:**
    - *Authority:* Government Open Data License - India (GODL-India).
    - *Op-01 to Op-10:* **PASS** (Requires explicit attribution to NIC and disclaimer of government endorsement).
* **Composite Verification Status:** **CONDITIONAL (PENDING LEGAL REVIEW)**

---

### 3.2 KanoonGPT Indian Legal Documents
* **Source ID:** `SRC-STAT-KANOON-01`
* **Publisher / Owner:** KanoonGPT Community Contributors
* **Dataset Name:** KanoonGPT Indian Legal Documents Corpus
* **Repository ID:** `[NOT VERIFIED]`
* **Composite Status:** **NOT VERIFIED / QUARANTINED** (Website Terms of Service bar unauthorized bulk scraping and redistribution).

---

## 4. Category C: Indian Case Law Repositories & Judicial Corpora

### 4.1 AWS Registry of Open Data: Indian Supreme Court Judgments
* **Source ID:** `SRC-CASE-AWSSC-01`
* **Publisher / Owner:** Open Legal Data Community in collaboration with Registry of Open Data on AWS
* **Dataset Name:** Indian Supreme Court Judgments (1950–2023)
* **Repository ID:** AWS Open Data Registry (`indian-legal-judgments-sc`)
* **Release / Version:** 2023 Archive Snapshot
* **Access URL:** `https://registry.opendata.aws/` (S3 endpoint verification pending Sprint 2.1)
* **Legal Grounding:** Section 52(1)(q)(iv) Copyright Act, 1957; public court judgments (*Eastern Book Company v. D.B. Modak (2008) 1 SCC 1*).
* **Dataset Size:** ~35,000 full-text judgments; ~50 GB raw text/PDF.
* **10-Operation Permissions Analysis (HIGH-1222-01):**
  - *Op-01 & Op-02 (Raw Collection & Storage):* **PASS** (Public record judicial texts).
  - *Op-03 & Op-04 (Parsing, Chunking, Indexing):* **PASS** (Non-infringing under § 52(1)(q)(iv)).
  - *Op-05 (Embedding Generation):* **PASS** (Mathematical representation for search).
  - *Op-06 (RAG Retrieval & Commercial Serving):* **CONDITIONAL ON LEGAL REVIEW** (Judicial texts are non-infringing, but downstream commercial SaaS deployment must verify non-infringement of editorial additions and ensure mandatory statutory redaction under BNS § 73 and POCSO § 24(5)/33(7)).
  - *Op-07 & Op-08 (Supervised Fine-Tuning & Pretraining):* **CONDITIONAL ON LEGAL REVIEW** (Public record status does not automatically create an express statutory AI training exception under Indian copyright law; see `03_LICENSE_AND_PROVENANCE_POLICY.md` § 2.2).
  - *Op-09 (Model-Weight Distribution):* **CONDITIONAL ON LEGAL REVIEW**.
  - *Op-10 (Redistribution):* **PASS** (Subject to strict PII and victim identity redaction).
* **Composite Verification Status:** **CONDITIONAL** (Legal basis verified; exact S3 bucket sync and manifest verification pending Sprint 2.1).

---

### 4.2 AWS Registry of Open Data: Indian High Court Judgments
* **Source ID:** `SRC-CASE-AWSHC-01`
* **Publisher / Owner:** Open Legal Data Community on AWS Open Data
* **Dataset Name:** Indian High Court Judgments Archive
* **Repository ID:** AWS Open Data Registry (`indian-high-courts`)
* **Dataset Size:** ~2.5 million records across 25 High Courts (~400 GB).
* **10-Operation Permissions Analysis (HIGH-1222-01):**
  - *Op-01 to Op-05 (Collection, Storage, Parsing, Indexing, Embeddings):* **PASS** (Verbatim judicial text under § 52(1)(q)(iv)).
  - *Op-06 (RAG Serving):* **CONDITIONAL ON LEGAL REVIEW** (Requires PII/POCSO filtering and legal opinion).
  - *Op-07 & Op-08 (SFT & Pretraining):* **CONDITIONAL ON LEGAL REVIEW**.
  - *Op-09 (Model Weights):* **CONDITIONAL ON LEGAL REVIEW**.
  - *Op-10 (Redistribution):* **RESTRICTED** (Subject to High Court electronic record rules and privacy screening).
* **Composite Verification Status:** **CONDITIONAL** (Pending endpoint confirmation and volume filtering).

---

### 4.3 Official Supreme Court Digital SCR (DigiSCR Portal)
* **Source ID:** `SRC-CASE-DIGISCR-01`
* **Publisher / Owner:** Supreme Court of India & Department of Justice, Government of India
* **Dataset Name:** Supreme Court Reports Digital Archive (DigiSCR)
* **Repository ID:** Official Supreme Court Portal (`https://digiscr.sci.gov.in/`)
* **Legal Grounding:** Section 52(1)(q)(iv) Copyright Act, 1957; official Supreme Court Reports. Cited in Evidence Register as `EVID-SRC-13`.
* **Dataset Size:** 36,000+ judgments published in official Supreme Court Reports (1950 to 2024).
* **10-Operation Permissions Analysis (HIGH-1222-01):**
  - *Op-01 to Op-05 (Collection, Storage, Verbatim Text Parsing, Indexing):* **PASS** (Verbatim judicial text is public record).
  - *Op-06 (Commercial RAG Serving):* **CONDITIONAL ON LEGAL REVIEW** (Layout parser must filter out official SCR editorial headnotes under *Eastern Book Company*; verbatim text non-infringing).
  - *Op-07 & Op-08 (SFT & Pretraining):* **CONDITIONAL ON LEGAL REVIEW** (Restricted to verbatim text; editorial headnotes strictly excluded).
  - *Op-09 (Model Weights):* **CONDITIONAL ON LEGAL REVIEW**.
  - *Op-10 (Redistribution):* **PASS** (Verbatim text only, with official SCR citation).
* **Composite Verification Status:** **PASS (for verbatim text) / CONDITIONAL (for AI training & commercial RAG)**.

---

### 4.4 Indian Legal Rhetorical Roles Corpus (OpenNYAI / SemEval-2023 Task 6)
* **Source ID:** `SRC-CASE-OPENNYAI-01`
* **Publisher / Owner:** OpenNYAI Team (Vijit Malik, Rishabh Sharma, et al.)
* **Dataset Name:** Indian Legal Rhetorical Roles Corpus
* **Repository ID:** `opennyaiorg/rhetorical-roles` | `https://github.com/OpenNYAI/OpenNYAI`
* **Code License:** MIT License | **Dataset Annotations License:** Creative Commons Attribution 4.0 International (`CC BY 4.0`).
* **Underlying Text:** Public High Court and Supreme Court judgments (§ 52(1)(q)(iv)).
* **10-Operation Permissions Analysis:**
  - *Op-01 to Op-07 (Processing, Embeddings, SFT on Annotations):* **PASS** (Full CC BY 4.0 permission with attribution).
  - *Op-08 & Op-09 (Pretraining & Model Weights):* **PASS** (Permitted with attribution).
  - *Op-10 (Redistribution):* **PASS** (Permitted with CC BY 4.0 notice).
* **Composite Verification Status:** **PASS**.

---

### 4.5 IN-Abs / IN-Ext (Indian Legal Summarization Corpus)
* **Source ID:** `SRC-CASE-INABS-01`
* **Publisher / Owner:** Paheli Bhattacharya et al. (IIT Kharagpur)
* **Dataset Name:** IN-Abs and IN-Ext Legal Document Summarization Corpora
* **Repository ID:** `https://github.com/Law-AI/summarization`
* **Code License:** Apache License 2.0 | **Summaries / Headnotes:** Academic Research License.
* **Underlying Text:** Supreme Court of India judgments (public record).
* **10-Operation Permissions Analysis (HIGH-1222-01):**
  - *Op-01 to Op-05 (Internal Processing & Evaluation):* **PASS**.
  - *Op-06 (Commercial RAG Serving of Summaries):* **CONDITIONAL / RESTRICTED** (Law reporter headnote summaries are protected copyright under *Eastern Book Company*).
  - *Op-07 (SFT on Summaries):* **CONDITIONAL / ACADEMIC RESEARCH ONLY** (Commercial fine-tuning requires clearance of headnote copyright).
  - *Op-08 to Op-10:* **RESTRICTED** (Redistribution permitted for academic research only).
* **Composite Verification Status:** **PASS (for Research / Benchmark) / CONDITIONAL (for Commercial Deployment)**.

---

### 4.6 KanoonGPT Indian Case Laws
* **Source ID:** `SRC-CASE-KANOON-02`
* **Composite Status:** **NOT VERIFIED / QUARANTINED** (Website ToS boundaries and risk of unredacted sensitive cases).

---

## 5. Category D: Bilingual & Case Reasoning Corpora

### 5.1 LegalTransEn Indic
* **Source ID:** `SRC-BIL-TRANS-01`
* **Composite Status:** **NOT VERIFIED / QUARANTINED** (Missing standalone Hub repository; bilingual corpora sourced from official gazettes).

### 5.2 BhashaBench-Legal
* **Source ID:** `SRC-BIL-BHASHA-01`
* **Publisher / Owner:** National Language Translation Mission (NLTM) / Bhashini / MeitY
* **Dataset Name:** BhashaBench Legal Evaluation Benchmark
* **Dataset Size:** ~5,000 evaluation QA pairs.
* **10-Operation Permissions Analysis:**
  - *Op-01 to Op-05 (Gated Evaluation Processing):* **PASS** (Under Bhashini evaluation credentials).
  - *Op-06 (Commercial Serving):* **PROHIBITED** (Blind evaluation benchmark).
  - *Op-07 & Op-08 (Model Training / SFT / Pretraining):* **STRICTLY PROHIBITED** (Contamination prevention rule).
  - *Op-09 & Op-10 (Model Weights & Redistribution):* **STRICTLY PROHIBITED**.
* **Composite Verification Status:** **CONDITIONAL (GATED EVALUATION ONLY — TRAINING PROHIBITED)**.

### 5.3 FIRAC-APPEALS, IndicLegalQA, CivilSum
* `SRC-CASE-FIRAC-01`, `SRC-CASE-INDQA-01`, `SRC-CASE-CIVSUM-01`: **NOT VERIFIED / QUARANTINED**.

---

## 6. Granular Operational Permissions Matrix (10 Technical Operations)

The table below provides the authoritative operational status across all 10 technical operations for LegalAI candidate sources:

| Source ID | Short Name | Op-01 Coll | Op-02 Stor | Op-03 Parse | Op-04 Index | Op-05 Embed | Op-06 RAG | Op-07 SFT | Op-08 Pretrain | Op-09 Weights | Op-10 Redist | Composite Status | Pipeline Ingestion Rule |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `SRC-CONT-CUAD-01-A` | CUAD Annotations | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | COND | PASS | **PASS / COND** | Approved for training (CC BY 4.0); model weights COND on review |
| `SRC-CONT-CUAD-01-C` | CUAD Underlying Contracts | COND | COND | COND | COND | COND | REST | COND | COND | COND | PROHIB | **CONDITIONAL** | Internal benchmark quarantine only; no commercial serving/redist |
| `SRC-CONT-MAUD-01-A` | MAUD Annotations | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | COND | PASS | **PASS / COND** | Approved for training (CC BY 4.0); model weights COND on review |
| `SRC-CONT-MAUD-01-C` | MAUD Underlying Contracts | COND | COND | COND | COND | COND | PROHIB | COND | COND | COND | PROHIB | **CONDITIONAL** | Internal benchmark quarantine only |
| `SRC-EXCL-ACORD-01` | ACORD Standards | PROHIB| PROHIB| PROHIB| PROHIB| PROHIB| PROHIB| PROHIB| PROHIB| PROHIB| PROHIB| **EXCLUDED** | **Excluded / Commercial copyright** |
| `SRC-STAT-INCODE-01` | India Code Central Acts | PASS | PASS | PASS | PASS | PASS | COND | COND | COND | COND | REST | **CONDITIONAL** | Approved (Commentary condition & TDM pending legal review) |
| `SRC-CASE-AWSSC-01` | AWS Supreme Court Judgments | PASS | PASS | PASS | PASS | PASS | COND | COND | COND | COND | PASS | **CONDITIONAL** | Approved (S3 sync pending; training conditional on review) |
| `SRC-CASE-AWSHC-01` | AWS High Court Judgments | PASS | PASS | PASS | PASS | PASS | COND | COND | COND | COND | REST | **CONDITIONAL** | Approved (Volume filter pending; training conditional on review)|
| `SRC-CASE-DIGISCR-01`| Supreme Court DigiSCR Archive | PASS | PASS | PASS | PASS | PASS | COND | COND | COND | COND | PASS | **PASS / COND** | Approved (Verbatim text PASS; official headnotes filtered) |
| `SRC-CASE-OPENNYAI-01`| OpenNYAI Rhetorical Roles | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** | Approved for rhetorical role classification |
| `SRC-CASE-INABS-01` | IN-Abs / IN-Ext Summaries | PASS | PASS | PASS | PASS | PASS | COND | COND | REST | COND | REST | **PASS / COND** | Approved for evaluation; commercial fine-tuning conditional |
| `SRC-BIL-BHASHA-01` | BhashaBench Legal Benchmark | PASS | PASS | PASS | PASS | PASS | PROHIB| PROHIB| PROHIB| PROHIB| PROHIB| **CONDITIONAL** | **Gated Evaluation Only (Training Strictly Barred)** |

*Key: PASS = Permitted under verified license or statute; COND = Conditional on independent legal review or operational test; REST = Restricted to internal evaluation or original matter pairing; PROHIB = Statutorily or contractually prohibited.*
