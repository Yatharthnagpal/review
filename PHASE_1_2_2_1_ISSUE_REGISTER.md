# Phase 1.2.2.1 — Evidence Integrity & Legal Permission Issue Register

**Document ID:** `LEGALAI-DOC-DE-ISSUES-1.2.2.1`  
**Version:** `1.2.2.1`  
**Status:** Canonical Issue Remediation Tracking Register  
**Audited Date:** 2026-11-13  
**Target Platform:** LegalAI (Indian Legal Intelligence Platform)  
**Dependencies:** `INDEX.md`, `PHASE_1_2_2_1_EVIDENCE_REGISTER.md`, `PHASE_1_2_2_1_SIGNOFF.md`

---

## 1. Executive Summary

This register formally logs, tracks, and documents the resolution of all findings raised during the independent documentation, evidence-integrity, and legal-interpretation review of Phase 1.2.2 (commit `214106aad5b883343a55ac7c44e1d198f5745fe7`).

In compliance with independent review directives, all 10 identified defects (3 Critical, 4 High-Priority, 3 Medium-Priority) have been systematically investigated, root-caused, and remediated in Phase 1.2.2.1 without expanding project scope into Phase 2 implementation.

---

## 2. Consolidated Issue Tracking Table

| Issue ID | Severity | Category | Brief Description | Affected Files | Status | Resolution Summary |
|:---|:---:|:---|:---|:---|:---:|:---|
| **CRIT-1222-01** | **Critical** | Evidence Integrity | AC-02 and AC-03 cited semantically unrelated dataset evidence records (`EVID-SRC-01..04` and `EVID-SRC-07..08`). | `PHASE_1_2_2_1_SIGNOFF.md`, `PHASE_1_2_2_SIGNOFF.md` | **RESOLVED** | Remapped AC-02 to `EVID-SRC-07` (India Code) & `EVID-LEG-03` (§ 52(1)(q)). Remapped AC-03 to `EVID-SRC-05` (CUAD) & `EVID-SRC-06` (MAUD). Re-audited AC-01 to AC-15. |
| **CRIT-1222-02** | **Critical** | Verification Tooling | Audit script `scripts/audit_docs_integrity.py` declared in validation report was missing from repository. | `scripts/audit_docs_integrity.py`, `PHASE_1_2_2_1_VALIDATION_REPORT.md` | **RESOLVED** | Developed, committed, and executed deterministic Python audit script supporting versioned register selection, link checking, signoff path checks, and semantic AC checks. |
| **CRIT-1222-03** | **Critical** | Documentation Integrity | Sign-off referenced 8 nonexistent file paths (e.g. `04_CANONICAL_DATA_SCHEMA.md`, `06_DATA_PREPROCESSING_PIPELINE.md`). | `PHASE_1_2_2_1_SIGNOFF.md`, `PHASE_1_2_2_SIGNOFF.md` | **RESOLVED** | Corrected every file reference to existing canonical files (`04_CANONICAL_DATA_SCHEMAS.md`, `09_DATA_PREPROCESSING_PIPELINE.md`, etc.). Stated multi-file criteria explicitly. |
| **HIGH-1222-01** | **High** | Legal / Permissions | Judicial data AI training permissions were inconsistent (monolithic "Training Use" conflating pretraining, SFT, RAG). | `02_SOURCE_REGISTRY.md`, `03_LICENSE_AND_PROVENANCE_POLICY.md` | **RESOLVED** | Deconstructed permissions into 10 granular technical operations. Classified model training, pretraining, and commercial RAG on court judgments as `CONDITIONAL ON LEGAL REVIEW`. |
| **HIGH-1222-02** | **High** | Legal Interpretation | Recent Indian copyright litigation (*ANI Media v. OpenAI*, Delhi HC interim order 24 July 2026) was omitted. | `03_LICENSE_AND_PROVENANCE_POLICY.md`, `PHASE_1_2_2_1_EVIDENCE_REGISTER.md` | **RESOLVED** | Added subsection 2.2.1 in `03` and new canonical evidence entry `EVID-LEG-09`. Accurately qualified interim procedural nature and unsettled statutory TDM landscape under § 52(1)(a). |
| **HIGH-1222-03** | **High** | Legal Interpretation | *BALCO* proposition in Section 3.2 was overbroad, asserting full party autonomy over substantive law, seat, and jurisdiction. | `05_LABEL_TAXONOMY.md` (§ 3.2), `PHASE_1_2_2_1_EVIDENCE_REGISTER.md` | **RESOLVED** | Narrowed *BALCO* to territoriality and seat vs. venue curial supervision. Documented Section 28 ACA substantive law limits, *PASL Wind*, and CPC jurisdiction limits under *Hakam Singh*. |
| **HIGH-1222-04** | **High** | Statutory Analysis | Family Courts Act § 11 in-camera procedure was conflated with a statutory penal ban on appellate case law publication. | `03_LICENSE_AND_PROVENANCE_POLICY.md` (§ 4.3), `PHASE_1_2_2_1_EVIDENCE_REGISTER.md` | **RESOLVED** | Distinguished in-camera trial procedure (*Santhini*) from penal publication bans. Contrasted with Hindu Marriage Act § 22. Clarified 7-step screening as internal LegalAI precautionary policy. |
| **MED-1222-01** | **Medium** | Contract Licensing | Underlying CUAD and MAUD contract collection/storage was labelled "allowed" despite Atticus copyright disclaimers. | `02_SOURCE_REGISTRY.md` (§ 2), `03_LICENSE_AND_PROVENANCE_POLICY.md` (§ 2.4) | **RESOLVED** | Reclassified collection and storage of underlying SEC EDGAR contracts as `CONDITIONAL / RESTRICTED` (internal quarantine evaluation only; commercial serving & redistribution barred). |
| **MED-1222-02** | **Medium** | Documentation Schema | Ambiguity between 14 registry metadata fields, 8 verification dimensions, and operational permissions. | `02_SOURCE_REGISTRY.md` (§ 1.2), `INDEX.md` (§ 3) | **RESOLVED** | Created explicit three-tier mapping table in Section 1.2 of `02_SOURCE_REGISTRY.md` and Section 3 of `INDEX.md`. |
| **MED-1222-03** | **Medium** | Audit Provenance | Validation report did not clearly record the exact reviewed commit SHA and full audit provenance chain. | `PHASE_1_2_2_1_VALIDATION_REPORT.md`, `PHASE_1_2_2_1_SIGNOFF.md` | **RESOLVED** | Documented exact commit chain: Baseline (`1d374ad`), Reviewed (`214106a`), and Remediation HEAD, alongside exact ISO execution timestamps and audited file paths. |

