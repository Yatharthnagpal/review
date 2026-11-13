# Phase 1.2 — Detailed Audit & Revision Changelog

**Document ID:** `LEGALAI-DOC-DE-CHANGELOG-1.2`  
**Version:** `1.2.0`  
**Status:** Complete — Audited & Verified  
**Date:** 2026-11-13  
**Framework:** LegalAI Evidence-Based Audit & Remediation Standard  
**Dependencies:** `PHASE_1_2_EVIDENCE_REGISTER.md`, `PHASE_1_2_ISSUE_REGISTER.md`, Specifications `01` through `14`, `INDEX.md`

---

## 1. Executive Summary

This changelog provides an exhaustive, auditable record of all modifications, statutory corrections, schema alignments, and governance enhancements executed during **Phase 1.2: Final Verification & Remediation**.

Every change recorded below is tied directly to an authoritative statutory enactment, primary judicial precedent, codebase inspection record, or empirical machine learning standard.

---

## 2. Document-by-Document Modification Register

### `01_DATASET_ARCHITECTURE.md` (Version 1.2.0)
- **Section 2.1 (Storage Topology):** Qualified the mandate for Indian data sovereignty; clarified that hosting inside AWS Mumbai (`ap-south-1`) is an internal organizational policy (Tier 5) rather than a direct DPDP statutory mandate (`LEG-02`, `EVID-LEG-02`).
- **Section 3.2 (Bilingual Corpus):** Corrected the description of Section 5 of the Official Languages Act, 1963; clarified that gazetted Hindi translations carry legal authority under the President's seal, but Article 348(1)(b) establishes English authoritative text primacy. Universal publication is not statutory (`LEG-01`, `EVID-LEG-01`).
- **Section 5 (Codebase Reality Mapping):** Harmonized runtime component status (Pydantic models, SQLAlchemy, Qdrant FastEmbed, AuditLog service verified as Existing; RAG and Multi-agent verified as Partial) (`EVID-COD-01`).

### `02_SOURCE_REGISTRY.md` (Version 1.2.0)
- **Sections 2–5 (16 Candidate Sources):** Standardized all source entries into the uniform 14-field metadata schema (`SRC-05`, `EVID-SRC-05`).
- **Section 2.2 (Atticus A-CoRD):** Marked standalone Hugging Face parquet release as **`NOT VERIFIED`** (`SRC-01`, `EVID-SRC-01`). Quarantined until primary repository confirmation.
- **Section 2.3 (ACORD Commercial Insurance Forms):** Strictly quarantined and excluded from all pipelines. Clarified that proprietary ACORD standards cannot be ingested under fair dealing or academic licenses (`SRC-02`, `EVID-SRC-02`).
- **Section 3.3 (LegalTransEn):** Marked standalone Hugging Face release as **`NOT VERIFIED`** (`SRC-03`, `EVID-SRC-03`). Quarantined; bilingual corpus restricted to official India Code gazettes.
- **Section 4.3 (KanoonGPT):** Marked terms of service boundaries as **`CONDITIONAL`** (`SRC-04`, `EVID-SRC-04`). Quarantined from automated crawling pending formal legal review; pipeline directed to AWS Open Data.
- **Section 6 (Multi-Dimensional Verification Matrix):** Added an 8-dimensional verification matrix tracking all candidate sources across 8 criteria.

### `03_LICENSE_AND_PROVENANCE_POLICY.md` (Version 1.2.0)
- **Section 2 (Indian Copyright Act § 52(1)(q)):** Replaced blanket public-domain claim with a 7-tier legal material classification. Applied *Eastern Book Company v. D.B. Modak* standard: bare acts and raw judgments are non-infringing; editorial headnotes, annotations, and commercial databases enjoy copyright and contractual protection (`LEG-03`, `EVID-LEG-03`).
- **Section 3 (Family Courts Act § 11):** Corrected categorical blanket exclusion. Formulated 7-Step Ingestion Eligibility Protocol allowing extraction of abstract legal propositions while redacting matrimonial/minor particulars (`LEG-04`, `EVID-LEG-04`).
- **Section 4 (Statutory Non-Disclosure):** Delineated specific statutory provisions: BNS 2023 § 72 (victim identity) vs § 73 (in-camera proceedings); POCSO Act 2012 § 24(5) (police/medical duty) vs § 33(7) (court trial duty); DPDP Act 2023 § 16 (negative-list transfer power) (`LEG-02`, `EVID-LEG-02`).

