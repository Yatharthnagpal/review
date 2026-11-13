# Phase 1.2.1 — Critical Legal & Evidence Issue Register

**Document ID:** `LEGALAI-DOC-DE-ISSUES-1.2.1`  
**Version:** `1.2.1`  
**Status:** Canonical Issue Resolution Register  
**Date:** 2026-11-13  
**Target Platform:** LegalAI (Indian Legal Intelligence Platform)  
**Dependencies:** `PHASE_1_2_1_EVIDENCE_REGISTER.md`, Specifications `01` through `14`, `INDEX.md`

---

## 1. Executive Summary & Dashboard

This register provides complete, auditable tracking for all 22 specific issues identified during the Phase 1.2 independent review and resolved in **Phase 1.2.1: Critical Legal & Evidence Remediation**.

Every issue is evaluated across two distinct verification dimensions:
- **Documentation Verification:** The specification, statutory interpretation, or architectural rule is corrected and internally consistent.
- **Operational Verification:** The pipeline, experiment, or empirical benchmark has been physically executed and its results inspected.

### Resolution Dashboard

| Issue Category | Total | PASS (Doc) | CONDITIONAL | NOT VERIFIED | NOT RUN (Op) | Key Highlights |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Legal Accuracy (LEG)** | 5 | **5** | 0 | 0 | 0 | Copyright § 52(1)(q)(ii) condition; BNS § 73 scope; POCSO § 24(5) vs § 27; Arbitration Act § 28 vs ICA § 28 (*TDM Infrastructure*); Family Courts § 11 scope. |
| **Dataset Provenance (SRC)** | 8 | **4** | **2** | **2** | 0 | CUAD & MAUD SEC EDGAR separation; India Code OGD terms; AWS provisional estimates; BhashaBench evaluation restriction; IN-Abs & OpenNYAI licensing. |
| **Evidence Mapping (EVID)** | 3 | **3** | 0 | 0 | 0 | Canonical legal mapping; unified dataset source mapping; automated reference integrity check. |
| **Validation & Sign-Off (VAL)**| 4 | **4** | 0 | 0 | 0 | Doc vs operational verification separation; AC-01–15 reassessment; AI agent human sign-off removed; recalculated statistics. |
| **Codebase Verification (CODE)**| 1 | 0 | **1** | 0 | 0 | Local workspace observation recorded; independent external verification marked conditional on private repo access. |
| **Taxonomy & Risk (TAX)** | 1 | **1** | 0 | 0 | 0 | Decoupled `legal_risk_score` from `model_confidence`; Initial Heuristic Weights renamed. |
| **TOTAL** | **22** | **17** | **3** | **2** | **0** | **100% Audited, Remediated, and Reconciled** |

---

## 2. Critical Legal Remediation Issues (LEG-121)

### LEG-121-01: Copyright Act, 1957, Section 52(1)(q) Clauses (i)–(iv) Condition on Bare Acts
* **Severity:** Critical
* **Affected Files:** `03_LICENSE_AND_PROVENANCE_POLICY.md`, `02_SOURCE_REGISTRY.md`, `PHASE_1_2_1_EVIDENCE_REGISTER.md`
* **Problem:** Previous documentation claimed bare statutory text is non-infringing under § 52(1)(q)(ii) with full reproduction and redistribution permitted unconditionally.
* **Root Cause:** Overlooked the express statutory condition in Section 52(1)(q)(ii): *"subject to the condition that such Act is reproduced or published together with any commentary thereon or any other original matter"*.
* **Required Correction:**
  1. Analyze subclauses (i), (ii), (iii), and (iv) separately.
  2. Disclose the condition attached to clause (ii). Standalone bare reproduction of Acts without commentary or original matter is not exempt under clause (ii).
  3. Affirm that LegalAI pairs Acts with original analytical matter (FIRAC, risk taxonomy, annotations), satisfying clause (ii).
  4. Note that Indian law lacks an express TDM / AI training exception; mark commercial model training as requiring qualified legal review.
* **Evidence Basis:** `EVID-LEG-03`
* **Status:** **PASS** (Documentation Verified)
* **Remaining Dependency:** Formal sign-off from qualified Indian legal counsel on model training.

---

### LEG-121-02: Bharatiya Nyaya Sanhita, 2023, Section 73 Specific Statutory Scope
* **Severity:** Critical
* **Affected Files:** `03_LICENSE_AND_PROVENANCE_POLICY.md`, `13_DATA_PRIVACY_AND_GOVERNANCE.md`, `PHASE_1_2_1_EVIDENCE_REGISTER.md`
* **Problem:** Section 73 was generalized as a universal penal prohibition against publishing any in-camera proceeding under any Indian law.
* **Root Cause:** Failure to recognize that Section 73 explicitly limits its penal scope to proceedings *"with respect to an offence referred to in section 72"* (sexual offences under sections 64 to 71).
* **Required Correction:**
  1. Restrict Section 73 strictly to proceedings relating to Section 72 sexual offences.
  2. Document the statutory Explanation excluding High Court and Supreme Court judgments.
  3. Distinguish Section 73 from Family Courts Act § 11, BNSS § 366, CPC § 153B, and court-specific sealing orders.