---

## 3. Remediation Details & Root Cause Analysis

### 3.1 CRIT-1222-01: Semantic Evidence Alignment
* **Root Cause:** In Phase 1.2.2, sign-off evidence rows were updated using contiguous evidence ID blocks (`EVID-SRC-01..04`, `EVID-SRC-05..08`) without cross-checking the substantive topics in the Evidence Register.
* **Remediation Action:**
  - AC-02 (India Code / portal licensing): Remapped to `EVID-SRC-07` (Official India Code) and `EVID-LEG-03` (Copyright Act § 52(1)(q)).
  - AC-03 (CUAD/MAUD rights separation): Remapped to `EVID-SRC-05` (CUAD v1) and `EVID-SRC-06` (MAUD).
  - AC-04 (Canonical Schemas): Added `EVID-COD-01` to harmonize with backend codebase reality.
  - AC-07 (Data Splitting): Added `EVID-ML-01` and `EVID-ML-02`.
  - AC-09 (Privacy & Redaction): Remapped to `EVID-LEG-02`, `EVID-LEG-04`, `EVID-LEG-05`, `EVID-LEG-06`.
  - AC-11 (Dataset Cards): Remapped to `EVID-SRC-05`, `EVID-SRC-07`, `EVID-LEG-03`.
  - AC-13 (Traceability): Remapped to `EVID-LEG-01`, `EVID-COD-01`, `EVID-SCH-01`.
* **Verification:** Validated by automated execution of `scripts/audit_docs_integrity.py`.

### 3.2 CRIT-1222-02: Missing Audit Tooling
* **Root Cause:** The script path `scripts/audit_docs_integrity.py` was referenced in the Phase 1.2.2 validation report before the script file was committed to the workspace.
* **Remediation Action:** Created `scripts/audit_docs_integrity.py` with full standard-library support, semantic AC mapping rules, version-aware artifact resolution, broken link detection, and signoff document path validation.

### 3.3 CRIT-1222-03: Sign-off File Reference Precision
* **Root Cause:** The signoff matrix used descriptive or singular file titles (e.g., `04_CANONICAL_DATA_SCHEMA.md` instead of `04_CANONICAL_DATA_SCHEMAS.md`; `06_DATA_PREPROCESSING_PIPELINE.md` instead of `09_DATA_PREPROCESSING_PIPELINE.md`) and assumed dedicated standalone files for topics covered across multiple canonical documents (synthetic data, dataset cards).
* **Remediation Action:** Corrected all paths to exact, verified disk filenames and explicitly documented where criteria are governed across multiple canonical specifications.
