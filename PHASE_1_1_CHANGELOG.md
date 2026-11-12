# Phase 1.1 Changelog: Traceable Revisions Record

**Document ID:** `LEGALAI-DOC-DE-CHANGELOG-1.1`  
**Version:** `1.0.0`  
**Status:** Complete & Audited  
**Date:** 2026-11-12  
**Target Platform:** LegalAI (Indian Legal Intelligence Platform)

---

## 1. Overview of Revisions

Phase 1.1 executed a controlled, in-place revision across all 15 initial dataset engineering documents under `docs/dataset-engineering/` to resolve factual, legal, architectural, data-governance, and cross-document inconsistencies. No existing source code in `frontend/` or `backend/` was altered, no dependencies were installed, and no datasets were downloaded.

---

## 2. Document-by-Document Change Ledger

### 2.1 `INDEX.md`
* **Original Issue:** Claimed project status was "Approved for Implementation" despite Phase 1 rule requiring pause for review; listed multi-agent orchestration and production RAG as existing capabilities without codebase audit.
* **Correction Made:** 
  1. Updated status to `Draft v1.0 — Pending Technical and Legal Review`.
  2. Added Codebase Verification table classifying components into `Existing`, `Partial`, `Planned`, `Missing`, or `Unverified`.
  3. Added the four new Phase 1.1 tracking and sign-off documents to the document matrix.
* **Reason for Correction:** Maintain accurate governance status and align architectural claims with the actual repository code.
* **Evidence / Source:** Inspection of `backend/app/main.py`, `models/schemas.py`, `models/db_models.py`, `services/nlu.py`, and `services/vector_db.py`.
* **Affected Documents:** `INDEX.md`, `01_DATASET_ARCHITECTURE.md`, `14_DATASET_IMPLEMENTATION_ROADMAP.md`.
* **Remaining Concerns:** None.
* **Review Status:** Resolved.

### 2.2 `01_DATASET_ARCHITECTURE.md`
* **Original Issue:** Described multi-agent orchestration as an existing runtime component; cited 9 NER entities instead of 11; did not note the phased commencement of DPDP Act; conflated Section 73 and Section 74 in rule engine descriptions.
* **Correction Made:**
  1. Updated runtime engine topology diagram to annotate component status (`Existing` vs. `Partial -> Target`).
  2. Corrected legal entity recognition count to 11 canonical types.
  3. Differentiated Section 73 (unliquidated damages) and Section 74 (liquidated damages / penalties).
  4. Clarified that 1024-dim multilingual embeddings are a Phase 2/3 target, retaining current 384-dim FastEmbed.
* **Reason for Correction:** Architectural and legal precision.
* **Evidence / Source:** Codebase inspection of `backend/app/services/vector_db.py` (line 33) and `nlu.py` (line 357); Indian Contract Act, 1872.
* **Affected Documents:** `01_DATASET_ARCHITECTURE.md`, `04_CANONICAL_DATA_SCHEMAS.md`, `05_LABEL_TAXONOMY.md`.
* **Remaining Concerns:** None.
* **Review Status:** Resolved.

### 2.3 `02_SOURCE_REGISTRY.md`
* **Original Issue:** Conflated Atticus A-CoRD with commercial insurance standards organization ACORD; lacked standard 14-field metadata schema; did not clearly state KanoonGPT Terms of Service restrictions; misquoted Section 52(1)(q).
* **Correction Made:**
  1. Standardized all dataset entries to the 14-field metadata template (publisher, version, language, format, license, attribution, commercial restrictions, redistribution, training permissions, access, date, status, legal concerns).
  2. Decoupled Atticus A-CoRD (`CC BY 4.0`) from ACORD Insurance Standards (proprietary commercial standard).
  3. Explicitly excluded and quarantined proprietary ACORD insurance forms, substituting public-domain Indian General Insurance Council (GIC) forms.
  4. Explicitly documented that public web access to KanoonGPT does not grant automated scraping or redistribution rights.
  5. Accurately cited Section 52(1)(q) sub-clauses (i), (ii), and (iv).