### `04_CANONICAL_DATA_SCHEMAS.md` (Version 1.2.0)
- **Section 1.1 (JSON Schema Standards):** Declared Pydantic v2 native output as JSON Schema Draft 2020-12; documented backward compatibility guidance for Draft-07 tooling (`SCH-01`, `EVID-SCH-01`).
- **Section 2.1 (`ContractClauseRecord`):** Ensured full nested field completeness (`example_id`, `document_id`, `dataset_version`, `language`, `jurisdiction`, `annotation_status`, `provenance`, `clause_index`, `clause_title`, `clause_text`, `clause_category`, `secondary_categories`, `char_start`, `char_end`, `is_boilerplate`, `perspective`, `embedding`) (`SCH-02`, `EVID-SCH-01`).
- **Section 2.3 (`RealJudgmentCaseStudyRecord`):** Harmonized FIRAC sub-model with structured fields for facts, issues, reasoning, ratio, obiter, and holding (`SCH-03`, `EVID-SCH-01`).
- **Section 2.4 (`BilingualStatuteRecord`):** Standardized dual-language fields, alignment confidence, and gazette notification references (`SCH-04`, `EVID-SCH-01`).
- **Section 2.5 (`LegalNERRecord`):** Standardized 11-class entity taxonomy (`COURT`, `JUDGE`, `PETITIONER`, `RESPONDENT`, `STATUTE`, `PROVISION`, `PRECEDENT`, `DATE`, `MONETARY_VALUE`, `ORGANIZATION`, `LOCATION`) with 0-based code point offsets (`SCH-05`, `EVID-SCH-01`).
- **Section 5 (Round-Trip Test Suite):** Added automated serialization and schema validation test specifications (`VAL-03`).

### `05_LABEL_TAXONOMY.md` (Version 1.2.0)
- **Section 2.3 (Non-Compete Contextualization):** Contextualized legal risks under Section 27 of the Indian Contract Act, 1872: distinguished covenants during employment (presumptively valid) from post-termination non-competes (void under § 27) (`TAX-01`, `EVID-LEG-03`).
- **Section 2.4 (Governing Law Contextualization):** Contextualized foreign governing law and foreign arbitration clauses under Section 28: domestic contracts between Indian parties cannot exclude Indian law (*TDM Infrastructure*); cross-border contracts allow party autonomy (*Bharat Aluminium*) (`TAX-02`, `EVID-LEG-03`).
- **Section 3.2 (Heuristic Risk Formula):** Codified exact mathematical formulation of heuristic risk score calculation ($S_{\text{clause}} = \min(100, \dots)$) with perspective multipliers (`TAX-03`, `EVID-SCH-01`).

### `06_ANNOTATION_GUIDELINES.md` (Version 1.2.0)
- **Section 3.2 (Inclusion/Exclusion Tables):** Added clear boundary criteria and positive, negative, and borderline examples for high-risk clauses (Indemnity, Limitation of Liability, Non-Compete, Governing Law) (`AC-06`).
- **Section 4.3 (Adjudication Workflow):** Formalized Tier 1 dual-annotation protocol, Kappa threshold evaluation ($\kappa < 0.70$ triggers review), and Tier 2 Legal Adjudicator escalation workflow (`AC-06`).

