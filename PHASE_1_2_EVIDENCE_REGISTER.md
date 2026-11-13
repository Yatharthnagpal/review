# Phase 1.2 Evidence Register

**Document ID:** `LEGALAI-DOC-DE-EVIDENCE-1.2`  
**Version:** `1.0.0`  
**Status:** Canonical Evidence Base  
**Date:** 2026-11-13  
**Target Platform:** LegalAI (Indian Legal Intelligence Platform)

---

## 1. Executive Summary

This register serves as the authoritative, central evidence ledger supporting all legal interpretations, dataset source metadata, technical architecture assertions, and privacy governance rules in the **LegalAI Data Platform**.

Every claim verified in Phase 1.2 is cross-referenced against primary sources (official Indian government gazettes, codified statutory enactments, Supreme Court of India law reports, official dataset repositories, and the inspected local application codebase). Claims where primary evidence is incomplete or inaccessible are explicitly recorded as **NOT VERIFIED**.

---

## 2. Legal Evidence Ledger

### EVID-LEG-01: Official Languages Act, 1963 — Section 5 & Constitutional Scheme
* **Primary Authority:** The Official Languages Act, 1963 (Act No. 19 of 1963), Section 5; Constitution of India, Articles 343 & 348.
* **Official Source URL:** `https://legislative.gov.in/sites/default/files/A1963-19.pdf`
* **Exact Statutory Text:**
  > **Section 5(1):** *"A translation in Hindi published under the authority of the President in the Official Gazette on and after the appointed day—*  
  > *(a) of any Central Act or of any Ordinance promulgated by the President, or*  
  > *(b) of any order, rule, regulation or bye-law issued under the Constitution or under any Central Act,*  
  > *shall be deemed to be the authoritative text thereof in Hindi."*
* **What the Source Establishes:** Section 5(1) establishes an evidentiary and authoritative legal rule: when a Hindi translation of a Central Act, Ordinance, or subordinate rule is published in the Official Gazette under the authority of the President, it is legally recognized as the "authoritative text thereof in Hindi".
* **What the Source Does NOT Establish:** Section 5 does **not** impose an automatic, self-executing universal obligation that every Central Act, state law, ordinance, or administrative notification must immediately have an authorized Hindi translation published simultaneously. Under Article 348(1)(b) of the Constitution of India, the authoritative text of all Parliamentary Acts, Bills, and Ordinances remains in the English language until Parliament by law otherwise provides.
* **Impact on LegalAI Dataset Assumptions:** Dataset ingestion pipelines cannot assume that every one of India's 850+ Central Acts or subordinate rules has a matching authoritative Hindi translation. Bilingual parallel corpora must be constructed from available authorized translations published by *Vidhi Sahitya Prakashan* (Legislative Department), acknowledging that coverage is selective and ongoing, not universal.
* **Verification Finding:** **PASS** (Statutory scope accurately limited and qualified).

---

### EVID-LEG-02: Digital Personal Data Protection Act, 2023 — Section 16 & Phased Commencement
* **Primary Authority:** The Digital Personal Data Protection Act, 2023 (Act No. 22 of 2023), Section 1(2) & Section 16; Gazette of India Notification S.O. dated 13 November 2025.
* **Official Source URL:** `https://www.meity.gov.in/writereaddata/files/Digital%20Personal%20Data%20Protection%20Act%202023.pdf`
* **Exact Statutory Text:**
  > **Section 16(1):** *"The Central Government may, by notification, restrict the transfer of personal data by a Data Fiduciary for processing to such country or territory outside India as may be so notified."*  
  > **Section 16(2):** *"Nothing contained in this section shall restrict the applicability of any law for the time being in force in India that provides for a higher degree of protection for or restriction on transfer of personal data by a Data Fiduciary outside India in relation to any personal data or Data Fiduciary or class thereof."*