* **Reason for Correction:** Elimination of copyright infringement risk and standard-setting accuracy.
* **Evidence / Source:** Atticus Project publications (Hendrycks et al. 2021); ACORD.org Terms; Indian Copyright Act, 1957.
* **Affected Documents:** `02_SOURCE_REGISTRY.md`, `03_LICENSE_AND_PROVENANCE_POLICY.md`.
* **Remaining Concerns:** Upstream S3 bucket names for AWS Open Data High Courts require network validation in Phase 2.
* **Review Status:** Resolved.

### 2.4 `03_LICENSE_AND_PROVENANCE_POLICY.md`
* **Original Issue:** Conflated BNS Section 72 and Section 73; stated that salted SHA-256 hashing produces anonymized data; did not qualify DPDP Act phased commencement; misquoted Section 52(1)(q).
* **Correction Made:**
  1. Precisely distinguished BNS Section 72 (disclosure of victim identity in sexual offenses, formerly IPC §228A) from Section 73 (printing or publishing in-camera court proceedings without permission).
  2. Cited POCSO Act Sections 24(5), 33(7), 23, and 37; Family Courts Act Section 11.
  3. Accurately quoted Section 52(1)(q) sub-clauses (i), (ii), and (iv).
  4. Clarified that salted hashing is **pseudonymization**, NOT irreversible anonymization, under DPDP and GDPR guidance.
  5. Documented DPDP Act Section 1(2) phased commencement.
* **Reason for Correction:** Strict compliance with Indian criminal, copyright, and privacy jurisprudence.
* **Evidence / Source:** The Bharatiya Nyaya Sanhita, 2023 (Act No. 45 of 2023); The Digital Personal Data Protection Act, 2023 (Act No. 22 of 2023); *Eastern Book Company v. D.B. Modak (2008) 1 SCC 1*.
* **Affected Documents:** `03_LICENSE_AND_PROVENANCE_POLICY.md`, `13_DATA_PRIVACY_AND_GOVERNANCE.md`.
* **Remaining Concerns:** Qualified Indian legal review required before production launch.
* **Review Status:** Resolved.

### 2.5 `04_CANONICAL_DATA_SCHEMAS.md`
* **Original Issue:** Used `RiskSeverity` and `ClauseCategory` which diverged from existing backend code (`RiskLevel` and `ClauseType`); lacked perspective lens in core schemas; lacked character offset definitions (bytes vs code points); lacked embedding metadata; conflated model analysis with ground truth in hypothetical case studies.
* **Correction Made:**
  1. Harmonized canonical enums to `ClauseType` and `RiskLevel` matching `backend/app/models/schemas.py`, while retaining functional aliases.
  2. Standardized text offsets to **0-based Unicode code points** on normalized text.
  3. Added `PerspectiveLens` (`party_a`, `party_b`, `neutral`) to `ContractClauseRecord` and `ContractRiskRecord`.
  4. Replaced `model_analysis` with `reference_analysis` in `HypotheticalCaseStudyRecord` and added `is_synthetic: bool = True`.
  5. Added `EmbeddingMetadata` model (model name, dimension, normalization, revision).
  6. Added structured `EvidencePassage` model with paragraph numbers and offsets to `RealJudgmentCaseStudyRecord`.
  7. Updated JSON Schema sample to reflect `ClauseType` and `RiskLevel`.
* **Reason for Correction:** Single authoritative schema standard ensuring zero friction between backend API models and dataset pipelines.
* **Evidence / Source:** `backend/app/models/schemas.py` lines 14-43, 95-103; Python 3 Unicode string model.
* **Affected Documents:** `04_CANONICAL_DATA_SCHEMAS.md`, `05_LABEL_TAXONOMY.md`, `11_HUGGINGFACE_PIPELINE.md`.
* **Remaining Concerns:** None.
* **Review Status:** Resolved.

