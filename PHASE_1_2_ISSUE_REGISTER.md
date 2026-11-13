# Phase 1.2 Issue Register

**Document ID:** `LEGALAI-DOC-DE-ISSUE-REGISTER-1.2`  
**Version:** `1.0.0`  
**Status:** Canonical Issue Tracking  
**Date:** 2026-11-13  
**Target Platform:** LegalAI (Indian Legal Intelligence Platform)

---

## 1. Issue Dashboard

| Category | Total Issues | PASS | CONDITIONAL | FAIL | NOT VERIFIED |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Legal Accuracy (LEG)** | 4 | 4 | 0 | 0 | 0 |
| **Source & Licensing (SRC)** | 5 | 2 | 1 | 0 | 2 |
| **Schema & Pipeline (SCH)** | 5 | 5 | 0 | 0 | 0 |
| **Risk Taxonomy (TAX)** | 3 | 3 | 0 | 0 | 0 |
| **ML & Leakage (ML)** | 4 | 4 | 0 | 0 | 0 |
| **Privacy & Governance (PRI)** | 4 | 4 | 0 | 0 | 0 |
| **Validation & Sign-Off (VAL)**| 4 | 3 | 1 | 0 | 0 |
| **TOTAL** | **29** | **25** | **2** | **0** | **2** |

---

## 2. Complete Issue Ledger

### Group A: Legal Accuracy

#### LEG-01: Official Languages Act, 1963, Section 5 Overstatement
* **Severity:** High
* **Affected Documents:** `01_DATASET_ARCHITECTURE.md`, `07_BILINGUAL_DATA_STRATEGY.md`
* **Problem:** Text overstated Section 5 as creating an automatic, universal obligation to publish authorized Hindi translations of all Central Acts and ordinances.
* **Correction:** Clarified that Section 5 establishes legal evidentiary authority for gazetted Hindi translations published under Presidential authority. Clarified Article 348(1)(b) English primacy. Removed claims of universal Hindi coverage.
* **Evidence:** The Official Languages Act, 1963, Section 5; Constitution of India, Article 348 (`EVID-LEG-01`).
* **Status:** **PASS**
* **Remaining Dependencies:** None.

#### LEG-02: DPDP Act 2023 Section 16 & Localization Overstatement
* **Severity:** Critical
* **Affected Documents:** `13_DATA_PRIVACY_AND_GOVERNANCE.md`, `01_DATASET_ARCHITECTURE.md`
* **Problem:** Claimed universal India-only data localization as a DPDP statutory mandate under Section 16.
* **Correction:** Corrected Section 16 as empowering a government negative list/blacklist for restricted countries. Reclassified LegalAI's India-only hosting as an internal architecture and risk-management decision. Recorded the Gazette notification of 13 November 2025 scheduling Sections 3–17 for phased commencement 18 months post-publication.
* **Evidence:** Digital Personal Data Protection Act, 2023, Section 1(2) & 16; Gazette Notification S.O. 13 Nov 2025 (`EVID-LEG-02`).
* **Status:** **PASS**
* **Remaining Dependencies:** None.

#### LEG-03: Family Courts Act, 1984, Section 11 Overstatement
* **Severity:** High
* **Affected Documents:** `03_LICENSE_AND_PROVENANCE_POLICY.md`, `13_DATA_PRIVACY_AND_GOVERNANCE.md`
* **Problem:** Treated all family court records as automatically secret and subject to statutory anonymization under Section 11.
* **Correction:** Clarified that Section 11 governs in-camera proceedings conducted at the court's discretion or party request. Substituted blanket claims with a case-by-case screening protocol for family court records.
* **Evidence:** Family Courts Act, 1984, Section 11 (`EVID-LEG-03`).
* **Status:** **PASS**
* **Remaining Dependencies:** Implementation of case-by-case filter script in Phase 2.

#### LEG-04: Copyright Act, 1957, Section 52(1)(q) Multi-Tiered Analysis
* **Severity:** Critical
* **Affected Documents:** `03_LICENSE_AND_PROVENANCE_POLICY.md`
* **Problem:** Applied Section 52(1)(q) too broadly without distinguishing pure text from private translations, editorial commentary, and commercial databases.
* **Correction:** Established a 7-tier legal material classification (bare statutes, gazettes, raw judgments, editorial annotations, headnotes, commercial databases, private translations). Clarified that private translations and commercial databases enjoy independent copyright or contractual protection.
* **Evidence:** Copyright Act, 1957, Section 52(1)(q); *Eastern Book Company v. D.B. Modak (2008) 1 SCC 1* (`EVID-LEG-04`).
* **Status:** **PASS**
* **Remaining Dependencies:** None.