### `07_BILINGUAL_DATA_STRATEGY.md` (Version 1.2.0)
- **Section 2.1 (Official Languages Act § 5):** Replaced universal mandate claim with accurate statutory interpretation; affirmed Article 348(1)(b) English text primacy; acknowledged selective gazette coverage (`LEG-01`, `EVID-LEG-01`).
- **Section 4 (Legal Terminology Glossary):** Verified English-Hindi legal terminology mappings against Legislative Department glossary (`AC-07`).

### `08_CASE_STUDY_DATA_SPECIFICATION.md` (Version 1.2.0)
- **Section 2.1 (FIRAC Decomposition):** Codified structured schema decomposing judgments into facts, procedural history, issues, ratio decidendi, and obiter dicta (`SCH-03`, `AC-08`).
- **Section 3.1 (Section 74 Doctrinal Evolution):** Corrected liquidated damages summary to reflect *Fateh Chand*, *Maula Bux*, and *Kailash Nath Associates* (*proof of actual damage required unless impossible*) (`EVID-LEG-03`, `AC-08`).
- **Section 4 (Synthetic Dispute Isolation):** Enforced mandatory `is_synthetic: true` tagging and benchmark isolation for mock contracts and educational case studies (`AC-08`).

### `09_DATA_PREPROCESSING_PIPELINE.md` (Version 1.2.0)
- **Section 2 (Canonical Lakehouse Paths):** Enforced canonical storage hierarchy (`data/bronze/`, `data/silver/`, `data/gold/`) (`AC-09`).
- **Section 3.2 (Safe Line-Number Stripping):** Implemented contextual regex filter preserving numbered subsections, statutory paragraphs, and currency figures while stripping marginal line numbers (1–28) (`ML-03`, `EVID-ML-01`).
- **Section 3.3 (Protected Legal De-Hyphenation):** Defined whitelist of protected hyphenated legal terms (*pro-rata*, *inter-alia*, *in-camera*, *non-compete*, *pre-condition*) (`ML-04`, `EVID-ML-01`).

### `10_DATASET_SPLITTING_AND_LEAKAGE.md` (Version 1.2.0)
- **Section 3.2 (Empirical Duplicate Benchmark):** Removed ungrounded "0% false positive" claim for MinHash LSH ($J \ge 0.85$); formulated formal Precision/Recall/F1 evaluation protocol and set status to `NOT RUN` pending baseline benchmarking (`ML-01`, `EVID-ML-01`).
- **Section 3.4 (Cross-Lingual Cosine Threshold):** Reclassified 0.88 cosine similarity threshold as a `PROVISIONAL HYPOTHESIS (NOT RUN)` requiring empirical validation against parallel bilingual pairs (`ML-02`, `EVID-ML-02`).
- **Section 4 (5-Tier Splitting Hierarchy):** Enforced document-level group splitting, bilingual section binding, temporal splitting for case law, and frozen golden benchmarks (`AC-10`).

### `11_HUGGINGFACE_PIPELINE.md` (Version 1.2.0)
- **Section 2 & 4 (Hugging Face Feature Alignment):** Expanded `datasets.Features` definitions for `contract_clauses`, `firac_case_studies`, and `statutes_bilingual` to match canonical Pydantic schemas in full (`SCH-02`, `AC-11`).
- **Section 3 (Field Mapping Table):** Added comprehensive mapping table linking Pydantic v2 types, PyArrow types, and Hugging Face feature types (`AC-11`).
- **Section 4 (Per-Config Licensing):** Enforced independent per-configuration licensing metadata in `GeneratorBasedBuilder` (`AC-11`).
- **Section 6 (Security & Gated Management):** Formulated gated access terms preventing PII re-identification and predatory litigation scraping (`AC-11`).

### `12_DATA_QUALITY_AND_VALIDATION.md` (Version 1.2.0)
- **Section 3.1 (Dataset-Specific Completeness):** Formalized strict non-null and permissible-null rules for each canonical record type (`VAL-02`, `EVID-SCH-01`).
- **Section 4 (Heuristic Section Bounds Screening):** Explicitly documented hardcoded statutory section counts as heuristic screening triage filters rather than definitive validity tests (`VAL-01`, `EVID-LEG-01`).
- **Section 6 (CI Pipeline Automation):** Integrated automated schema validation and quarantine routing rules (`AC-12`).

