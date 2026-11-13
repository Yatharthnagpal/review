# Phase 1.2.1 — Detailed Audit & Revision Changelog

**Document ID:** `LEGALAI-DOC-DE-CHANGELOG-1.2.1`  
**Version:** `1.2.1`  
**Status:** Canonical Remediation Changelog  
**Date:** 2026-11-13  
**Target Platform:** LegalAI (Indian Legal Intelligence Platform)  
**Baseline Commit:** `6a0b09b0bbec3a866591209d86f221e9a3908ed6`  
**Dependencies:** `PHASE_1_2_1_EVIDENCE_REGISTER.md`, `PHASE_1_2_1_ISSUE_REGISTER.md`, Specifications `01` through `14`, `INDEX.md`

---

## 1. Executive Summary

This changelog provides an exhaustive, auditable record of all modifications, statutory corrections, schema alignments, and governance updates executed during **Phase 1.2.1: Critical Legal & Evidence Remediation**.

Every change recorded below is tied directly to an authoritative statutory enactment, primary judicial precedent, codebase inspection record, or empirical machine learning standard. The previous Phase 1.2 changelog (`PHASE_1_2_CHANGELOG.md`) is preserved intact as historical baseline documentation.

---

## 2. Document-by-Document Remediation Register

### `03_LICENSE_AND_PROVENANCE_POLICY.md` (Version 1.2.1)
- **Section 2 & 2.1 (Copyright Act § 52(1)(q) Analysis):**  
  - *Problem:* Claimed that bare statutory text is unconditionally non-infringing under § 52(1)(q)(ii), with full reproduction, chunking, and redistribution permitted.
  - *Correction:* Analyzed clauses (i), (ii), (iii), and (iv) separately. Highlighted the express statutory condition in clause (ii): Acts of Legislature are exempt *only when accompanied by commentary or other original matter*. Clarified that standalone bare reproduction is restricted. Affirmed that LegalAI pairs statutory text with original analytical matter (FIRAC, risk taxonomy, annotations), satisfying clause (ii). Added explicit legal counsel dependency for commercial model training.
  - *Issue ID:* `LEG-121-01`
  - *Evidence Basis:* `EVID-LEG-03`
  - *Status:* **PASS (Doc Verified)**
- **Section 4.1 (POCSO Act § 24(5) vs § 27):**  
  - *Problem:* Conflated identity-protection duties of police officers with medical examination procedures.
  - *Correction:* Delineated Section 24(5) specifically as a duty on the *police officer* during statement recording; documented Section 27 as an independent procedure for medical examinations.
  - *Issue ID:* `LEG-121-03`
  - *Evidence Basis:* `EVID-LEG-06`
  - *Status:* **PASS (Doc Verified)**
- **Section 4.2 (BNS 2023 § 73 Scope):**  
  - *Problem:* Described Section 73 as a general penal ban on publishing every in-camera proceeding under Indian law.
  - *Correction:* Limited Section 73 penal scope strictly to proceedings *with respect to an offence referred to in section 72* (sexual offences). Documented the statutory Explanation excluding High Court and Supreme Court judgments.
  - *Issue ID:* `LEG-121-02`
  - *Evidence Basis:* `EVID-LEG-05`
  - *Status:* **PASS (Doc Verified)**
- **Section 4.3 (Family Courts Act § 11):**  
  - *Problem:* Language treated in-camera status as an automatic publication ban on published appellate case law.
  - *Correction:* Explained that Section 11 primarily governs procedural trial closure; distinguished trial closure from court sealing orders and published appellate precedents; classified 7-step redaction protocol as an internal Tier 5 policy.
  - *Issue ID:* `LEG-121-05`
  - *Evidence Basis:* `EVID-LEG-04`
  - *Status:* **PASS (Doc Verified)**

---

### `13_DATA_PRIVACY_AND_GOVERNANCE.md` (Version 1.2.1)
- **Section 3.1 (POCSO Attribution):**  
  - *Problem:* Merged medical officers into the Section 24(5) media protection duty.
  - *Correction:* Corrected attribution: Section 24(5) specifically directs the police officer; medical examinations are independently governed by Section 27.
  - *Issue ID:* `LEG-121-03`
  - *Evidence Basis:* `EVID-LEG-06`
  - *Status:* **PASS (Doc Verified)**
- **Section 3.2 (BNS § 73 Specific Statutory Scope):**  
  - *Problem:* Overbroad generalization of Section 73 penal bar across all in-camera proceedings.
  - *Correction:* Explicitly limited Section 73 to Section 72 sexual offences; affirmed that other in-camera proceedings (Family Courts § 11, BNSS § 366, CPC § 153B) are governed by their respective statutory rules and express judicial orders.
  - *Issue ID:* `LEG-121-02`
  - *Evidence Basis:* `EVID-LEG-05`
  - *Status:* **PASS (Doc Verified)**