---

### Group B: Dataset Source & Licensing Verification

#### SRC-01: Atticus A-CoRD Hub Status & Verification
* **Severity:** High
* **Affected Documents:** `02_SOURCE_REGISTRY.md`
* **Problem:** Asserted verified license and size for a standalone A-CoRD Hugging Face release that was not independently located.
* **Correction:** Reclassified Atticus A-CoRD as **NOT VERIFIED**. Retained confirmed Atticus datasets CUAD and MAUD as primary contract training corpora.
* **Evidence:** Hugging Face Hub audit (`TheAtticusProject/cuad` and `TheAtticusProject/maud` verified; standalone `acord` not verified) (`EVID-SRC-01`).
* **Status:** **NOT VERIFIED** (Marked NOT VERIFIED with missing evidence explained).
* **Remaining Dependencies:** Confirmation of repository identifier from The Atticus Project.

#### SRC-02: LegalTransEn Identity & Release
* **Severity:** High
* **Affected Documents:** `02_SOURCE_REGISTRY.md`, `07_BILINGUAL_DATA_STRATEGY.md`
* **Problem:** Marked as verified without verifiable public repository, publisher, or release commit.
* **Correction:** Reclassified as **NOT VERIFIED**. Clarified that bilingual parallel corpora will be sourced directly from official Government parallel gazettes and verified IndicTrans2 benchmarks.
* **Evidence:** Repository audit (`EVID-SRC-02`).
* **Status:** **NOT VERIFIED**
* **Remaining Dependencies:** Locating standalone Hugging Face dataset card or relying on primary gazettes.

#### SRC-03: Dataset Metadata Standardization
* **Severity:** Medium
* **Affected Documents:** `02_SOURCE_REGISTRY.md`
* **Problem:** Inconsistent metadata fields and lack of explicit verification dimensions.
* **Correction:** Updated all source registry entries to include the mandatory 14-field schema (Source ID, Publisher, Dataset Name, Repository ID, Release/Version, Access URL, License, License Evidence, Dataset Size, Commercial Use, Redistribution, Training Use, Verification Date, Verification Status).
* **Evidence:** `02_SOURCE_REGISTRY.md` Section 2–5.
* **Status:** **PASS**
* **Remaining Dependencies:** None.

#### SRC-04: Multi-Dimensional Verification Status
* **Severity:** Medium
* **Affected Documents:** `02_SOURCE_REGISTRY.md`
* **Problem:** Single monolithic VERIFIED status hid dimensional uncertainties.
* **Correction:** Expanded verification reporting across 8 distinct dimensions: Publisher, Identity, Release, License, Endpoint, Commercial Rights, Redistribution Rights, Training Rights.
* **Evidence:** `02_SOURCE_REGISTRY.md` Section 6 matrix.
* **Status:** **PASS**
* **Remaining Dependencies:** None.

#### SRC-05: Public Availability vs. Legal Permissions Distinction
* **Severity:** High
* **Affected Documents:** `03_LICENSE_AND_PROVENANCE_POLICY.md`
* **Problem:** Conflated public web accessibility with permission to collect, store, process, train on, or redistribute data.
* **Correction:** Formalized explicit 7-tier permission ladder in Section 3 of `03_LICENSE_AND_PROVENANCE_POLICY.md`.
* **Evidence:** Legal IP doctrine; Terms of Service principles (`EVID-LEG-04`).
* **Status:** **PASS**
* **Remaining Dependencies:** None.

---

### Group C: Canonical Schema & Pipeline

#### SCH-01: Canonical Schema to Hugging Face Features Alignment
* **Severity:** High
* **Affected Documents:** `04_CANONICAL_DATA_SCHEMAS.md`, `11_HUGGINGFACE_PIPELINE.md`
* **Problem:** HF `datasets.Features` definitions omitted core canonical fields (`dataset_version`, `jurisdiction`, `annotation_status`, `provenance`, `secondary_categories`, `embedding_metadata`).
* **Correction:** Completely updated `11_HUGGINGFACE_PIPELINE.md` features definitions to map 1:1 to canonical Pydantic v2 schemas; documented field-by-field mapping table.
* **Evidence:** Comparison between `04_CANONICAL_DATA_SCHEMAS.md` and `11_HUGGINGFACE_PIPELINE.md`.
* **Status:** **PASS**
* **Remaining Dependencies:** None.