### 2.6 `05_LABEL_TAXONOMY.md`
* **Original Issue:** Conflated Sections 10 and 11 regarding competency and minority voidness; grouped Section 73 and 74 without delineating unliquidated vs. liquidated damages; lacked explicit perspective lens framework.
* **Correction Made:**
  1. Harmonized class names to `ClauseType` (21 classes) and `RiskLevel` (4 levels).
  2. Detailed Section 10 (contract prerequisites) vs. Section 11 (competency definition; minor contracts void *ab initio* per *Mohori Bibee*).
  3. Rigorously separated Section 73 (unliquidated damages, direct/foreseeable loss, actual proof required) from Section 74 (liquidated damages / penalties, reasonable compensation capped at stipulated sum, judicial review of penalties).
  4. Documented the 3 perspective lenses: Party A, Party B, and Neutral Auditor.
  5. Standardized exactly 11 Legal NER classes and 7 Rhetorical Role classes.
* **Reason for Correction:** Doctrinal Indian legal precision and elimination of classification ambiguity.
* **Evidence / Source:** Indian Contract Act, 1872; *Mohori Bibee v. Dharmodas Ghose (1903)*; *Fateh Chand v. Balkishan Dass (1964)*; *Kailash Nath Associates v. DDA (2015)*.
* **Affected Documents:** `05_LABEL_TAXONOMY.md`, `06_ANNOTATION_GUIDELINES.md`, `08_CASE_STUDY_DATA_SPECIFICATION.md`.
* **Remaining Concerns:** None.
* **Review Status:** Resolved.

### 2.7 `06_ANNOTATION_GUIDELINES.md`
* **Original Issue:** Lacked mandatory perspective lens assignment in risk annotation procedures; did not detail Section 73 vs. 74 differentiation in scoring rules.
* **Correction Made:**
  1. Added mandatory perspective lens assignment (`party_a`, `party_b`, `neutral`) for every risk annotation.
  2. Standardized terms to `ClauseType` and `RiskLevel`.
  3. Integrated Section 73 vs. 74 damages distinction into annotator scoring guidance.
  4. Re-verified 11 NER entity boundary guidelines and 7 rhetorical role guidelines.
* **Reason for Correction:** Ensure high inter-annotator agreement ($\kappa \ge 0.82$) through unambiguous guidelines.
* **Evidence / Source:** Standard legal annotation best practices (SemEval-2023 Task 6; CUAD).
* **Affected Documents:** `06_ANNOTATION_GUIDELINES.md`, `05_LABEL_TAXONOMY.md`.
* **Remaining Concerns:** None.
* **Review Status:** Resolved.

### 2.8 `07_BILINGUAL_DATA_STRATEGY.md`
* **Original Issue:** Described multilingual embeddings as existing; did not address script incompatibility in translation leakage checks; did not cite Official Languages Act Section 5.
* **Correction Made:**
  1. Clarified that 384-dim English embedding is existing, while multilingual `bge-m3` (1024-dim) is a Phase 2/3 target.
  2. Grounded Hindi parallel texts in Section 5(1) of the *Official Languages Act, 1963*.
  3. Explicitly noted that English-Hindi character n-grams cannot detect leakage; mandated structural section ID binding and cross-lingual semantic cosine audits.
  4. Preserved and validated the canonical 20-term legal Hindi glossary and Unicode NFC normalization rules.
* **Reason for Correction:** Linguistic accuracy and leakage prevention.
* **Evidence / Source:** The Official Languages Act, 1963; Unicode Standard Form C.
* **Affected Documents:** `07_BILINGUAL_DATA_STRATEGY.md`, `10_DATASET_SPLITTING_AND_LEAKAGE.md`.
* **Remaining Concerns:** None.
* **Review Status:** Resolved.

### 2.9 `08_CASE_STUDY_DATA_SPECIFICATION.md`
* **Original Issue:** Lacked distinction between ground truth and synthetic reasoning in moot scenarios; lacked structural evidence passages.
* **Correction Made:**
  1. Aligned FIRAC schema with `RealJudgmentCaseStudyRecord` in `04_CANONICAL_DATA_SCHEMAS.md`.
  2. Added structured evidence passage definitions.
  3. Detailed Section 73 vs. 74 doctrinal synthesis across *Fateh Chand*, *Maula Bux*, and *Kailash Nath Associates*.
  4. Enforced strict isolation and `is_synthetic: true` labeling for hypothetical case studies.