* **What the Source Establishes:** Section 16 adopts a "blacklist" or "negative list" model: Data Fiduciaries are generally permitted to transfer personal data cross-border *unless* the target country or territory is explicitly restricted by Central Government notification, subject to stricter sectoral laws (e.g., Reserve Bank of India storage requirements for payment system data).
* **What the Source Does NOT Establish:** Section 16 does **not** mandate blanket, universal data localization within India for all personal data or database volumes.
* **Commencement Status:** Under Section 1(2), the Act comes into force on appointed dates. Gazette notification dated 13 November 2025 schedules substantive operational provisions (Sections 3 to 17, including Section 16) for commencement 18 months following publication. Therefore, Section 16 is scheduled for future legal effect and is not currently in force as an operational restriction.
* **Impact on LegalAI Architecture:** LegalAI's requirement to host Qdrant, PostgreSQL, and Parquet volumes in data centers within India is an **internal risk-management policy and voluntary sovereign infrastructure choice**, NOT a universal statutory mandate under Section 16.
* **Verification Finding:** **PASS** (Localization claim reclassified as voluntary internal architecture policy; commencement timeline documented).

---

### EVID-LEG-03: Family Courts Act, 1984 — Section 11 & Matrimonial In-Camera Proceedings
* **Primary Authority:** The Family Courts Act, 1984 (Act No. 66 of 1984), Section 11.
* **Official Source URL:** `https://legislative.gov.in/sites/default/files/A1984-66_0.pdf`
* **Exact Statutory Text:**
  > **Section 11:** *"In every suit or proceedings to which this Act applies, the proceedings may be held in camera if the Family Court so desires and shall be so held if either party so desires."*
* **What the Source Establishes:** In-camera hearings in Family Courts are discretionary upon the court's motion and mandatory if either party requests. Where an in-camera order is passed, proceedings and transcripts are confidential.
* **What the Source Does NOT Establish:** Section 11 does **not** declare that every family court decree, final appellate High Court matrimonial judgment, or general family court file is automatically confidential, secret, or subject to blanket statutory anonymization by default.
* **Impact on LegalAI Ingestion Policy:** Family-court records cannot be handled via sweeping assumptions. Ingestion pipelines must enforce a **case-by-case review protocol**: judgments explicitly conducted in-camera, involving juvenile custody disputes, or containing sensitive allegations require full redaction or exclusion, whereas reported High Court and Supreme Court matrimonial jurisprudence delivered in open court remains public record subject to victim privacy safeguards.
* **Verification Finding:** **PASS** (Discretionary in-camera threshold clarified; case-by-case audit established).

---

### EVID-LEG-04: Indian Copyright Act, 1957 — Section 52(1)(q) Multi-Tiered Analysis
* **Primary Authority:** The Copyright Act, 1957 (Act No. 14 of 1957), Section 52(1)(q); *Eastern Book Company v. D.B. Modak (2008) 1 SCC 1*.
* **Official Source URL:** `https://copyright.gov.in/documents/copyrightrules1957.pdf`
* **Exact Statutory Text:**
  > **Section 52(1)(q):** The following acts shall not constitute an infringement of copyright, namely:  
  > *(i) the reproduction or publication of any matter which has been published in any Official Gazette except an Act of a Legislature;*  
  > *(ii) the reproduction or publication of any Act of a Legislature unless such reproduction or publication is accompanied by any commentary or other original matter;*  
  > *(iv) the reproduction or publication of any judgment or order of a court, tribunal or other judicial authority, unless the reproduction or publication of such judgment or order is prohibited by the court, tribunal or other judicial authority, as the case may be.*
* **What the Source Establishes:** Pure statutory enactments and raw judicial opinions are exempt from copyright infringement claims.
* **Multi-Tier Classification of Legal Materials:**
  1. **Bare Statutory Text:** Non-infringing under § 52(1)(q)(ii). Full reproduction, chunking, and indexing permitted.
  2. **Official Gazette Enactments:** Non-infringing under § 52(1)(q)(i). Public domain.
  3. **Raw Judicial Opinions:** Non-infringing under § 52(1)(q)(iv). Public domain per *Eastern Book Company*.
  4. **Editorial Annotations & Section Comments:** Copyrighted by publisher/author. Ingestion prohibited without license.
  5. **Law Reporter Headnotes & Catchwords:** Copyrighted under the "modicum of creativity" standard (*Eastern Book Company*). Excluded from ingestion.
  6. **Commercial Legal Databases (SCC Online, Manupatra):** Database compilations and search features protected by contract and database rights. Scraping prohibited under portal Terms of Service.
  7. **Private Translations:** Translations of statutes or judgments prepared by private authors or publishers enjoy independent copyright protection under Section 13(1)(a) as derivative literary works. Only translations published under Presidential authority in the Official Gazette fall under official public status.