#### SCH-02: Canonical Dataset Path Consistency
* **Severity:** Medium
* **Affected Documents:** `01`, `04`, `09`, `11`, `14`
* **Problem:** Minor path variations between data lake tiers.
* **Correction:** Standardized canonical filesystem topology: `data/{bronze,silver,gold}/` with consistent sub-partitions documented identically across all 5 files.
* **Evidence:** Cross-document path audit.
* **Status:** **PASS**
* **Remaining Dependencies:** None.

#### SCH-03: Mixed License Handling in Dataset Packaging
* **Severity:** High
* **Affected Documents:** `11_HUGGINGFACE_PIPELINE.md`
* **Problem:** Packaging multiple sources under a single Hub repo without record-level and config-level license isolation.
* **Correction:** Implemented record-level `source_license` field, independent configuration-level licenses (`CC-BY-4.0` for clauses, `OGD India` for statutes), and declared `license: other` in the Hub card frontmatter.
* **Evidence:** `11_HUGGINGFACE_PIPELINE.md` Section 3 & 4.
* **Status:** **PASS**
* **Remaining Dependencies:** None.

#### SCH-04: Pydantic v2 and JSON Schema Compatibility
* **Severity:** Medium
* **Affected Documents:** `04_CANONICAL_DATA_SCHEMAS.md`
* **Problem:** Cited Pydantic v2.10+ alongside JSON Schema Draft-07 without explaining dialect generation discrepancies.
* **Correction:** Formally declared **JSON Schema Draft 2020-12** as the native canonical dialect generated by Pydantic v2. Documented Draft-07 transformation procedures for legacy tooling.
* **Evidence:** Pydantic v2 documentation on `.model_json_schema()` (`EVID-SCH-01`).
* **Status:** **PASS**
* **Remaining Dependencies:** None.

#### SCH-05: Serialization and Round-Trip Validation Test Specification
* **Severity:** Medium
* **Affected Documents:** `04_CANONICAL_DATA_SCHEMAS.md`
* **Problem:** Asserted serialization readiness without a concrete test specification.
* **Correction:** Documented complete test specification covering canonical record instantiation, Pydantic validation, JSON serialization, PyArrow conversion, and optional field preservation.
* **Evidence:** `04_CANONICAL_DATA_SCHEMAS.md` Section 5.
* **Status:** **PASS**
* **Remaining Dependencies:** Execution of unit test suite in Phase 2.

---

### Group D: Risk Taxonomy & Annotation Quality