### `13_DATA_PRIVACY_AND_GOVERNANCE.md` (Version 1.2.0)
- **Section 2 (Six-Tier Privacy Governance Framework):** Disentangled statutory non-disclosure, court orders, contractual duties, platform terms, internal policies, and engineering safeguards (`PRI-01`, `EVID-LEG-02`).
- **Section 3.4 (Family Courts § 11 Protocol):** Established 7-step screening and anonymization protocol for matrimonial jurisprudence (`PRI-02`, `EVID-LEG-04`).
- **Section 5 (DPDP § 16 Negative List Clarification):** Removed universal India localization claim under § 16; clarified negative list model and phased commencement; designated India hosting as Tier 5 internal policy (`LEG-02`, `EVID-LEG-02`).
- **Section 6 (12-Stage Data Lifecycle & Lineage):** Documented complete 12-stage lifecycle preserving chunk lineage, parent document IDs, and character offsets (`PRI-03`, `EVID-COD-01`).
- **Section 7 (AuditLog Database Alignment):** Aligned documentation with existing `AuditLog` model in `backend/app/models/db_models.py` and `audit.py` (`PRI-04`, `EVID-COD-01`).

### `14_DATASET_IMPLEMENTATION_ROADMAP.md` (Version 1.2.0)
- **Section 2 (Roadmap Gantt):** Updated chronological milestones to include Phase 1.2 verification and remediation (`AC-14`).
- **Section 4 (Risk Matrix):** Updated risk matrix with Phase 1.2 verified statuses: ACORD commercial forms quarantined/excluded; Atticus A-CoRD standalone HF release unverified; LegalTransEn unverified; KanoonGPT conditional; duplicate evaluation protocol defined; cross-lingual threshold provisional hypothesis (`AC-14`).
- **Section 5 (Governance Gate):** Affirmed platform determination: `CONDITIONALLY READY FOR INDEPENDENT REVIEW`. Enforced rule: Phase 2 implementation cannot proceed without formal sign-off (`AC-14`).

### `INDEX.md` (Version 1.2.0)
- **Master Document Matrix:** Updated directory structure to include all 15 core specifications and all 5 Phase 1.2 governance artifacts (`AC-15`).
- **Codebase Reality Table:** Re-verified and harmonized component status against repository source code (`EVID-COD-01`).
- **Readiness Determination:** Explicitly declared platform readiness as `CONDITIONALLY READY FOR INDEPENDENT REVIEW` (`AC-15`).

---

## 3. New Phase 1.2 Governance Artifacts Created

| Artifact File | Description | Purpose |
| :--- | :--- | :--- |
| `PHASE_1_2_EVIDENCE_REGISTER.md` | Primary evidence register capturing statutory texts, Supreme Court precedents, publisher repo data, and codebase inspection records. | Grounds every claim in verified evidence. |
| `PHASE_1_2_ISSUE_REGISTER.md` | Consolidated tracking register of all 29 issues across 7 categories with acceptance criteria, evidence IDs, and resolution status. | Provides full auditability and issue resolution tracking. |
| `PHASE_1_2_VALIDATION_REPORT.md` | Comprehensive evaluation report analyzing all 7 engineering and legal pillars, revalidating claims with PASS, CONDITIONAL, FAIL, NOT VERIFIED. | Documents technical and legal audit findings. |
| `PHASE_1_2_SIGNOFF.md` | Formal sign-off document evaluating criteria AC-01 through AC-15 and stating the final readiness determination. | Enforces human review governance gate before Phase 2. |
| `PHASE_1_2_CHANGELOG.md` | Exhaustive document-by-document change log detailing every modification made during Phase 1.2. | Ensures complete traceability of revisions. |