* **Verification Finding:** **PASS** (Multi-tiered statutory analysis formalized; private translations and commercial databases protected).

---

## 3. Dataset Source and Licensing Evidence Ledger

### EVID-SRC-01: Atticus A-CoRD (Atticus Corpus of Reviewed Documents)
* **Dataset Name:** Atticus Corpus of Reviewed Documents (A-CoRD)
* **Publisher / Owner:** The Atticus Project (Prof. Dan Hendrycks et al.)
* **Hugging Face / Zenodo / GitHub Endpoint:** The Atticus Project has published CUAD (`TheAtticusProject/cuad`) and MAUD (`TheAtticusProject/maud`). However, an independently released, standalone Hugging Face repository under the explicit identifier `TheAtticusProject/acord` or `a-cord` is **NOT VERIFIED** as an active public Hub repository.
* **License File & Evidence:** Not verified independently for an "A-CoRD" standalone Hub release. While Atticus Project research artifacts are typically released under `CC BY 4.0`, asserting a confirmed license for an unlocated standalone Hub release is procedurally improper.
* **Operational Determination:** **NOT VERIFIED**. The dataset cannot be marked verified in the source registry. Base contract clause classification must rely on verified **CUAD** (`TheAtticusProject/cuad`, NeurIPS 2021, `CC BY 4.0`) and **MAUD** (`TheAtticusProject/maud`, 2023, `CC BY 4.0`).
* **Verification Finding:** **NOT VERIFIED** (Marked NOT VERIFIED in `02_SOURCE_REGISTRY.md`; claims of verified size and license removed).

---

### EVID-SRC-02: LegalTransEn
* **Dataset Name:** LegalTransEn Indic
* **Claimed Publisher:** AI4Bharat / IndicNLP / Community
* **Investigation:** AI4Bharat has released **IndicTrans2** (`ai4bharat/indictrans2-indic-en-1B`) and general multi-domain evaluation sets. While AI4Bharat research papers describe domain evaluation on judicial translation, an independent standalone repository explicitly named "LegalTransEn" with public open-access parquet splits on Hugging Face is **NOT VERIFIED**.
* **Operational Determination:** **NOT VERIFIED**. The dataset must not be marked verified. Cross-lingual parallel statutory corpora will be sourced directly from official Government of India parallel gazette enactments (*India Code* + *Vidhi Sahitya Prakashan*) and verified subsets of IndicTrans2 documentation.
* **Verification Finding:** **NOT VERIFIED** (Reclassified in `02_SOURCE_REGISTRY.md`).

---

### EVID-SRC-03: KanoonGPT
* **Claimed Publisher:** KanoonGPT Contributors
* **Investigation:** KanoonGPT exists as an online AI legal service / interface. The provider's terms and conditions prohibit unauthorized scraping, bulk ingestion, or unauthorized redistribution of underlying indices.
* **Operational Determination:** **NOT VERIFIED / QUARANTINED**. No evidence of an open-access commercial redistribution license. Raw scraping from KanoonGPT is excluded.
* **Verification Finding:** **NOT VERIFIED** (Quarantine preserved).

---

### EVID-SRC-04: AWS Registry of Open Data — Supreme Court & High Court Judgments
* **Publisher:** Hosted on AWS Open Data (OpenNYAI / Community Legal Data initiatives)
* **Registry URI:** `https://registry.opendata.aws/` (Dataset tags: `legal`, `indian-law`)
* **Legal Basis:** Section 52(1)(q)(iv) of Copyright Act, 1957; official public records of the Supreme Court and 25 High Courts.
* **Operational Determination:** **CONDITIONAL**. The legal status of the underlying judgments is verified public domain; exact S3 bucket ARN (`s3://...`) requires network synchronization and authentication check in Phase 2.
* **Verification Finding:** **CONDITIONAL** (Legal basis PASS; bucket endpoint CONDITIONAL).

---

## 4. Codebase Reality Evidence Ledger