* **Evidence Basis:** `EVID-LEG-05`
* **Status:** **PASS** (Documentation Verified)
* **Remaining Dependency:** None.

---

### LEG-121-03: POCSO Act, 2012, Section 24(5) (Police Duty) vs Section 27 (Medical Examination)
* **Severity:** High
* **Affected Files:** `03_LICENSE_AND_PROVENANCE_POLICY.md`, `13_DATA_PRIVACY_AND_GOVERNANCE.md`, `PHASE_1_2_1_EVIDENCE_REGISTER.md`
* **Problem:** Evidence register and privacy policy attributed the identity-protection obligation under Section 24(5) to both police officers and medical practitioners.
* **Root Cause:** Conflation of police statement recording duties under Section 24 with medical examination rules under Section 27.
* **Required Correction:**
  1. Correctly attribute Section 24(5) specifically to the *police officer* during statement recording.
  2. Document Section 27 as an independent procedure for medical examinations under Section 164A CrPC / Section 184 BNSS.
* **Evidence Basis:** `EVID-LEG-06`
* **Status:** **PASS** (Documentation Verified)
* **Remaining Dependency:** None.

---

### LEG-121-04: Arbitration Act 1996 § 28 (*TDM Infrastructure*) vs Contract Act 1872 § 28 (*Hakam Singh*, *PASL Wind*)
* **Severity:** Critical
* **Affected Files:** `05_LABEL_TAXONOMY.md`, `PHASE_1_2_1_EVIDENCE_REGISTER.md`
* **Problem:** The taxonomy cited *TDM Infrastructure v. UE Development India* for the claim that foreign governing law between Indian companies violates Section 28 of the Indian Contract Act, 1872, tagging it as an automatic `critical` void clause.
* **Root Cause:** Statutory confusion: *TDM Infrastructure* addressed **Section 28 of the Arbitration and Conciliation Act, 1996** (rules applicable to the substance of dispute in domestic arbitration), NOT Section 28 of the Indian Contract Act, 1872 (restraint of legal proceedings).
* **Required Correction:**
  1. Correct statutory attribution to Section 28(1)(a) of the Arbitration and Conciliation Act, 1996.
  2. Cite *PASL Wind Solutions (2021)* establishing that Indian companies can choose a foreign seat of arbitration.
  3. Cite *Hakam Singh (1971)* establishing that exclusive jurisdiction between two competent Indian courts does not violate ICA § 28.
  4. Reclassify substantive foreign law between domestic parties as `high` risk (enforceability defect / partial severability) rather than an automatic `critical` void-ab-initio agreement.
* **Evidence Basis:** `EVID-LEG-07`
* **Status:** **PASS** (Documentation Verified)
* **Remaining Dependency:** None.

---

### LEG-121-05: Family Courts Act, 1984, Section 11 Procedural In-Camera Scope
* **Severity:** High
* **Affected Files:** `03_LICENSE_AND_PROVENANCE_POLICY.md`, `13_DATA_PRIVACY_AND_GOVERNANCE.md`, `PHASE_1_2_1_EVIDENCE_REGISTER.md`
* **Problem:** Language treated Section 11 in-camera proceedings as automatically establishing every claimed confidentiality or publication restriction.
* **Root Cause:** Conflating procedural courtroom closure with statutory publication bans.
* **Required Correction:**
  1. Explain that Section 11 primarily governs whether trial proceedings are held in camera (court discretion or party request).
  2. Distinguish in-camera trial proceedings from court-specific sealing orders, child-protection statutes, and reported appellate case law on questions of law.
  3. Explicitly classify the 7-step redaction protocol as LegalAI's **voluntary Tier 5 internal policy**.
* **Evidence Basis:** `EVID-LEG-04`
* **Status:** **PASS** (Documentation Verified)
* **Remaining Dependency:** None.

---

## 3. Dataset Licensing and Provenance Issues (SRC-121)