- **Section 3.4 (Family Courts Act § 11 Scope):**  
  - *Problem:* Conflated procedural in-camera hearings with automatic non-disclosure of legal jurisprudence.
  - *Correction:* Clarified that Section 11 governs courtroom closure; designated the 7-step screening and PII redaction protocol as LegalAI's voluntary Tier 5 policy to protect matrimonial dignity while allowing extraction of abstract FIRAC legal principles.
  - *Issue ID:* `LEG-121-05`
  - *Evidence Basis:* `EVID-LEG-04`
  - *Status:* **PASS (Doc Verified)**

---

### `05_LABEL_TAXONOMY.md` (Version 1.2.1)
- **Section 3.2 (Governing Law & Arbitration — Statutory Disentanglement):**  
  - *Problem:* Associated foreign governing law between Indian companies with Section 28 of the Indian Contract Act, 1872, citing *TDM Infrastructure*, and tagged it as an automatic `critical` void clause.
  - *Correction:* Corrected statutory reference: *TDM Infrastructure* addressed **Section 28 of the Arbitration and Conciliation Act, 1996**, not Section 28 of the Contract Act. Clarified that domestic parties cannot contract out of Indian substantive law in a domestic arbitration (violates Arbitration Act § 28(1)(a) — High Risk / Severable). Cited *PASL Wind Solutions (2021)* confirming that Indian parties can choose a foreign arbitration seat. Cited *Hakam Singh (1971)* confirming exclusive jurisdiction between competent Indian courts does not violate ICA § 28.
  - *Issue ID:* `LEG-121-04`
  - *Evidence Basis:* `EVID-LEG-07`
  - *Status:* **PASS (Doc Verified)**
- **Section 4.1 to 4.4 (Decoupled Risk Scoring Framework):**  
  - *Problem:* The formula multiplied intrinsic risk by model confidence: $\text{RiskScore} = [\dots] \times \text{Confidence}$, artificially deflating the risk score of an onerous clause when the model was uncertain.
  - *Correction:* Decoupled into four independent outputs: `legal_risk_score` (intrinsic severity $\in [0, 100]$), `model_confidence` ($\in [0.0, 1.0]$), `evidence_completeness` ($\in [0.0, 1.0]$), and `review_required` (boolean escalation). Added explicit review escalation logic: triggers if `legal_risk_score >= 70` OR if (`legal_risk_score >= 40` AND `model_confidence < 0.75`).
  - *Issue ID:* `TAX-121-01`
  - *Evidence Basis:* `EVID-SCH-01`
  - *Status:* **PASS (Doc Verified)**
- **Section 4.3 (Weight Naming):**  
  - *Problem:* Heading claimed "Calibrated Weights" without an executed calibration experiment.
  - *Correction:* Renamed to "Initial Heuristic Weights" and scheduled empirical logistic regression calibration for Phase 3.
  - *Issue ID:* `TAX-121-01`
  - *Status:* **PASS (Doc Verified)**

---

### `02_SOURCE_REGISTRY.md` (Version 1.2.1)
- **Section 2.1 & 2.2 (CUAD & MAUD Release Separation):**  
  - *Problem:* Did not clearly separate `CC BY 4.0` annotation rights from underlying contract rights.
  - *Correction:* Documented that annotations are licensed under `CC BY 4.0` by The Atticus Project, while underlying contracts are public corporate disclosure filings from SEC EDGAR. Confirmed commercial, redistribution, and training permissions.
  - *Issue ID:* `SRC-121-01`, `SRC-121-02`
  - *Evidence Basis:* `EVID-SRC-05`, `EVID-SRC-06`
  - *Status:* **PASS (Doc Verified)**
- **Section 3.5 (India Code & OGD Portal Terms):**  
  - *Problem:* Blanket public domain and commercial resale claims without statutory conditions.
  - *Correction:* Clarified that GODL India applies to portal metadata, while republication of Acts of the Legislature is conditioned on accompanying commentary or original matter under Copyright Act § 52(1)(q)(ii).
  - *Issue ID:* `SRC-121-03`
  - *Evidence Basis:* `EVID-SRC-07`
  - *Status:* **PASS (Doc Verified)**
- **Section 3.3 & 3.4 (AWS Open Data Corpora):**  
  - *Problem:* Unverified disk sizes and exact record manifests claimed.
  - *Correction:* Labeled figures (~50GB for Supreme Court, ~400GB for High Courts) and S3 bucket ARNs as **provisional estimates pending operational sync in Sprint 2.1**.
  - *Issue ID:* `SRC-121-04`
  - *Evidence Basis:* `EVID-SRC-08`, `EVID-SRC-09`
  - *Status:* **CONDITIONAL (Doc Verified / Op Sync Pending)**