Inspected codebase root: `c:\Users\Yatharth nagpal\Desktop\LegalAI-main\backend\app\`

| Component Symbol | Exact File Path | Verified Line Range | Actual Code Status | Reality Finding |
| :--- | :--- | :--- | :--- | :--- |
| `VectorDBService` | `backend/app/services/vector_db.py` | Lines 12–262 | Singleton class initializing local Qdrant at `qdrant_data/`, FastEmbed `BAAI/bge-small-en-v1.5` (384-dim), collections `clauses` & `statutes`. | **EXISTING (PASS)** |
| `log_audit()` | `backend/app/services/audit.py` | Lines 7–21 | Function accepting `(db, action, details, user_id, ip_address)` and inserting into `AuditLog`. | **EXISTING (PASS)** |
| `AuditLog` Model | `backend/app/models/db_models.py` | Lines 86–94 | SQLAlchemy table `audit_logs` with columns `id`, `user_id`, `action`, `details`, `ip_address`, `created_at`. No `resource_type` or `resource_id` columns exist. | **EXISTING (PASS)** |
| `generate_chat_response` | `backend/app/services/nlu.py` | Lines 357–415 | Sequential 3-prompt chain: Analyst Agent $\rightarrow$ Compliance Expert $\rightarrow$ General Counsel. No autonomous agent framework or tool-calling loop exists. | **PARTIAL (PASS)** |
| `search_statutes()` | `backend/app/services/vector_db.py` | Lines 210–240 | Dense cosine similarity search in local Qdrant collection; no sparse BM25, reranker, or citation verifier exists. | **PARTIAL (PASS)** |
| `ClauseType` Enum | `backend/app/models/schemas.py` | Lines 21–43 | Canonical 21 clause types (`Payment`, `Termination`, ..., `Penalty`, `Other`). | **EXISTING (PASS)** |
| `RiskLevel` Enum | `backend/app/models/schemas.py` | Lines 14–19 | Canonical 4 risk levels (`low`, `medium`, `high`, `critical`). | **EXISTING (PASS)** |
| Transformer Training | N/A | N/A | No model training scripts, fine-tuning harnesses, or PyTorch trainers exist in the repository. | **PLANNED (PASS)** |
| Multilingual Embedder | N/A | N/A | Local embeddings strictly use 384-dim English `bge-small-en-v1.5`. No `bge-m3` or Indic embedder currently loaded. | **PLANNED (PASS)** |

---

## 5. Technical Specification Evidence Ledger

### EVID-SCH-01: Pydantic v2.10+ and JSON Schema Dialect
* **Inspected Environment:** Pydantic v2.10.4 installed (`pydantic>=2.10.4` in `backend/requirements.txt`).
* **Technical Reality:** Pydantic v2's `.model_json_schema()` generates schemas conforming to **JSON Schema Draft 2020-12** (Core/Validation) and OpenAPI 3.1.0 specifications. It does **not** natively emit Draft-07 schemas.
* **Resolution:** Documentation updated to formally specify **JSON Schema Draft 2020-12** as the native canonical dialect. A Draft-07 compatibility transformation is documented for downstream systems that require legacy validator compatibility.
* **Verification Finding:** **PASS**.

### EVID-ML-01: Leakage Metrics & False Positive Claims
* **Previous Claim:** "0% false positive cluster merges in MinHash LSH".
* **Evidence Check:** No human-labeled ground truth duplicate evaluation has been run on LegalAI contract data. Stating a 0% false positive rate was an unsupported theoretical assumption, not an empirical result.
* **Resolution:** Removed the 0% claim. Defined the formal duplicate evaluation protocol, sample size, and metric calculations (Precision, Recall, F1) to be executed during Sprint 2.3. Marked metric status as **NOT RUN**.
* **Verification Finding:** **PASS** (Unsupported claim removed; empirical protocol documented).

### EVID-ML-02: Cross-Lingual Semantic Cosine Threshold (0.88)
* **Previous Claim:** Universal cross-lingual translation leakage threshold asserted at 0.88.
* **Evidence Check:** Threshold was proposed without an empirical threshold sweep across parallel Indic corpora.
* **Resolution:** Reclassified 0.88 as a **provisional hypothesis**. Documented an empirical calibration protocol evaluating candidate thresholds (0.80, 0.84, 0.88, 0.92) against human-annotated parallel pairs during Phase 2. Marked metric status as **NOT RUN**.
* **Verification Finding:** **PASS**.