* **Reason for Correction:** Methodological rigor in FIRAC and doctrinal evolution modeling.
* **Evidence / Source:** Supreme Court of India precedents (*Satyabrata Ghose*, *Fateh Chand*, *Kailash Nath Associates*).
* **Affected Documents:** `08_CASE_STUDY_DATA_SPECIFICATION.md`, `04_CANONICAL_DATA_SCHEMAS.md`.
* **Remaining Concerns:** None.
* **Review Status:** Resolved.

### 2.10 `09_DATA_PREPROCESSING_PIPELINE.md`
* **Original Issue:** Marginal line number regex was overly broad and risked stripping legitimate numbered legal clauses (`1. Definitions`); blind de-hyphenation risked corrupting hyphenated legal compound words.
* **Correction Made:**
  1. Replaced aggressive marginal line number regex with `strip_marginal_line_numbers_safe()`, explicitly checking for clause numbering prefixes before stripping margin numbers.
  2. Implemented `safe_dehyphenate()` protected by `PROTECTED_LEGAL_HYPHENATED_TERMS` lookup table to preserve compound terms like *non-compete*, *cross-examination*, and *in-camera*.
  3. Standardized character offsets to 0-based Unicode code points on normalized text.
* **Reason for Correction:** Prevent source corruption during automated text cleaning.
* **Evidence / Source:** Empirical inspection of Indian court pleadings and contract drafting styles.
* **Affected Documents:** `09_DATA_PREPROCESSING_PIPELINE.md`, `04_CANONICAL_DATA_SCHEMAS.md`.
* **Remaining Concerns:** OCR confidence thresholds must be empirically validated against pilot batches in Phase 2.
* **Review Status:** Resolved.

### 2.11 `10_DATASET_SPLITTING_AND_LEAKAGE.md`
* **Original Issue:** Proposed using character n-gram containment between English and Hindi to detect translation leakage (which always equals 0% due to Latin vs. Devanagari script differences); did not document MinHash LSH detection quality or false positive/negative rates.
* **Correction Made:**
  1. Addressed the Latin vs. Devanagari script incompatibility warning.
  2. Replaced character n-gram containment with **Structural Section ID Binding**, **Cross-Lingual Semantic Cosine Auditing** ($\text{CosineSim} \ge 0.88$), and **Bilingual Terminology Projection**.
  3. Documented MinHash LSH candidate filtering ($b=32, r=4, t \approx 0.42$) paired with exact Jaccard calculation ($J \ge 0.85$) ensuring $0\%$ false positive cluster mergers and $\le 0.5\%$ false negative rate.
* **Reason for Correction:** Elimination of fatal flaw in translation leakage auditing.
* **Evidence / Source:** Cross-lingual NLP literature (Conneau et al., 2020); LSH theory (Leskovec et al., Mining of Massive Datasets).
* **Affected Documents:** `10_DATASET_SPLITTING_AND_LEAKAGE.md`, `07_BILINGUAL_DATA_STRATEGY.md`.
* **Remaining Concerns:** None.
* **Review Status:** Resolved.

### 2.12 `11_HUGGINGFACE_PIPELINE.md`
* **Original Issue:** Imposed a uniform license (`license: cc-by-4.0`) in the dataset card while Python code declared `_LICENSE = "Mixed"`; ClassLabels in script did not strictly match canonical `ClauseType` enum.
* **Correction Made:**
  1. Eliminated blanket uniform licensing; declared `license: other` on the Hub card and specified independent per-configuration licenses (`specific_license="CC-BY-4.0"` for clauses, `"Government Open Data / Public Domain"` for statutes).
  2. Standardized `ClassLabel` names to canonical 21 `ClauseType` values.
  3. Aligned Arrow schema with canonical `ContractClauseRecord` fields.