- **Section 4.2 (BhashaBench-Legal Terms):**  
  - *Problem:* Ambiguity regarding training permissions.
  - *Correction:* Explicitly stated that training is **strictly prohibited** to preserve blind benchmark integrity; usage is restricted to evaluation only under gated license.
  - *Issue ID:* `SRC-121-05`
  - *Evidence Basis:* `EVID-SRC-12`
  - *Status:* **CONDITIONAL (Doc Verified / Gated Access Pending)**
- **Section 5.3 & 5.5 (IN-Abs, IN-Ext, and OpenNYAI Dual Licensing):**  
  - *Problem:* Did not distinguish code repository license from dataset/judgment content.
  - *Correction:* Delineated Apache 2.0 / MIT code licenses from underlying public domain judicial texts and CC BY 4.0 annotation layers.
  - *Issue ID:* `SRC-121-06`, `SRC-121-07`
  - *Evidence Basis:* `EVID-SRC-10`, `EVID-SRC-11`
  - *Status:* **PASS (Doc Verified)**
- **Section 6 (Unified 8-Field Matrix):**  
  - *Problem:* Inconsistent status codes across sources.
  - *Correction:* Standardized all 16 candidate sources across the 8 dimensions using strict keys: `PASS`, `COND`, `UNKNOWN`, `PROHIB`, `REST`.
  - *Issue ID:* `SRC-121-08`
  - *Status:* **PASS (Doc Verified)**

---

### `04_CANONICAL_DATA_SCHEMAS.md` (Version 1.2.1)
- **Section 3.2 (`ContractRiskRecord` Schema Update):**  
  - *Problem:* Schema lacked decoupled fields for model confidence, evidence completeness, and human review escalation.
  - *Correction:* Added `model_confidence: float = Field(default=1.0)`, `evidence_completeness: float = Field(default=1.0)`, and `review_required: bool = Field(default=False)`.
  - *Issue ID:* `TAX-121-01`
  - *Evidence Basis:* `EVID-SCH-01`
  - *Status:* **PASS (Doc Verified)**
- **Header & Dependencies:** Updated version to `1.2.1` and linked `PHASE_1_2_1_EVIDENCE_REGISTER.md`.

---

### `INDEX.md` (Version 1.2.1)
- **Master Document Matrix:** Updated directory tree to incorporate all 5 new Phase 1.2.1 governance artifacts.
- **Section 3 (Codebase Reality & Independent Verification):**  
  - *Problem:* Inspection of local application files (`backend/app/`) could not be reproduced by independent third parties from the public docs repo alone.
  - *Correction:* Explicitly labeled local inspections as **Local Observation Only / Pending Application Repository Access** to ensure complete audit transparency.
  - *Issue ID:* `CODE-121-01`
  - *Evidence Basis:* `EVID-COD-01`
  - *Status:* **CONDITIONAL (Doc Verified / Local Observation)**

---

### Core Specifications Version & Dependency Alignments (v1.2.1)
- `11_HUGGINGFACE_PIPELINE.md`: Updated to v1.2.1; dependency linked to `PHASE_1_2_1_EVIDENCE_REGISTER.md`.
- `12_DATA_QUALITY_AND_VALIDATION.md`: Updated to v1.2.1; dependency linked to `PHASE_1_2_1_EVIDENCE_REGISTER.md`.
- `14_DATASET_IMPLEMENTATION_ROADMAP.md`: Updated to v1.2.1; Gantt chart updated with Phase 1.2.1 milestones; dependency linked to `PHASE_1_2_1_ISSUE_REGISTER.md` and `PHASE_1_2_1_EVIDENCE_REGISTER.md`.

---

## 3. New Phase 1.2.1 Governance Artifacts

| File Name | Purpose & Scope |
| :--- | :--- |
| `PHASE_1_2_1_EVIDENCE_REGISTER.md` | Canonical evidence ledger cross-referencing statutory authorities (`EVID-LEG-01` to `07`), source metadata (`EVID-SRC-01` to `13`), codebase reality (`EVID-COD-01`), and ML benchmarks (`EVID-ML-01` to `02`). |
| `PHASE_1_2_1_ISSUE_REGISTER.md` | Consolidated tracking register covering all 22 remediation issues with dual-dimension verification status (`PASS`, `CONDITIONAL`, `NOT VERIFIED`, `NOT RUN`). |
| `PHASE_1_2_1_VALIDATION_REPORT.md` | Comprehensive evaluation report analyzing all 6 engineering and legal pillars, decoupling documented validation from operational execution. |
| `PHASE_1_2_1_SIGNOFF.md` | Criteria audit (AC-01 through AC-15), external dependencies, stakeholder sign-off ledger, and `CONDITIONALLY READY FOR INDEPENDENT REVIEW` readiness determination. |
| `PHASE_1_2_1_CHANGELOG.md` | Exhaustive document-by-document change log detailing every modification made during Phase 1.2.1. |