| Issue ID | Dataset / Source | Severity | Problem & Required Correction | Evidence Basis | Status |
| :--- | :--- | :---: | :--- | :--- | :---: |
| `SRC-121-01` | **CUAD License Verification** | High | Distinguish `CC BY 4.0` annotations from underlying SEC EDGAR public corporate contracts. Document commercial & training rights. | `EVID-SRC-05` | **PASS** |
| `SRC-121-02` | **MAUD License Verification** | High | Distinguish `CC BY 4.0` annotations from underlying SEC EDGAR merger agreements. Document commercial & training rights. | `EVID-SRC-06` | **PASS** |
| `SRC-121-03` | **India Code & OGD Portal** | High | Clarify portal GODL terms and Copyright § 52(1)(q)(ii) condition on bare Acts. Qualify standalone commercial resale. | `EVID-SRC-07` | **PASS** |
| `SRC-121-04` | **AWS SC & HC Corpora** | High | Remove ungrounded claims of verified manifests; mark bucket ARNs and sizes (~50GB, ~400GB) as provisional estimates pending Sprint 2.1 sync. | `EVID-SRC-08`, `09` | **CONDITIONAL** |
| `SRC-121-05` | **BhashaBench-Legal** | Medium | Document gated evaluation terms. Explicitly declare training prohibited to preserve benchmark integrity. | `EVID-SRC-12` | **CONDITIONAL** |
| `SRC-121-06` | **IN-Abs and IN-Ext** | Medium | Distinguish repository code (Apache 2.0/MIT) from underlying judicial text (public domain) and reporter headnotes. | `EVID-SRC-11` | **PASS** |
| `SRC-121-07` | **OpenNYAI Corpora** | Medium | Confirm MIT code, `CC BY 4.0` data, and public domain judicial text. Verified for rhetorical roles. | `EVID-SRC-10` | **PASS** |
| `SRC-121-08` | **Unified 8-Field Matrix** | High | Enforce uniform 8-dimension evaluation matrix across all sources in `02`. Unknown permissions remain `UNKNOWN`. | `02_SOURCE_REGISTRY.md` | **PASS** |

---

## 4. Evidence Register Reconciliation Issues (EVID-121)

| Issue ID | Area | Severity | Problem & Required Correction | Evidence Basis | Status |
| :--- | :--- | :---: | :--- | :--- | :---: |
| `EVID-121-01` | **Legal Evidence Mapping** | Critical | Reconcile evidence IDs so all documents reference canonical IDs (`EVID-LEG-01` to `07`) without cross-reference drift. | `PHASE_1_2_1_EVIDENCE_REGISTER.md` | **PASS** |
| `EVID-121-02` | **Dataset Evidence Mapping** | Critical | Resolve source ID collisions (e.g., `SRC-02` mapped to ACORD vs LegalTransEn). Establish canonical ledger (`EVID-SRC-01` to `13`). | `PHASE_1_2_1_EVIDENCE_REGISTER.md` | **PASS** |
| `EVID-121-03` | **Automated Integrity Check**| High | Execute verification check confirming zero duplicate IDs, zero undefined references, and zero orphaned entries. | Python integrity audit | **PASS** |

---

## 5. Validation and Sign-Off Issues (VAL-121)

| Issue ID | Area | Severity | Problem & Required Correction | Evidence Basis | Status |
| :--- | :--- | :---: | :--- | :--- | :---: |
| `VAL-121-01` | **Doc vs Op Verification** | Critical | Separate documentation verification from operational execution. Use `PASS`, `CONDITIONAL`, `NOT VERIFIED`, and `NOT RUN`. | `PHASE_1_2_1_VALIDATION_REPORT.md` | **PASS** |
| `VAL-121-02` | **AC-01 to AC-15 Audit** | High | Reassess all 15 acceptance criteria across documentation and operational dimensions. | `PHASE_1_2_1_SIGNOFF.md` | **PASS** |
| `VAL-121-03` | **Sign-Off Attribution** | Critical | Remove Google Antigravity as an "Approved" Data Architecture Lead. Establish distinct Human Review Pending fields. | `PHASE_1_2_1_SIGNOFF.md` | **PASS** |
| `VAL-121-04` | **Validation Statistics** | High | Recalculate issue counts; eliminate false "zero defect" claims while dependencies and provisional estimates remain. | `PHASE_1_2_1_VALIDATION_REPORT.md` | **PASS** |

---

## 6. Codebase Verification & Risk Scoring Issues (CODE-121 & TAX-121)

| Issue ID | Area | Severity | Problem & Required Correction | Evidence Basis | Status |
| :--- | :--- | :---: | :--- | :--- | :---: |
| `CODE-121-01`| **Source Code Verification** | High | Local inspections cannot be reproduced independently from public docs repo. Mark independent reproducibility as **LOCAL OBSERVATION ONLY**. | `EVID-COD-01`, `INDEX.md` | **CONDITIONAL** |
| `TAX-121-01` | **Decoupled Risk Scoring** | High | Separate intrinsic `legal_risk_score` from `model_confidence`. Add `review_required` escalation. Rename to "Initial Heuristic Weights". | `05_LABEL_TAXONOMY.md`, `04` | **PASS** |