#### TAX-01: Context-Dependent Legal Risk Analysis
* **Severity:** High
* **Affected Documents:** `05_LABEL_TAXONOMY.md`
* **Problem:** Assigned universal "critical" or "void ab initio" classifications without context (e.g., non-competes during employment vs. post-termination; domestic vs. cross-border governing law).
* **Correction:** Contextualized Section 27 non-competes (during employment valid per *Niranjan Shankar Golikari*; post-termination void per *Percept D'Mark*). Contextualized foreign governing law (valid in cross-border agreements; restricted between purely domestic entities).
* **Evidence:** *Niranjan Shankar Golikari v. Century Spg. & Mfg. Co. (AIR 1967 SC 1098)*; *TDM Infrastructure (P) Ltd. v. UE Development India (P) Ltd. (2008) 14 SCC 271*.
* **Status:** **PASS**
* **Remaining Dependencies:** None.

#### TAX-02: Reproducible Heuristic Risk-Scoring Formula
* **Severity:** Medium
* **Affected Documents:** `05_LABEL_TAXONOMY.md`
* **Problem:** Numerical risk scores lacked a mathematical formulation.
* **Correction:** Codified explicit mathematical formula:
  $$\text{RiskScore} = \min\left(100, \, \Big[\text{BaseWeight}(S) \times \text{PerspectiveFactor}(P) + \text{StatutoryPenalty} - \text{MitigationDiscount}\Big] \times \text{Confidence}\right)$$
  Explicitly designated as a configurable heuristic model, not an actuarially validated score.
* **Evidence:** `05_LABEL_TAXONOMY.md` Section 4.2.
* **Status:** **PASS**
* **Remaining Dependencies:** None.

#### TAX-03: Annotation Consistency & Disagreement Procedures
* **Severity:** Medium
* **Affected Documents:** `05_LABEL_TAXONOMY.md`, `06_ANNOTATION_GUIDELINES.md`
* **Problem:** Lacked inclusion/exclusion criteria, positive/negative/ambiguous examples, and formal escalation workflows for ambiguous clauses.
* **Correction:** Added complete criteria tables with positive, negative, and ambiguous examples for high-risk clauses; formalized Tier 2 Adjudicator escalation workflow.
* **Evidence:** `06_ANNOTATION_GUIDELINES.md` Section 4 & 5.
* **Status:** **PASS**
* **Remaining Dependencies:** None.

---

### Group E: Preprocessing, Leakage & Evaluation

#### ML-01: MinHash Leakage Detection False-Positive Claims
* **Severity:** High
* **Affected Documents:** `10_DATASET_SPLITTING_AND_LEAKAGE.md`
* **Problem:** Claimed 0% false-positive cluster merges without empirical evaluation.
* **Correction:** Removed the unsupported claim. Defined false-positive cluster merges, sample size requirements ($N=1,000$ pairs), and evaluation metric formulas (Precision, Recall, F1). Marked metric as **NOT RUN**.
* **Evidence:** `10_DATASET_SPLITTING_AND_LEAKAGE.md` Section 3.2 (`EVID-ML-01`).
* **Status:** **PASS**
* **Remaining Dependencies:** Execution on pilot dataset in Sprint 2.3.

#### ML-02: Cross-Lingual Similarity Threshold (0.88)
* **Severity:** Medium
* **Affected Documents:** `10_DATASET_SPLITTING_AND_LEAKAGE.md`
* **Problem:** 0.88 threshold was stated without empirical calibration evidence.
* **Correction:** Reclassified 0.88 as a provisional proposal. Documented empirical calibration procedure sweeping thresholds from 0.80 to 0.92 using multilingual embeddings. Marked status as **NOT RUN**.
* **Evidence:** `10_DATASET_SPLITTING_AND_LEAKAGE.md` Section 4.2 (`EVID-ML-02`).
* **Status:** **PASS**
* **Remaining Dependencies:** Empirical threshold sweep in Phase 2.

#### ML-03: Leakage-Safe Splitting Hierarchy
* **Severity:** High
* **Affected Documents:** `10_DATASET_SPLITTING_AND_LEAKAGE.md`
* **Problem:** Needed explicit split assignment order covering templates, translations, and case documents.
* **Correction:** Defined 5-tier hierarchical grouping and deterministic assignment sequence in Section 2.
* **Evidence:** `10_DATASET_SPLITTING_AND_LEAKAGE.md` Section 2.
* **Status:** **PASS**
* **Remaining Dependencies:** None.

#### ML-04: Pipeline Reproducibility Specifications
* **Severity:** Medium
* **Affected Documents:** `10_DATASET_SPLITTING_AND_LEAKAGE.md`, `14_DATASET_IMPLEMENTATION_ROADMAP.md`
* **Problem:** Missing explicit configuration parameters (seed, version, manifest).
* **Correction:** Codified standard reproducibility block (Seed `42`, deterministic manifests, Git commit tagging). Marked unexecuted stages as **NOT RUN**.
* **Evidence:** `10_DATASET_SPLITTING_AND_LEAKAGE.md` Section 6.
* **Status:** **PASS**
* **Remaining Dependencies:** None.

---

### Group F: Privacy & Codebase Verification

#### PRI-01: Disentangling Privacy Policy from Statutory Requirements
* **Severity:** Critical
* **Affected Documents:** `13_DATA_PRIVACY_AND_GOVERNANCE.md`
* **Problem:** Voluntary product controls were presented as statutory mandates.
* **Correction:** Structured into 6 distinct categories: Statutory Obligations, Contractual Obligations, Court-Specific Restrictions, Source Terms, Internal Privacy Policy, Recommended Security Controls.
* **Evidence:** `13_DATA_PRIVACY_AND_GOVERNANCE.md` Section 2 (`EVID-LEG-02`).
* **Status:** **PASS**
* **Remaining Dependencies:** None.

#### PRI-02: Family-Court Ingestion Eligibility Protocol
* **Severity:** High
* **Affected Documents:** `13_DATA_PRIVACY_AND_GOVERNANCE.md`
* **Problem:** Lacked source-specific pre-ingestion screening for matrimonial records.
* **Correction:** Formalized 7-step Family Court Eligibility and Exclusion Protocol evaluating in-camera status, children's interests, and re-identification risks.
* **Evidence:** `13_DATA_PRIVACY_AND_GOVERNANCE.md` Section 3 (`EVID-LEG-03`).
* **Status:** **PASS**
* **Remaining Dependencies:** None.

#### PRI-03: Data Lifecycle & Provenance Transformation
* **Severity:** Medium
* **Affected Documents:** `13_DATA_PRIVACY_AND_GOVERNANCE.md`
* **Problem:** Incomplete description of provenance preservation during chunking and transformations.
* **Correction:** Documented 12-stage data lifecycle from ingestion approval to cascading deletion, tracking parent-child SHA-256 hashes.
* **Evidence:** `13_DATA_PRIVACY_AND_GOVERNANCE.md` Section 5.
* **Status:** **PASS**
* **Remaining Dependencies:** None.

#### PRI-04: Actual Codebase Verification & Alignment
* **Severity:** Critical
* **Affected Documents:** `INDEX.md`, `01_DATASET_ARCHITECTURE.md`, `13_DATA_PRIVACY_AND_GOVERNANCE.md`
* **Problem:** Claimed existence of components without repository audit.
* **Correction:** Conducted file-by-file audit of `backend/app/`. Verified `vector_db.py` (Existing, 384-dim), `audit.py` (Existing), `AuditLog` (Existing, verified columns), `nlu.py` agent chain (Partial), RAG (Partial). Corrected all documentation claims.
* **Evidence:** `backend/app/` file inspections (`EVID-COD-01`).
* **Status:** **PASS**
* **Remaining Dependencies:** None.

---

### Group G: Validation & Readiness

#### VAL-01: Revalidation of Previous Phase 1.1 Claims
* **Severity:** High
* **Affected Documents:** `PHASE_1_1_VALIDATION_REPORT.md` (superseded by `PHASE_1_2_VALIDATION_REPORT.md`)
* **Problem:** Overly optimistic PASS claims on legal and dataset items.
* **Correction:** Reaudited all 32 previous claims with strict evidence requirements.
* **Evidence:** `PHASE_1_2_VALIDATION_REPORT.md` Section 3.
* **Status:** **PASS**
* **Remaining Dependencies:** None.

#### VAL-02: Adoption of 4 Evidence-Based Statuses
* **Severity:** High
* **Affected Documents:** `PHASE_1_2_VALIDATION_REPORT.md`, `PHASE_1_2_SIGNOFF.md`
* **Problem:** Binary Pass/Fail hid missing evidence.
* **Correction:** Standardized strictly on: **PASS**, **CONDITIONAL**, **FAIL**, **NOT VERIFIED**.
* **Evidence:** Validation Report and Sign-off documents.
* **Status:** **PASS**
* **Remaining Dependencies:** None.

#### VAL-03: Reassessment of Acceptance Criteria AC-01 to AC-15
* **Severity:** High
* **Affected Documents:** `PHASE_1_2_SIGNOFF.md`
* **Problem:** Previous checklist marked all items SATISFIED without individual evidentiary qualification.
* **Correction:** Individually evaluated AC-01 through AC-15 with concrete evidence citations and outstanding dependencies.
* **Evidence:** `PHASE_1_2_SIGNOFF.md` Section 1.
* **Status:** **PASS**
* **Remaining Dependencies:** None.

#### VAL-04: Phase Readiness Decision
* **Severity:** Critical
* **Affected Documents:** All documentation files
* **Problem:** Risk of prematurely declaring Phase 2 ready before independent review.
* **Correction:** Established official determination: **CONDITIONALLY READY FOR INDEPENDENT REVIEW**. Explicitly barred proceeding to Phase 2 implementation without human stakeholder approval.
* **Evidence:** `PHASE_1_2_SIGNOFF.md` Section 3.
* **Status:** **PASS**
* **Remaining Dependencies:** Human approval.