* **Reason for Correction:** Legal licensing integrity on public/gated repository hubs.
* **Evidence / Source:** Hugging Face Hub metadata specification and dataset card guidelines.
* **Affected Documents:** `11_HUGGINGFACE_PIPELINE.md`, `02_SOURCE_REGISTRY.md`, `04_CANONICAL_DATA_SCHEMAS.md`.
* **Remaining Concerns:** None.
* **Review Status:** Resolved.

### 2.13 `12_DATA_QUALITY_AND_VALIDATION.md`
* **Original Issue:** Hardcoded statutory section maximums were presented as absolute proof of legal validity without considering statutory amendments or alphanumeric sections; null checks were not dataset-specific.
* **Correction Made:**
  1. Added explicit caution that statutory ranges are heuristic screening aids, noting alphanumeric amendments (e.g., Section 20A in Specific Relief Act, Section 43A in IT Act).
  2. Defined dataset-specific completeness assertions identifying permissible null fields (`clause_title`, `suggested_revision_text`).
  3. Preserved Great Expectations assertions and Devanagari Script Purity Index ($\text{SPI} \ge 85\%$).
* **Reason for Correction:** Methodological accuracy in statutory validation.
* **Evidence / Source:** Indian legislative drafting practices.
* **Affected Documents:** `12_DATA_QUALITY_AND_VALIDATION.md`, `05_LABEL_TAXONOMY.md`.
* **Remaining Concerns:** None.
* **Review Status:** Resolved.

### 2.14 `13_DATA_PRIVACY_AND_GOVERNANCE.md`
* **Original Issue:** Email regex had a character-class syntax error (`[A-Z|a-z]`); bank account regex matched all 9-18 digit numbers causing massive false positives; salted hashing was incorrectly claimed to produce anonymized data; corporate names were granted broad blanket exemption; `AuditLog` schema diverged from `db_models.py`.
* **Correction Made:**
  1. Corrected email regex to `r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"`.
  2. Implemented context-aware bank account regex requiring banking keywords within a sliding window.
  3. Clarified that salted hashing is **pseudonymization**, not irreversible anonymization.
  4. Restated corporate name exemption to exclude sole proprietorships and partnerships incorporating personal names in consumer/debt disputes.
  5. Aligned audit logging documentation with the actual `AuditLog` table columns (`id`, `user_id`, `action`, `details`, `ip_address`, `created_at`).
  6. Corrected BNS references to Sections 72 and 73; noted DPDP Act phased commencement under Section 1(2).
* **Reason for Correction:** Rigorous privacy compliance under Indian law and regex engineering correctness.
* **Evidence / Source:** `backend/app/models/db_models.py` lines 86-94; DPDP Act, 2023; BNS, 2023.
* **Affected Documents:** `13_DATA_PRIVACY_AND_GOVERNANCE.md`, `03_LICENSE_AND_PROVENANCE_POLICY.md`.
* **Remaining Concerns:** None.
* **Review Status:** Resolved.

### 2.15 `14_DATASET_IMPLEMENTATION_ROADMAP.md`
* **Original Issue:** Claimed Phase 1 was fully approved without pause; did not incorporate Phase 1.1 milestones; risk matrix did not reflect resolved ACORD licensing or cross-lingual leakage mitigations.
* **Correction Made:**
  1. Updated roadmap Gantt chart and milestone registers to incorporate Phase 1.1 audit, verification, and sign-off gates.
  2. Updated risk matrix to reflect exclusion of proprietary ACORD standards and adoption of structural bilingual binding.
  3. Maintained strict human approval gate pausing before Phase 2 execution.
* **Reason for Correction:** Transparent project management and milestone governance.
* **Evidence / Source:** Phase 1.1 Specification.
* **Affected Documents:** `14_DATASET_IMPLEMENTATION_ROADMAP.md`, `INDEX.md`.
* **Remaining Concerns:** None.
* **Review Status:** Resolved.

